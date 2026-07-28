"""§7 agentic retrieval loop.

The design doc chose repeated LLM-directed retrieval over a single
route->vector->graph->merge pass (§14.3), because a multi-hop question rarely has
its evidence in one search. That choice buys recall and costs latency and tokens,
so everything here is about bounding the cost:

* §7.2 budget — iterations, tool calls, and a wall-clock deadline standing in for
  the §12 p95 SLA. Exhaustion never hides itself: it forces confidence "low".
* §7.3 role split — a light model picks actions, a larger one writes the answer.
* §14.8 context — tool results accumulate, so older ones collapse to a re-fetchable
  id once the accumulated text passes CONTEXT_BUDGET_CHARS.
* §7.4 — citations are verified against observed evidence after synthesis.

The loop is invisible from outside: §7.5 keeps the §8.1 request/response contract
unchanged, with the trace exposed only for debugging.
"""
from __future__ import annotations

import json
import time
from dataclasses import dataclass, field

from qa import config
from qa.llm import extract_json
from qa.prompts import LOOP_SYSTEM, SYNTHESIS_SYSTEM
from qa.verify import verify_citations

_VALID_CONFIDENCE = ("high", "medium", "low")
_ELIDED = "[result elided to save context — re-fetch by ref_id if you still need it]"


@dataclass
class LoopResult:
    answer: str
    citations: list = field(default_factory=list)
    related_entities: list = field(default_factory=list)
    confidence: str = "low"
    evidence: list = field(default_factory=list)
    trace: list = field(default_factory=list)
    iterations: int = 0
    tool_calls: int = 0
    budget_exhausted: bool = False
    dropped_citations: list = field(default_factory=list)
    duration_ms: int = 0


class AgenticLoop:
    def __init__(self, actions, *, action_model=None, synthesis_model=None,
                 max_iterations=None, max_tool_calls=None, deadline_ms=None,
                 chat_fn=None):
        self.actions = actions
        self.action_model = action_model or config.ACTION_MODEL
        self.synthesis_model = synthesis_model or config.MODEL
        self.max_iterations = max_iterations or config.MAX_ITERATIONS
        self.max_tool_calls = max_tool_calls or config.MAX_TOOL_CALLS
        self.deadline_ms = deadline_ms or config.DEADLINE_MS
        self._chat_fn = chat_fn

    async def _chat(self, messages, *, model, tools=None, tool_choice="auto"):
        if self._chat_fn is not None:
            return await self._chat_fn(messages, model=model, tools=tools,
                                       tool_choice=tool_choice)
        from qa import llm

        return await llm.chat(messages, model=model, tools=tools, tool_choice=tool_choice)

    def _build_messages(self, query, conversation_context):
        messages = [{"role": "system", "content": LOOP_SYSTEM}]
        if conversation_context:
            # §8.3: prior turns are context for re-reading the question, not state
            # this agent owns. They are summarised into the user turn and dropped.
            rendered = "\n".join(
                f"- {t.get('role', 'user')}: {t.get('content', '')}"
                for t in conversation_context if isinstance(t, dict)
            )
            messages.append({"role": "user", "content":
                             f"Earlier turns, for interpreting the question only:\n{rendered}"})
        messages.append({"role": "user", "content": query})
        return messages

    def _compact(self, messages, accumulated):
        """§14.8: collapse the oldest tool payloads once the transcript gets heavy."""
        if accumulated <= config.CONTEXT_BUDGET_CHARS:
            return accumulated
        for msg in messages:
            if msg.get("role") != "tool" or msg.get("content") == _ELIDED:
                continue
            accumulated -= len(msg["content"])
            msg["content"] = _ELIDED
            if accumulated <= config.CONTEXT_BUDGET_CHARS:
                break
        return accumulated

    async def run(self, query, *, scope_filter=None, conversation_context=None):
        t0 = time.monotonic()
        messages = self._build_messages(query, conversation_context)
        schemas = list(getattr(self.actions, "TOOL_SCHEMAS", []))

        evidence: list = []
        trace: list = []
        tool_calls = 0
        iterations = 0
        accumulated = 0
        budget_exhausted = False
        first_search = True
        final_text = ""

        while iterations < self.max_iterations:
            if (time.monotonic() - t0) * 1000 >= self.deadline_ms:
                budget_exhausted = True
                break
            iterations += 1

            resp = await self._chat(messages, model=self.action_model,
                                    tools=schemas, tool_choice="auto")
            msg = resp.choices[0].message
            calls = getattr(msg, "tool_calls", None)

            assistant_msg = {"role": "assistant", "content": msg.content or ""}
            if calls:
                assistant_msg["tool_calls"] = [
                    {"id": c.id, "type": "function",
                     "function": {"name": c.function.name, "arguments": c.function.arguments}}
                    for c in calls
                ]
            messages.append(assistant_msg)

            if not calls:
                final_text = msg.content or ""
                break

            for call in calls:
                tool_calls += 1
                name = call.function.name
                raw_args = call.function.arguments or "{}"
                step = {"iteration": iterations, "action": name, "args": None,
                        "evidence": 0, "chars": 0}
                try:
                    args = json.loads(raw_args)
                    if not isinstance(args, dict):
                        raise ValueError("arguments were not a JSON object")
                except (json.JSONDecodeError, ValueError) as exc:
                    text = f"Error: malformed arguments for {name!r} ({exc}): {raw_args!r}"
                    step["error"] = text
                    trace.append(step)
                    messages.append({"role": "tool", "tool_call_id": call.id, "content": text})
                    accumulated += len(text)
                    continue

                # §7.0's hint reaches the first search only if the model did not
                # pick its own scope — the hint is advisory, not a constraint.
                if name == "vector_search" and first_search:
                    first_search = False
                    if scope_filter and not args.get("scope_filter"):
                        args["scope_filter"] = scope_filter

                result = await self.actions.run(name, args)
                evidence.extend(result.evidence)
                step.update({"args": args, "evidence": len(result.evidence),
                             "chars": len(result.text)})
                trace.append(step)
                messages.append({"role": "tool", "tool_call_id": call.id, "content": result.text})
                accumulated += len(result.text)

            accumulated = self._compact(messages, accumulated)

            if tool_calls >= self.max_tool_calls:
                budget_exhausted = True
                break

        if iterations >= self.max_iterations and not final_text:
            budget_exhausted = True

        if not final_text:
            # §7.2: forced termination still owes the caller a real answer.
            budget_exhausted = True
            messages.append({"role": "system", "content": SYNTHESIS_SYSTEM})
            resp = await self._chat(messages, model=self.synthesis_model,
                                    tools=schemas, tool_choice="none")
            final_text = resp.choices[0].message.content or ""

        result = self._finalise(final_text, evidence, budget_exhausted)
        result.trace = trace
        result.iterations = iterations
        result.tool_calls = tool_calls
        result.evidence = evidence
        result.budget_exhausted = budget_exhausted
        result.duration_ms = int((time.monotonic() - t0) * 1000)
        return result

    def _finalise(self, final_text, evidence, budget_exhausted):
        payload = extract_json(final_text)
        if not isinstance(payload, dict):
            # Unparseable output is still worth returning, but it carries no
            # verifiable citations, so it cannot claim confidence.
            return LoopResult(answer=(final_text or "").strip(), citations=[],
                              related_entities=[], confidence="low")

        confidence = str(payload.get("confidence", "")).lower()
        if confidence not in _VALID_CONFIDENCE:
            confidence = "low"

        verified = verify_citations(payload.get("citations") or [], evidence)
        if verified.dropped and not verified.citations:
            confidence = "low"  # §7.4: nothing survived the grounding check
        if budget_exhausted:
            confidence = "low"  # §7.2

        related = [str(e) for e in (payload.get("related_entities") or []) if e]
        return LoopResult(
            answer=str(payload.get("answer", "")).strip(),
            citations=verified.citations,
            related_entities=related,
            confidence=confidence,
            dropped_citations=verified.dropped,
        )

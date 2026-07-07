# Swap the agent LLM backend from Claude to an OpenAI-compatible endpoint (gpt-oss-120B)

**Date**: 2026-07-07
**Status**: Approved

## Goal

Run the entire agent stack — the answering agent, the eval judge, and the v2
search sufficiency judge — on a company-hosted **gpt-oss-120B** model exposed
through an **OpenAI-compatible** API (`/v1/chat/completions` with function
calling). Remove the Anthropic dependency entirely: no `claude-agent-sdk`, no
`anthropic`. This is a full, one-provider replacement (not a switchable
abstraction).

## Constraints (from the user)

- Endpoint is OpenAI-compatible (`/v1/chat/completions`, supports tool/function
  calling).
- **All three LLM roles** (agent, judge, sufficiency) use the same
  gpt-oss-120B model.
- **Do not use the Claude Agent SDK.** Reimplement the agent loop directly.
- OpenAI-only: drop `claude-agent-sdk` and `anthropic` from dependencies.
- Keep the public `BluetoothWikiAgent(...).ask(question) -> AgentResponse`
  contract unchanged so `server/http.py`, `server/mcp.py`, and eval callers
  need no changes.

## Non-goals

- No switchable multi-provider abstraction (OpenAI-only, per decision).
- No re-tuning of the anti-hallucination system prompt for gpt-oss. The port
  is mechanical; prompt tuning is a separate follow-up if answer quality needs
  it (flagged as a risk, not built here).
- No change to the search strategies, chunker, index, or tool *logic* — only
  the LLM client and the tool *wiring*.
- No change to `server/` (the agent's public interface is preserved).

## Architecture

Reuse everything that is already provider-neutral; replace only the LLM client
and the agentic loop.

```
OPENAI_BASE_URL / OPENAI_API_KEY / MODEL
        │
   agent/llm.py  (get_client(): cached AsyncOpenAI)   ← NEW, shared
        ├── agent/agent.py       hand-rolled tool-calling loop   ← REWRITE
        ├── eval/judge.py        chat.completions.create         ← swap client
        └── search/sufficiency.py chat.completions.create        ← swap client

agent/tools.py   provider-neutral tool registry (schemas + handlers)  ← REWRITE wiring
    └── _list_index / _search_wiki_async / _read_page / _read_source  ← UNCHANGED logic
```

## Components

### 1. `agent/llm.py` (new) — shared OpenAI client factory

- `get_client() -> AsyncOpenAI` — module-cached
  `AsyncOpenAI(base_url=OPENAI_BASE_URL, api_key=OPENAI_API_KEY)`.
- One place configures the endpoint; agent, judge, and sufficiency all import
  it (DRY).

### 2. `agent/config.py`

- Replace `ANTHROPIC_API_KEY` with `OPENAI_API_KEY` (env; may be a dummy token
  for an internal endpoint) and add `OPENAI_BASE_URL` (env, no default that
  points at OpenAI's public API — require it to be set, or default to the
  company endpoint placeholder).
- `MODEL` (`BT_AGENT_MODEL`), `JUDGE_MODEL` (`BT_AGENT_JUDGE_MODEL`), and
  `SUFFICIENCY_MODEL` (`BT_AGENT_SUFFICIENCY_MODEL`) default to the
  gpt-oss-120B model id.
- Keep `MAX_TURNS`, `SEARCH_*`, `SUFFICIENCY_MAX_ITER`, etc.

### 3. `agent/tools.py` — provider-neutral tool registry

- Remove `from claude_agent_sdk import tool` and `create_sdk_mcp_server`, and
  the `mcp__bluetooth-wiki__*` name prefixes.
- Define each tool as a plain record: `name`, `description`, a JSON-Schema
  `parameters` object (OpenAI function-calling format), and an async
  `handler(args: dict) -> str` that calls the existing pure-logic function and
  returns the text (drop the MCP `{"content":[...]}` envelope — the loop wants
  the string).
- Tool set and schemas (unchanged contract):
  - `list_index` — params `{}`.
  - `search_wiki` — params `{query: string (required), scope: string enum
    [wiki, sources, both]}`; bound to the active search strategy.
  - `read_page` — params `{path: string (required)}`.
  - `read_source` — params `{version: string (required), vol: string, part:
    string}`.
- `build_tools(strategy_name)` returns `(openai_tool_schemas: list[dict],
  handlers: dict[str, callable])` so the agent loop has both the schemas to
  send and the dispatch map to execute.

### 4. `agent/agent.py` — hand-rolled tool-calling loop (rewrite)

- Construct once: system prompt (unchanged file), tool schemas + handlers from
  `build_tools`.
- `ask(question)`:
  1. `messages = [{"role":"system", ...}, {"role":"user", ...}]`.
  2. Loop up to `MAX_TURNS`:
     - `resp = await client.chat.completions.create(model=MODEL,
       messages=messages, tools=schemas, tool_choice="auto")`.
     - Append the assistant message. If it has `tool_calls`: execute each
       (parse `arguments` JSON, dispatch to the handler, append a
       `{"role":"tool", "tool_call_id":..., "content": result}` message per
       call — handles parallel tool calls), then continue the loop.
     - Else (no tool calls): this message's content is the final answer →
       stop.
  3. Parse the final text with the existing `_parse_final_text` /
     `extract_json_payload` (unchanged), hydrate citations (unchanged).
- Populate `AgentResponse` (same dataclass): `answer/citations/reasoning/raw`
  from the parse; `tool_calls` and `tools_used` counted in the loop;
  `num_turns` = loop iterations; `usage` from `resp.usage`
  (prompt/completion tokens, summed across turns); `duration_ms` measured
  locally; `total_cost_usd = None` (internal endpoint gives no cost);
  `stop_reason` from the final `resp.choices[0].finish_reason`.
- Robustness: if the model emits a tool call for an unknown tool or bad JSON
  args, return an error string as the tool result (so the model can recover)
  rather than crashing the loop. If `MAX_TURNS` is hit without a final
  answer, fall back to the last assistant text.

### 5. `eval/judge.py` and `search/sufficiency.py`

- Replace `from anthropic import AsyncAnthropic` / `AsyncAnthropic()` with the
  shared `get_client()`.
- Convert the call: Anthropic takes `system=` as a separate param; OpenAI
  takes a `{"role":"system"}` message. Move the system text into `messages`.
  `max_tokens` → `max_tokens` (same). Read text from
  `resp.choices[0].message.content`.
- JSON extraction via existing `extract_json_payload` unchanged. Fail-open /
  heuristic-fallback behavior in sufficiency unchanged.

### 6. `agent/__init__.py`

- Update the docstring (it references `claude_agent_sdk` as the reason for the
  lazy `BluetoothWikiAgent` import; the reason is now `openai`). Keep the lazy
  `__getattr__` import so `agent.config`/`agent.citations` stay importable
  without `openai` for pure-logic consumers (search, scripts, their tests).

### 7. `pyproject.toml`

- Remove `claude-agent-sdk>=0.1.0` and `anthropic>=0.39.0`.
- Add `openai>=1.0` (async client + function calling).
- Keep `mcp>=1.0.0` — used by `server/mcp.py` to expose the agent *as* an MCP
  server to external clients; unrelated to the LLM backend.

### 8. `.env.example`

- Replace `ANTHROPIC_API_KEY=sk-ant-...` with `OPENAI_API_KEY=...` and add
  `OPENAI_BASE_URL=` (company gpt-oss endpoint).
- Set `BT_AGENT_MODEL`, `BT_AGENT_JUDGE_MODEL`, `BT_AGENT_SUFFICIENCY_MODEL`
  to the gpt-oss-120B id.

### 9. Docs

- Update `README.md` and `CLAUDE.md` where they name the model/provider or the
  `ANTHROPIC_*` env vars, per the repo's keep-docs-in-sync rule.

## Data flow (one `ask`)

```
question ─► [system, user] ─► chat.completions.create(tools) ─┐
             ▲                                                 │
             │  append tool results                     tool_calls?
             │        (role="tool")                        │  │
             └──────── execute handlers ◄──────────────────┘  │ no
                                                              ▼
                            final assistant text ─► extract_json_payload ─► AgentResponse
```

## Testing

- **Tool-schema conversion** — assert `build_tools("v1")` yields OpenAI
  function schemas with the right names/required params for all four tools and
  a handler map covering them.
- **Agent loop (fake client)** — a stub OpenAI client whose first
  `create` returns a `tool_calls` response (e.g. `search_wiki`) and whose
  second returns a final `content` with a fenced ```json answer. Assert the
  loop: executes the tool (real pure-logic handler over the repo), appends the
  tool result, then parses `AgentResponse` (answer/citations/reasoning,
  `tool_calls == 1`, `tools_used == {"search_wiki": 1}`). No network.
- **Loop safety** — fake client that returns an unknown tool call → loop
  returns an error tool result and continues; and a client that never stops →
  loop terminates at `MAX_TURNS` with a best-effort answer.
- **judge / sufficiency (fake client)** — mock `get_client()` to return a
  canned JSON string; assert parsing and the `SufficiencyVerdict` /
  judge-score shapes are unchanged.
- **Smoke test against the real endpoint** (manual, in the plan's final step,
  gated on `OPENAI_BASE_URL` being set): one real `ask` that must produce at
  least one tool call and a parseable answer — this is the gpt-oss
  tool-calling reliability check flagged below.

## Risks

1. **Tool-calling reliability on gpt-oss (highest).** The agent is worthless
   if the model won't reliably emit well-formed function calls. Mitigation: the
   loop tolerates malformed/unknown calls (feeds an error back), and the plan
   ends with a real-endpoint smoke test. If it proves unreliable, prompt/tool
   description tuning is the follow-up.
2. **System prompt tuned for Claude.** Out of scope to re-tune here; flagged so
   answer-quality regressions are attributed correctly.
3. **Cost/latency telemetry.** `total_cost_usd` is unavailable from an internal
   endpoint (set `None`); token usage still comes from `resp.usage`.
4. **Parallel tool calls / streaming.** Non-streaming `create` is used for
   simplicity; parallel `tool_calls` are handled as a list.

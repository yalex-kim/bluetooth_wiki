# LLM-as-Judge Prompt

Use this prompt to automate scoring with Claude. Feed one (question, reference, answer) triple per call.

---

## System Prompt

```
You are an expert evaluator for Bluetooth specification knowledge systems.
Your job is to score a system's answer against a reference answer using a strict rubric.
You must return valid JSON only — no explanation outside the JSON block.
Be strict: only mark a fact as correct if it explicitly matches the reference.
Do not reward plausible-sounding but unverifiable claims.
```

---

## User Prompt Template

```
## Question
{QUESTION}

## Reference Answer
{REFERENCE_ANSWER}

## Key Facts (must be present for full Completeness score)
{KEY_FACTS_LIST}

## Expected Citations
{EXPECTED_CITATIONS}

## System Answer to Evaluate
{SYSTEM_ANSWER}

---

Score the System Answer on these 5 dimensions. Return ONLY a JSON object.

Dimensions:
1. accuracy (0-3): Are all stated facts correct? Penalize any factual error.
2. completeness (0-3): What fraction of Key Facts appear in the answer? (≥90%=3, 60-89%=2, 30-59%=1, <30%=0)
3. citation (0-3): Is the spec version + section correctly cited? (version+section=3, version only=2, vague=1, none=0)
4. hallucination_penalty (0 to -3): Did the answer fabricate any facts not in the reference? (none=0, minor=-1, significant=-2, substantially fabricated=-3)
5. usability (0-2): Is the answer clearly structured and actionable for an engineer?

Also provide a one-sentence rationale for each dimension.

Return this exact JSON structure:
{
  "scores": {
    "accuracy": <int>,
    "completeness": <int>,
    "citation": <int>,
    "hallucination_penalty": <int>,
    "usability": <int>
  },
  "rationales": {
    "accuracy": "<one sentence>",
    "completeness": "<one sentence>",
    "citation": "<one sentence>",
    "hallucination_penalty": "<one sentence>",
    "usability": "<one sentence>"
  },
  "raw_total": <sum of all scores>,
  "key_facts_found": [<list of key facts that were present in the answer>],
  "key_facts_missing": [<list of key facts absent from the answer>]
}
```

---

## Example Invocation (Python)

```python
import anthropic
import json

client = anthropic.Anthropic()

SYSTEM_PROMPT = """You are an expert evaluator for Bluetooth specification knowledge systems.
Your job is to score a system's answer against a reference answer using a strict rubric.
You must return valid JSON only — no explanation outside the JSON block.
Be strict: only mark a fact as correct if it explicitly matches the reference.
Do not reward plausible-sounding but unverifiable claims."""

def evaluate_answer(question: dict, system_answer: str) -> dict:
    key_facts = "\n".join(f"- {f}" for f in question["key_facts"])
    citations = ", ".join(question["expected_citations"])

    user_prompt = f"""## Question
{question["question"]}

## Reference Answer
{question["reference_answer"]}

## Key Facts (must be present for full Completeness score)
{key_facts}

## Expected Citations
{citations}

## System Answer to Evaluate
{system_answer}

---

Score the System Answer on these 5 dimensions. Return ONLY a JSON object.

Dimensions:
1. accuracy (0-3): Are all stated facts correct? Penalize any factual error.
2. completeness (0-3): What fraction of Key Facts appear in the answer? (≥90%=3, 60-89%=2, 30-59%=1, <30%=0)
3. citation (0-3): Is the spec version + section correctly cited? (version+section=3, version only=2, vague=1, none=0)
4. hallucination_penalty (0 to -3): Did the answer fabricate any facts not in the reference? (none=0, minor=-1, significant=-2, substantially fabricated=-3)
5. usability (0-2): Is the answer clearly structured and actionable for an engineer?

Return this exact JSON structure:
{{
  "scores": {{
    "accuracy": <int>,
    "completeness": <int>,
    "citation": <int>,
    "hallucination_penalty": <int>,
    "usability": <int>
  }},
  "rationales": {{
    "accuracy": "<one sentence>",
    "completeness": "<one sentence>",
    "citation": "<one sentence>",
    "hallucination_penalty": "<one sentence>",
    "usability": "<one sentence>"
  }},
  "raw_total": <sum of all scores>,
  "key_facts_found": ["<fact>"],
  "key_facts_missing": ["<fact>"]
}}"""

    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_prompt}],
    )

    return json.loads(response.content[0].text)


DIFFICULTY_WEIGHTS = {
    "easy": 1.0,
    "medium": 1.5,
    "hard": 2.0,
    "expert": 2.5,
}

def run_evaluation(dataset: dict, system_answers: dict) -> dict:
    """
    dataset: loaded dataset.json
    system_answers: dict mapping question id -> answer string
                    e.g. {"Q001": "The minimum connection interval is ...", ...}
    Returns aggregated scores by category and overall.
    """
    results = []
    for q in dataset["questions"]:
        qid = q["id"]
        answer = system_answers.get(qid, "")
        scores = evaluate_answer(q, answer)
        weight = DIFFICULTY_WEIGHTS[q["difficulty"]]
        raw = scores["raw_total"]
        weighted = raw * weight
        max_weighted = 11 * weight  # max raw score is 11
        results.append({
            "id": qid,
            "category": q["category"],
            "difficulty": q["difficulty"],
            "weight": weight,
            "raw": raw,
            "weighted": weighted,
            "max_weighted": max_weighted,
            "detail": scores,
        })

    # Aggregate
    total_weighted = sum(r["weighted"] for r in results)
    total_max = sum(r["max_weighted"] for r in results)
    overall_pct = round(total_weighted / total_max * 100, 1)

    by_category = {}
    for r in results:
        cat = r["category"]
        by_category.setdefault(cat, {"weighted": 0, "max": 0, "count": 0})
        by_category[cat]["weighted"] += r["weighted"]
        by_category[cat]["max"] += r["max_weighted"]
        by_category[cat]["count"] += 1
    for cat in by_category:
        by_category[cat]["pct"] = round(
            by_category[cat]["weighted"] / by_category[cat]["max"] * 100, 1
        )

    return {
        "overall_pct": overall_pct,
        "by_category": by_category,
        "per_question": results,
    }
```

---

## Running a Full Comparison

```python
import json

with open("eval/dataset.json") as f:
    dataset = json.load(f)

# Collect answers from both systems for all 30 questions
rag_answers = collect_answers_from_rag(dataset["questions"])       # your implementation
wiki_answers = collect_answers_from_wiki(dataset["questions"])     # your implementation

rag_result  = run_evaluation(dataset, rag_answers)
wiki_result = run_evaluation(dataset, wiki_answers)

print(f"RAG overall:      {rag_result['overall_pct']}%")
print(f"LLM-Wiki overall: {wiki_result['overall_pct']}%")
print(f"Gap:              {wiki_result['overall_pct'] - rag_result['overall_pct']:+.1f} pts")

print("\nBy category:")
for cat in dataset["meta"]["categories"]:
    rag_pct  = rag_result["by_category"].get(cat, {}).get("pct", 0)
    wiki_pct = wiki_result["by_category"].get(cat, {}).get("pct", 0)
    print(f"  {cat:<30} RAG={rag_pct}%  Wiki={wiki_pct}%  Δ={wiki_pct-rag_pct:+.1f}")
```

---

## Expected Output Shape

```
RAG overall:      61.4%
LLM-Wiki overall: 83.7%
Gap:              +22.3 pts

By category:
  version_facts                  RAG=88.2%  Wiki=90.1%  Δ=+1.9
  feature_explanation            RAG=72.0%  Wiki=85.5%  Δ=+13.5
  version_comparison             RAG=55.3%  Wiki=87.2%  Δ=+31.9
  cross_version_reasoning        RAG=44.1%  Wiki=79.8%  Δ=+35.7
  implementation_hci             RAG=58.6%  Wiki=82.4%  Δ=+23.8
  edge_cases                     RAG=38.9%  Wiki=75.6%  Δ=+36.7
```

*(These are illustrative numbers — actual results will vary.)*

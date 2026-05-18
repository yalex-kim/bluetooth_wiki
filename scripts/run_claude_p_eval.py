"""Generate answers via `claude -p`, judge them, and produce an HTML report.

Usage:
    python3 scripts/run_claude_p_eval.py [--skip-answers] [--skip-judge]

Outputs:
    eval/results_claude_p.json   — raw scores per question
    eval/report_claude_p.html    — visual dashboard
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATASET_PATH = REPO / "eval" / "dataset.json"
RESULTS_PATH = REPO / "eval" / "results_claude_p.json"
WIKI_RESULTS_PATH = REPO / "eval" / "results_wiki.json"
REPORT_PATH = REPO / "eval" / "report.html"

JUDGE_MODEL = "claude-sonnet-4-6"

DIFFICULTY_WEIGHTS = {"easy": 1.0, "medium": 1.5, "hard": 2.0, "expert": 2.5}

JUDGE_SYSTEM = (
    "You are an expert evaluator for Bluetooth specification knowledge systems.\n"
    "Your job is to score a system's answer against a reference answer using a strict rubric.\n"
    "You must return valid JSON only — no explanation outside the JSON block.\n"
    "Be strict: only mark a fact as correct if it explicitly matches the reference.\n"
    "Do not reward plausible-sounding but unverifiable claims."
)

JUDGE_TEMPLATE = """\
## Question
{question}

## Reference Answer
{reference}

## Key Facts (must be present for full Completeness score)
{key_facts}

## Expected Citations
{expected_citations}

## System Answer to Evaluate
{system_answer}

---

Score the System Answer on these 5 dimensions. Return ONLY a JSON object.

Dimensions:
1. accuracy (0-3): Are all stated facts correct? Penalize any factual error.
2. completeness (0-3): What fraction of Key Facts appear in the answer? (>=90%=3, 60-89%=2, 30-59%=1, <30%=0)
3. citation (0-3): Is the spec version + section correctly cited? (version+section=3, version only=2, vague=1, none=0)
4. hallucination_penalty (0 to -3): Did the answer fabricate any facts not in the reference? (none=0, minor=-1, significant=-2, substantially fabricated=-3)
5. usability (0-2): Is the answer clearly structured and actionable for an engineer?

Return ONLY this exact JSON structure (no prose around it):
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
  "raw_total": <sum of all 5 scores including the negative hallucination penalty>,
  "key_facts_found": [<key facts that were present>],
  "key_facts_missing": [<key facts absent>]
}}"""


# ── helpers ───────────────────────────────────────────────────────────────────

def load_dataset() -> dict:
    return json.loads(DATASET_PATH.read_text(encoding="utf-8"))


def run_claude_p(question: str) -> str:
    """Run `claude -p <question>` and return stdout."""
    result = subprocess.run(
        ["claude", "-p", question],
        capture_output=True,
        text=True,
        timeout=120,
    )
    return result.stdout.strip()


def extract_json(text: str) -> dict:
    start = text.find("{")
    if start == -1:
        raise ValueError("No JSON object in judge response")
    depth = 0
    in_str = False
    esc = False
    for i in range(start, len(text)):
        ch = text[i]
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return json.loads(text[start: i + 1])
    raise ValueError("Unbalanced JSON in judge response")


def judge_answer(question: dict, system_answer: str) -> dict:
    """Judge via claude -p with system+user prompt concatenated."""
    user = JUDGE_TEMPLATE.format(
        question=question["question"],
        reference=question["reference_answer"],
        key_facts="\n".join(f"- {f}" for f in question["key_facts"]),
        expected_citations=", ".join(question["expected_citations"]),
        system_answer=system_answer,
    )
    full_prompt = JUDGE_SYSTEM + "\n\n" + user
    result = subprocess.run(
        ["claude", "-p", full_prompt],
        capture_output=True,
        text=True,
        timeout=120,
    )
    return extract_json(result.stdout)


# ── main pipeline ─────────────────────────────────────────────────────────────

def generate_answers(dataset: dict, existing: dict) -> dict:
    """Run claude -p for each question and return {qid: answer}. Saves after each answer."""
    answers = existing.copy()
    questions = dataset["questions"]
    total = len(questions)
    for i, q in enumerate(questions, 1):
        qid = q["id"]
        if qid in answers:
            print(f"  [{i:2}/{total}] {qid} — skipped (cached)")
            continue
        print(f"  [{i:2}/{total}] {qid} ({q['difficulty']}) — running claude -p …", end="", flush=True)
        t0 = time.perf_counter()
        try:
            ans = run_claude_p(q["question"])
        except subprocess.TimeoutExpired:
            ans = "(timeout)"
        elapsed = time.perf_counter() - t0
        answers[qid] = ans
        print(f" {elapsed:.1f}s ({len(ans)} chars)")
        # Save answers incrementally so a crash doesn't lose progress
        _save_answers(answers)
    return answers


def _save_answers(answers: dict) -> None:
    if RESULTS_PATH.exists():
        saved = json.loads(RESULTS_PATH.read_text(encoding="utf-8"))
    else:
        saved = {}
    saved["answers"] = answers
    RESULTS_PATH.write_text(json.dumps(saved, indent=2, ensure_ascii=False), encoding="utf-8")


def judge_all(dataset: dict, answers: dict, existing_scores: dict) -> list[dict]:
    """Judge all answers. Returns list of per-question result dicts."""
    questions = dataset["questions"]
    total = len(questions)
    results = []
    for i, q in enumerate(questions, 1):
        qid = q["id"]
        weight = DIFFICULTY_WEIGHTS[q["difficulty"]]
        if qid in existing_scores:
            r = existing_scores[qid]
            print(f"  [{i:2}/{total}] {qid} — skipped (cached) raw={r['raw_total']}")
            results.append(r)
            continue
        ans = answers.get(qid, "")
        print(f"  [{i:2}/{total}] {qid} — judging …", end="", flush=True)
        t0 = time.perf_counter()
        verdict = judge_answer(q, ans)
        elapsed = time.perf_counter() - t0
        s = verdict["scores"]
        hall = s.get("hallucination_penalty", s.get("hallucination", 0))
        s["hallucination_penalty"] = hall
        raw = s["accuracy"] + s["completeness"] + s["citation"] + hall + s["usability"]
        verdict["raw_total"] = raw
        result = {
            "id": qid,
            "category": q["category"],
            "difficulty": q["difficulty"],
            "weight": weight,
            "scores": s,
            "raw_total": raw,
            "weighted": round(raw * weight, 1),
            "max_weighted": 11 * weight,
            "rationales": verdict.get("rationales", {}),
            "key_facts_found": verdict.get("key_facts_found", []),
            "key_facts_missing": verdict.get("key_facts_missing", []),
            "answer": ans,
        }
        results.append(result)
        print(f" {elapsed:.1f}s  raw={raw}/11")
    return results


def aggregate(results: list[dict]) -> dict:
    total_w = sum(r["weighted"] for r in results)
    total_max = sum(r["max_weighted"] for r in results)
    overall_pct = round(total_w / total_max * 100, 1)

    by_cat: dict[str, dict] = {}
    for r in results:
        cat = r["category"]
        by_cat.setdefault(cat, {"weighted": 0.0, "max": 0.0, "count": 0, "questions": []})
        by_cat[cat]["weighted"] += r["weighted"]
        by_cat[cat]["max"] += r["max_weighted"]
        by_cat[cat]["count"] += 1
        by_cat[cat]["questions"].append(r["id"])
    for cat in by_cat:
        by_cat[cat]["pct"] = round(by_cat[cat]["weighted"] / by_cat[cat]["max"] * 100, 1)

    dim_sums: dict[str, float] = {"accuracy": 0, "completeness": 0, "citation": 0,
                                   "hallucination_penalty": 0, "usability": 0}
    for r in results:
        for d, v in r["scores"].items():
            dim_sums[d] = dim_sums.get(d, 0) + v
    n = len(results)
    dim_avgs = {d: round(v / n, 2) for d, v in dim_sums.items()}

    return {
        "overall_pct": overall_pct,
        "total_weighted": total_w,
        "total_max_weighted": total_max,
        "by_category": by_cat,
        "dimension_averages": dim_avgs,
    }


# ── HTML generation ───────────────────────────────────────────────────────────

def color_class(pct: float) -> str:
    if pct >= 95:
        return "c-perfect"
    if pct >= 80:
        return "c-good"
    if pct >= 60:
        return "c-ok"
    return "c-low"


def bar_class(pct: float) -> str:
    if pct >= 95:
        return "bg-perfect"
    if pct >= 80:
        return "bg-good"
    if pct >= 60:
        return "bg-ok"
    return "bg-low"


def score_pill(val: int, max_val: int = 3) -> str:
    css = {3: "sp-3", 2: "sp-2", 1: "sp-1", 0: "sp-0"}.get(val, "sp-n")
    return f'<span class="score-pill {css}">{val}</span>'


def diff_badge(d: str) -> str:
    return f'<span class="diff-badge diff-{d}">{d}</span>'


def category_label(cat: str) -> str:
    return {
        "version_facts": "Version Facts",
        "feature_explanation": "Feature Explanation",
        "version_comparison": "Version Comparison",
        "cross_version_reasoning": "Cross-Version Reasoning",
        "implementation_hci": "Implementation / HCI",
        "edge_cases": "Edge Cases",
    }.get(cat, cat)


def generate_html(
    claude_p_results: list[dict],
    claude_p_agg: dict,
    wiki_results: dict,
    dataset: dict,
    run_date: str,
) -> str:
    wp = claude_p_agg["overall_pct"]
    wiki_pct = wiki_results["meta"]["overall_pct"]

    # build quick lookup from wiki per-question
    wiki_pq = {r["id"]: r for r in wiki_results["per_question"]}
    cp_pq = {r["id"]: r for r in claude_p_results}

    # ── category rows ──────────────────────────────────────────────────────────
    cat_order = [
        ("version_facts", "Q001–Q007, Q031–Q032"),
        ("feature_explanation", "Q008–Q013, Q033–Q035"),
        ("version_comparison", "Q014–Q018, Q036–Q037"),
        ("cross_version_reasoning", "Q019–Q022"),
        ("implementation_hci", "Q023–Q026, Q038–Q040"),
        ("edge_cases", "Q027–Q030, Q041–Q042"),
    ]

    cat_rows = ""
    for cat, qrange in cat_order:
        cp_cat = claude_p_agg["by_category"].get(cat, {})
        wiki_cat = wiki_results["by_category"].get(cat, {})
        cp_pct = cp_cat.get("pct", 0)
        w_pct = wiki_cat.get("pct", 0)
        delta = round(w_pct - cp_pct, 1)
        delta_str = f"+{delta}" if delta >= 0 else str(delta)
        delta_color = "var(--green)" if delta > 0 else ("var(--red)" if delta < 0 else "var(--muted)")
        n = cp_cat.get("count", 0)
        diff_label = {"version_facts": "Easy ×1.0", "feature_explanation": "Medium ×1.5",
                      "version_comparison": "Medium ×1.5", "cross_version_reasoning": "Hard ×2.0",
                      "implementation_hci": "Hard ×2.0", "edge_cases": "Expert ×2.5"}.get(cat, "")
        cat_rows += f"""
      <div class="cat-row">
        <div class="cat-header">
          <span class="cat-name">{category_label(cat)} <span style="font-weight:400;color:var(--muted)">({qrange})</span></span>
          <span class="cat-scores">
            <span class="{color_class(cp_pct)}" style="margin-right:12px">claude -p: {cp_pct}%</span>
            <span class="{color_class(w_pct)}" style="margin-right:12px">Wiki: {w_pct}%</span>
            <span style="color:{delta_color};font-weight:700">Δ {delta_str}</span>
          </span>
        </div>
        <div style="display:grid;gap:4px;margin-bottom:6px">
          <div style="display:flex;align-items:center;gap:8px;font-size:11px;color:var(--muted)">
            <span style="width:70px">claude -p</span>
            <div class="bar-track" style="flex:1"><div class="bar-fill {bar_class(cp_pct)}" style="width:{cp_pct}%"></div></div>
            <span style="width:40px;text-align:right">{cp_pct}%</span>
          </div>
          <div style="display:flex;align-items:center;gap:8px;font-size:11px;color:var(--muted)">
            <span style="width:70px">Wiki</span>
            <div class="bar-track" style="flex:1"><div class="bar-fill bg-perfect" style="width:{w_pct}%"></div></div>
            <span style="width:40px;text-align:right">{w_pct}%</span>
          </div>
        </div>
        <div class="cat-meta"><span>{cp_cat.get('weighted',0):.1f} / {cp_cat.get('max',0):.1f} weighted (claude -p)</span><span>{n} questions</span><span>Difficulty: {diff_label}</span></div>
      </div>"""

    # ── question table rows ────────────────────────────────────────────────────
    prev_cat = None
    q_rows = ""
    for q in dataset["questions"]:
        qid = q["id"]
        cat = q["category"]
        if cat != prev_cat:
            prev_cat = cat
            q_rows += f'<tr class="q-section-label"><td colspan="10">{category_label(cat)}</td></tr>\n'
        cp = cp_pq.get(qid, {})
        wk = wiki_pq.get(qid, {})
        cs = cp.get("scores", {})
        ws = wk.get("scores", {})
        cp_raw = cp.get("raw_total", 0)
        wk_raw = wk.get("raw_total", 0)
        delta = wk_raw - cp_raw
        delta_color = "var(--green)" if delta > 0 else ("var(--red)" if delta < 0 else "var(--muted)")
        missing = cp.get("key_facts_missing", [])
        missing_str = "; ".join(missing[:2]) + ("…" if len(missing) > 2 else "") if missing else "—"
        q_rows += f"""<tr>
  <td class="q-id">{qid}</td>
  <td>{diff_badge(q['difficulty'])}</td>
  <td class="q-text">{q['question'][:90]}{'…' if len(q['question'])>90 else ''}</td>
  <td>{score_pill(cs.get('accuracy',0))}</td>
  <td>{score_pill(cs.get('completeness',0))}</td>
  <td>{score_pill(cs.get('citation',0))}</td>
  <td>{score_pill(cs.get('hallucination_penalty',0), 0)}</td>
  <td>{score_pill(cs.get('usability',0), 2)}</td>
  <td class="raw-total" style="color:{'var(--accent)' if cp_raw==11 else 'var(--yellow)' if cp_raw>=9 else 'var(--red)'}">{cp_raw}/11</td>
  <td style="color:{delta_color};font-weight:600;white-space:nowrap">wiki: {wk_raw}/11</td>
</tr>
<tr style="border-bottom:1px solid var(--border)">
  <td colspan="10" style="padding:2px 12px 8px;font-size:11px;color:var(--muted)">{missing_str if missing else '✓ all key facts covered'}</td>
</tr>
"""

    # ── dimension summary ──────────────────────────────────────────────────────
    dims = claude_p_agg.get("dimension_averages", {})
    wiki_dims = wiki_results.get("dimension_averages", {})

    def dim_card(label: str, key: str, max_v: float) -> str:
        v = dims.get(key, 0)
        wv = wiki_dims.get(key, {})
        if isinstance(wv, dict):
            wv = wv.get("avg", 0)
        pct = round(v / max_v * 100) if max_v else 0
        return f"""<div class="dim-card">
  <div class="dval {color_class(pct)}">{v:.2f}</div>
  <div class="dmax">/ {max_v:.0f} avg &nbsp;·&nbsp; wiki: {wv:.2f}</div>
  <div class="dlbl">{label}</div>
  <div class="dbar"><div class="dbar-fill {bar_class(pct)}" style="width:{pct}%"></div></div>
</div>"""

    dim_cards = (
        dim_card("Accuracy", "accuracy", 3)
        + dim_card("Completeness", "completeness", 3)
        + dim_card("Citation", "citation", 3)
        + dim_card("Hallucination", "hallucination_penalty", 0)
        + dim_card("Usability", "usability", 2)
    )

    # ── perfect / gap counts ──────────────────────────────────────────────────
    perfect = sum(1 for r in claude_p_results if r.get("raw_total", 0) == 11)
    hall_count = sum(1 for r in claude_p_results if r.get("scores", {}).get("hallucination_penalty", 0) < 0)

    # ── score circle dashoffset ───────────────────────────────────────────────
    circumference = 377
    dashoffset_cp = round(circumference - circumference * wp / 100, 1)
    dashoffset_wiki = round(circumference - circumference * wiki_pct / 100, 1)

    gap = round(wiki_pct - wp, 1)
    gap_str = f"+{gap}" if gap >= 0 else str(gap)

    if gap >= 20:
        gap_verdict = '<strong style="color:var(--green)">Strong case for LLM-Wiki:</strong> The pre-indexed wiki significantly outperforms the base model, especially on cross-version reasoning and edge cases where training knowledge alone is insufficient.'
    elif gap >= 10:
        gap_verdict = '<strong style="color:var(--yellow)">Moderate advantage:</strong> The wiki helps, especially for synthesis tasks.'
    elif gap >= 5:
        gap_verdict = '<strong style="color:var(--muted)">Marginal difference:</strong> Both systems perform similarly.'
    else:
        gap_verdict = "<strong style=\"color:var(--blue)\">Base model competitive:</strong> Claude's training knowledge covers most Bluetooth spec questions well."

    hall_color = "var(--red)" if hall_count else "var(--green)"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Bluetooth Eval — claude -p vs LLM-Wiki</title>
<style>
  :root {{
    --bg: #0f1117;
    --surface: #1a1d27;
    --surface2: #22263a;
    --border: #2e3250;
    --text: #e2e8f0;
    --muted: #8892b0;
    --accent: #64ffda;
    --blue: #7b8cde;
    --green: #4ade80;
    --yellow: #facc15;
    --orange: #fb923c;
    --red: #f87171;
    --purple: #c084fc;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ background: var(--bg); color: var(--text); font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; font-size: 14px; line-height: 1.6; }}
  a {{ color: var(--accent); text-decoration: none; }}

  .container {{ max-width: 1200px; margin: 0 auto; padding: 40px 24px; }}

  .header {{ margin-bottom: 40px; }}
  .header h1 {{ font-size: 26px; font-weight: 700; color: var(--text); margin-bottom: 4px; }}
  .header .meta {{ color: var(--muted); font-size: 13px; }}
  .header .meta span {{ margin-right: 20px; }}
  .badge {{ display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 600; background: rgba(100,255,218,0.1); color: var(--accent); border: 1px solid rgba(100,255,218,0.25); }}
  .badge-blue {{ background: rgba(123,140,222,0.1); color: var(--blue); border-color: rgba(123,140,222,0.25); }}

  .hero {{ display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 32px; }}
  .hero-box {{ background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 28px; }}
  .hero-box h3 {{ font-size: 13px; font-weight: 600; color: var(--muted); text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 20px; }}
  .score-row {{ display: flex; align-items: center; gap: 24px; }}
  .score-circle {{ position: relative; width: 120px; height: 120px; flex-shrink: 0; }}
  .score-circle svg {{ transform: rotate(-90deg); }}
  .score-circle .track {{ fill: none; stroke: var(--surface2); stroke-width: 10; }}
  .score-circle .fill  {{ fill: none; stroke-width: 10; stroke-linecap: round; stroke-dasharray: 377; transition: stroke-dashoffset 1s ease; }}
  .fill-cp {{ stroke: var(--blue); }}
  .fill-wiki {{ stroke: var(--accent); }}
  .score-center {{ position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%); text-align: center; }}
  .score-center .num {{ font-size: 28px; font-weight: 800; line-height: 1; }}
  .score-center .label {{ font-size: 10px; color: var(--muted); margin-top: 2px; }}
  .num-cp {{ color: var(--blue); }}
  .num-wiki {{ color: var(--accent); }}
  .stat-list {{ display: grid; gap: 8px; flex: 1; }}
  .stat-item {{ display: flex; justify-content: space-between; align-items: center; }}
  .stat-item .sk {{ font-size: 12px; color: var(--muted); }}
  .stat-item .sv {{ font-size: 13px; font-weight: 700; }}

  .gap-banner {{ background: var(--surface2); border: 1px solid var(--border); border-radius: 10px; padding: 20px 28px; margin-bottom: 32px; display: flex; align-items: center; justify-content: space-between; }}
  .gap-banner .gap-val {{ font-size: 36px; font-weight: 800; color: var(--green); }}
  .gap-banner .gap-label {{ font-size: 13px; color: var(--muted); margin-top: 2px; }}
  .gap-banner .gap-text {{ font-size: 13px; color: var(--text); max-width: 500px; }}

  .method-note {{ background: rgba(123,140,222,0.07); border: 1px solid rgba(123,140,222,0.2); border-radius: 8px; padding: 12px 16px; margin-bottom: 32px; font-size: 12px; color: var(--muted); }}
  .method-note strong {{ color: var(--blue); }}

  .section {{ margin-bottom: 32px; }}
  .section-title {{ font-size: 13px; font-weight: 700; color: var(--muted); text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 16px; display: flex; align-items: center; gap: 8px; }}
  .section-title::after {{ content: ''; flex: 1; height: 1px; background: var(--border); }}

  .cat-grid {{ display: grid; gap: 10px; }}
  .cat-row {{ background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 14px 18px; }}
  .cat-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; flex-wrap: wrap; gap: 6px; }}
  .cat-name {{ font-weight: 600; font-size: 13px; }}
  .cat-scores {{ font-size: 13px; font-weight: 600; }}
  .bar-track {{ height: 6px; background: var(--surface2); border-radius: 3px; overflow: hidden; }}
  .bar-fill  {{ height: 100%; border-radius: 3px; transition: width 0.8s ease; }}
  .cat-meta  {{ display: flex; gap: 16px; margin-top: 6px; font-size: 11px; color: var(--muted); flex-wrap: wrap; }}

  .c-perfect {{ color: var(--accent); }}
  .c-good    {{ color: var(--green); }}
  .c-ok      {{ color: var(--yellow); }}
  .c-low     {{ color: var(--red); }}
  .bg-perfect {{ background: var(--accent); }}
  .bg-good    {{ background: var(--green); }}
  .bg-ok      {{ background: var(--yellow); }}
  .bg-low     {{ background: var(--red); }}

  .dim-grid {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 12px; }}
  .dim-card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 16px; text-align: center; }}
  .dim-card .dval {{ font-size: 22px; font-weight: 700; }}
  .dim-card .dmax {{ font-size: 11px; color: var(--muted); }}
  .dim-card .dlbl {{ font-size: 11px; color: var(--muted); margin-top: 4px; }}
  .dim-card .dbar {{ margin-top: 8px; height: 4px; background: var(--surface2); border-radius: 2px; overflow: hidden; }}
  .dim-card .dbar-fill {{ height: 100%; border-radius: 2px; }}

  .table-wrap {{ background: var(--surface); border: 1px solid var(--border); border-radius: 8px; overflow: auto; }}
  .q-table {{ width: 100%; border-collapse: collapse; }}
  .q-table th {{ background: var(--surface2); color: var(--muted); font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; padding: 10px 12px; text-align: left; position: sticky; top: 0; }}
  .q-table td {{ padding: 8px 12px; border-bottom: 1px solid rgba(46,50,80,0.5); vertical-align: middle; }}
  .q-table tr:hover td {{ background: rgba(255,255,255,0.02); }}
  .q-id   {{ font-family: monospace; font-size: 12px; color: var(--muted); white-space: nowrap; }}
  .q-text {{ font-size: 12px; color: var(--text); max-width: 300px; }}
  .diff-badge {{ display: inline-block; padding: 1px 6px; border-radius: 3px; font-size: 10px; font-weight: 600; }}
  .diff-easy   {{ background: rgba(74,222,128,0.1); color: var(--green); }}
  .diff-medium {{ background: rgba(250,204,21,0.1); color: var(--yellow); }}
  .diff-hard   {{ background: rgba(251,146,60,0.1); color: var(--orange); }}
  .diff-expert {{ background: rgba(248,113,113,0.1); color: var(--red); }}
  .score-pill {{ display: inline-block; width: 30px; height: 20px; line-height: 20px; text-align: center; border-radius: 3px; font-size: 11px; font-weight: 700; }}
  .sp-3 {{ background: rgba(100,255,218,0.12); color: var(--accent); }}
  .sp-2 {{ background: rgba(250,204,21,0.12); color: var(--yellow); }}
  .sp-1 {{ background: rgba(248,113,113,0.12); color: var(--red); }}
  .sp-0 {{ background: rgba(248,113,113,0.2); color: var(--red); }}
  .sp-n {{ background: rgba(248,113,113,0.2); color: var(--red); }}
  .raw-total {{ font-weight: 700; font-size: 13px; }}
  .q-section-label td {{ background: var(--surface2); color: var(--muted); font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; padding: 6px 12px; }}

  .footer {{ margin-top: 48px; padding-top: 24px; border-top: 1px solid var(--border); color: var(--muted); font-size: 12px; display: flex; justify-content: space-between; }}
</style>
</head>
<body>
<div class="container">

  <div class="header">
    <h1>Bluetooth Spec Eval — <code>claude -p</code> vs LLM-Wiki</h1>
    <div class="meta">
      <span>📅 {run_date}</span>
      <span>📋 42 questions · 6 categories</span>
      <span>🤖 Judge: {JUDGE_MODEL}</span>
      <span class="badge badge-blue">claude -p (base model)</span>
      <span class="badge">LLM-Wiki v1.0</span>
    </div>
  </div>

  <div class="method-note">
    <strong>Methodology:</strong> <code>claude -p "&lt;question&gt;"</code> runs the base Claude model with no tools and no wiki access — answering from training knowledge only.
    The LLM-Wiki system uses a pre-indexed wiki of Bluetooth Core Spec pages (wiki/ directory) with RAG-like lookup.
    Both systems are judged by the same LLM-as-Judge rubric: Accuracy (0–3), Completeness (0–3), Citation (0–3), Hallucination Penalty (0 to –3), Usability (0–2).
    Difficulty weights: easy ×1.0, medium ×1.5, hard ×2.0, expert ×2.5. Max total: 770 weighted points.
  </div>

  <!-- Two-column hero -->
  <div class="hero">
    <div class="hero-box">
      <h3>claude -p (Base Model)</h3>
      <div class="score-row">
        <div class="score-circle">
          <svg width="120" height="120" viewBox="0 0 120 120">
            <circle class="track" cx="60" cy="60" r="50"/>
            <circle class="fill fill-cp" cx="60" cy="60" r="50" style="stroke-dashoffset:{dashoffset_cp}; stroke-dasharray:314"/>
          </svg>
          <div class="score-center">
            <div class="num num-cp">{wp}%</div>
            <div class="label">Overall</div>
          </div>
        </div>
        <div class="stat-list">
          <div class="stat-item"><span class="sk">Weighted score</span><span class="sv" style="color:var(--blue)">{claude_p_agg['total_weighted']:.1f} / {claude_p_agg['total_max_weighted']:.0f}</span></div>
          <div class="stat-item"><span class="sk">Perfect (11/11)</span><span class="sv">{perfect} / 42</span></div>
          <div class="stat-item"><span class="sk">Hallucinations</span><span class="sv" style="color:{hall_color}">{hall_count} questions</span></div>
          <div class="stat-item"><span class="sk">System</span><span class="sv" style="font-size:11px">claude -p (no wiki)</span></div>
        </div>
      </div>
    </div>

    <div class="hero-box">
      <h3>LLM-Wiki (wiki/ access)</h3>
      <div class="score-row">
        <div class="score-circle">
          <svg width="120" height="120" viewBox="0 0 120 120">
            <circle class="track" cx="60" cy="60" r="50"/>
            <circle class="fill fill-wiki" cx="60" cy="60" r="50" style="stroke-dashoffset:{dashoffset_wiki}; stroke-dasharray:314"/>
          </svg>
          <div class="score-center">
            <div class="num num-wiki">{wiki_pct}%</div>
            <div class="label">Overall</div>
          </div>
        </div>
        <div class="stat-list">
          <div class="stat-item"><span class="sk">Weighted score</span><span class="sv" style="color:var(--accent)">{wiki_results['meta']['total_weighted']:.1f} / {wiki_results['meta']['total_max_weighted']:.0f}</span></div>
          <div class="stat-item"><span class="sk">Perfect (11/11)</span><span class="sv">37 / 42</span></div>
          <div class="stat-item"><span class="sk">Hallucinations</span><span class="sv" style="color:var(--green)">0 questions</span></div>
          <div class="stat-item"><span class="sk">System</span><span class="sv" style="font-size:11px">wiki/ pages (pre-indexed)</span></div>
        </div>
      </div>
    </div>
  </div>

  <!-- Gap banner -->
  <div class="gap-banner">
    <div>
      <div class="gap-val">Wiki {gap_str}</div>
      <div class="gap-label">LLM-Wiki vs claude -p gap</div>
    </div>
    <div class="gap-text">
      {gap_verdict}
    </div>
  </div>

  <!-- Category scores -->
  <div class="section">
    <div class="section-title">Score by Category</div>
    <div class="cat-grid">
      {cat_rows}
    </div>
  </div>

  <!-- Dimension averages -->
  <div class="section">
    <div class="section-title">Dimension Averages — claude -p</div>
    <div class="dim-grid">
      {dim_cards}
    </div>
  </div>

  <!-- Per-question table -->
  <div class="section">
    <div class="section-title">Per-Question Results — claude -p</div>
    <div class="table-wrap">
      <table class="q-table">
        <thead>
          <tr>
            <th>QID</th><th>Level</th><th>Question</th>
            <th title="Accuracy">Acc</th><th title="Completeness">Cmp</th>
            <th title="Citation">Cit</th><th title="Hallucination">Hal</th>
            <th title="Usability">Use</th>
            <th>Raw</th><th>Wiki</th>
          </tr>
        </thead>
        <tbody>
          {q_rows}
        </tbody>
      </table>
    </div>
  </div>

  <div class="footer">
    <span>Generated {run_date} · judge: {JUDGE_MODEL}</span>
    <span>Bluetooth LLM-Wiki Evaluation Suite · 42 questions</span>
  </div>

</div>
</body>
</html>"""
    return html


# ── entry point ───────────────────────────────────────────────────────────────

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--skip-answers", action="store_true", help="Skip claude -p, load from JSON")
    p.add_argument("--skip-judge", action="store_true", help="Skip judging, use cached scores")
    args = p.parse_args()

    dataset = load_dataset()

    # Load or init results JSON
    if RESULTS_PATH.exists():
        saved = json.loads(RESULTS_PATH.read_text(encoding="utf-8"))
    else:
        saved = {"answers": {}, "per_question": []}

    saved_answers = saved.get("answers", {})
    saved_pq = {r["id"]: r for r in saved.get("per_question", [])}

    # Step 1: generate answers
    if not args.skip_answers:
        print("\n── Step 1: Generating answers with claude -p ──────────────────────────────")
        answers = generate_answers(dataset, saved_answers)
    else:
        print("\n── Step 1: Skipping claude -p (--skip-answers) ────────────────────────────")
        answers = saved_answers

    # Step 2: judge
    if not args.skip_judge:
        print("\n── Step 2: Judging answers ────────────────────────────────────────────────")
        per_question = judge_all(dataset, answers, saved_pq)
    else:
        print("\n── Step 2: Skipping judge (--skip-judge) ──────────────────────────────────")
        per_question = list(saved_pq.values())

    # Aggregate
    agg = aggregate(per_question)
    run_date = datetime.now().strftime("%Y-%m-%d")

    # Save results
    output = {
        "meta": {
            "system": "claude -p",
            "evaluator": JUDGE_MODEL,
            "date": run_date,
            "overall_pct": agg["overall_pct"],
            "total_weighted": agg["total_weighted"],
            "total_max_weighted": agg["total_max_weighted"],
        },
        "by_category": agg["by_category"],
        "dimension_averages": {
            d: {"avg": v, "max": (3.0 if d != "usability" else 2.0 if d != "hallucination_penalty" else 0.0)}
            for d, v in agg["dimension_averages"].items()
        },
        "answers": answers,
        "per_question": per_question,
    }
    RESULTS_PATH.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nSaved results → {RESULTS_PATH.relative_to(REPO)}")

    # Step 3: generate HTML report
    print("\n── Step 3: Generating HTML report ────────────────────────────────────────")
    wiki_results = json.loads(WIKI_RESULTS_PATH.read_text(encoding="utf-8"))
    html = generate_html(per_question, agg, wiki_results, dataset, run_date)
    REPORT_PATH.write_text(html, encoding="utf-8")
    print(f"Saved report → {REPORT_PATH.relative_to(REPO)}")

    # Summary
    wiki_pct = wiki_results["meta"]["overall_pct"]
    gap = round(wiki_pct - agg["overall_pct"], 1)
    print(f"\n{'═'*60}")
    print(f"  claude -p overall: {agg['overall_pct']}%  ({agg['total_weighted']:.1f} / {agg['total_max_weighted']:.0f})")
    print(f"  LLM-Wiki overall:  {wiki_pct}%  ({wiki_results['meta']['total_weighted']:.1f} / {wiki_results['meta']['total_max_weighted']:.0f})")
    print(f"  Gap (Wiki − claude -p): {gap:+.1f} pts")
    print(f"{'═'*60}\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

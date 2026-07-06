"""HTML rendering for the search-strategy comparison report.

Pure f-string templating (no Jinja2 — matches the repo's existing hand-built
report style), reusing eval/report.html's dark-theme CSS vocabulary.
Used by scripts/generate_search_report.py (CLI) and server/jobs.py.
"""

from __future__ import annotations

import html
from datetime import date

STRAT_COLORS = {"v0": "var(--muted)", "v1": "var(--blue)", "v2": "var(--accent)"}
STRAT_LABELS = {
    "v0": "v0 — naive substring",
    "v1": "v1 — ripgrep ranked",
    "v2": "v2 — hybrid + agentic",
}

CSS = """
  :root {
    --bg: #0f1117; --surface: #1a1d27; --surface2: #22263a; --border: #2e3250;
    --text: #e2e8f0; --muted: #8892b0; --accent: #64ffda; --blue: #7b8cde;
    --green: #4ade80; --yellow: #facc15; --orange: #fb923c; --red: #f87171; --purple: #c084fc;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { background: var(--bg); color: var(--text); font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; font-size: 14px; line-height: 1.6; }
  a { color: var(--accent); text-decoration: none; }
  .container { max-width: 1150px; margin: 0 auto; padding: 40px 24px; }
  .header { margin-bottom: 32px; }
  .header h1 { font-size: 26px; font-weight: 700; margin-bottom: 4px; }
  .header .meta { color: var(--muted); font-size: 13px; }
  .header .meta span { margin-right: 20px; }
  .section { margin-bottom: 32px; }
  .section-title { font-size: 13px; font-weight: 700; color: var(--muted); text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 16px; display: flex; align-items: center; gap: 8px; }
  .section-title::after { content: ''; flex: 1; height: 1px; background: var(--border); }
  .hero-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; }
  .hero-card { background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 24px; display: flex; gap: 20px; align-items: center; }
  .score-circle { position: relative; width: 110px; height: 110px; flex-shrink: 0; }
  .score-circle svg { transform: rotate(-90deg); }
  .score-circle .track { fill: none; stroke: var(--surface2); stroke-width: 9; }
  .score-circle .fill  { fill: none; stroke-width: 9; stroke-linecap: round; }
  .score-center { position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%); text-align: center; }
  .score-center .num { font-size: 24px; font-weight: 800; line-height: 1; }
  .score-center .label { font-size: 10px; color: var(--muted); margin-top: 2px; }
  .hero-side .sname { font-weight: 700; font-size: 14px; margin-bottom: 6px; }
  .hero-side .srow { font-size: 12px; color: var(--muted); }
  .hero-side .srow b { color: var(--text); font-weight: 600; }
  .tele-table { width: 100%; border-collapse: collapse; background: var(--surface); border: 1px solid var(--border); border-radius: 8px; overflow: hidden; }
  .tele-table th, .tele-table td { padding: 10px 14px; text-align: left; font-size: 12px; border-bottom: 1px solid var(--border); }
  .tele-table th { background: var(--surface2); color: var(--muted); font-size: 11px; text-transform: uppercase; letter-spacing: 0.05em; }
  .tele-table tr:last-child td { border-bottom: none; }
  .tele-table td.num { font-weight: 700; font-size: 13px; }
  .cat-grid { display: grid; gap: 10px; }
  .cat-row { background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 14px 18px; }
  .cat-name { font-weight: 600; font-size: 13px; margin-bottom: 8px; }
  .strat-line { display: grid; grid-template-columns: 150px 1fr 110px; gap: 12px; align-items: center; margin-bottom: 6px; }
  .strat-label { font-size: 11px; color: var(--muted); }
  .bar-track { height: 6px; background: var(--surface2); border-radius: 3px; overflow: hidden; }
  .bar-fill  { height: 100%; border-radius: 3px; }
  .strat-val { font-size: 12px; font-weight: 700; text-align: right; white-space: nowrap; }
  .delta { font-size: 11px; font-weight: 600; margin-left: 6px; }
  .delta.pos { color: var(--green); } .delta.neg { color: var(--red); } .delta.zero { color: var(--muted); }
  .table-wrap { background: var(--surface); border: 1px solid var(--border); border-radius: 8px; overflow: auto; }
  .q-table { width: 100%; border-collapse: collapse; }
  .q-table th { background: var(--surface2); color: var(--muted); font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; padding: 10px 12px; text-align: left; position: sticky; top: 0; }
  .q-table td { padding: 10px 12px; border-bottom: 1px solid var(--border); vertical-align: top; }
  .q-table tr:last-child td { border-bottom: none; }
  .q-table tr:hover td { background: rgba(255,255,255,0.02); }
  .q-id { font-family: monospace; font-size: 12px; color: var(--muted); white-space: nowrap; }
  .q-text { font-size: 12px; max-width: 320px; }
  .diff-badge { display: inline-block; padding: 1px 6px; border-radius: 3px; font-size: 10px; font-weight: 600; }
  .diff-easy   { background: rgba(74,222,128,0.1); color: var(--green); }
  .diff-medium { background: rgba(250,204,21,0.1); color: var(--yellow); }
  .diff-hard   { background: rgba(251,146,60,0.1); color: var(--orange); }
  .diff-expert { background: rgba(248,113,113,0.1); color: var(--red); }
  .score-pill { display: inline-block; min-width: 38px; height: 20px; line-height: 20px; text-align: center; border-radius: 3px; font-size: 11px; font-weight: 700; }
  .sp-hi { background: rgba(100,255,218,0.12); color: var(--accent); }
  .sp-mid { background: rgba(250,204,21,0.12); color: var(--yellow); }
  .sp-lo { background: rgba(248,113,113,0.15); color: var(--red); }
  .lat { font-size: 10px; color: var(--muted); display: block; margin-top: 2px; }
  .method-note { background: rgba(123,140,222,0.07); border: 1px solid rgba(123,140,222,0.2); border-radius: 8px; padding: 12px 16px; margin-bottom: 32px; font-size: 12px; color: var(--muted); }
  .method-note strong { color: var(--blue); }
  .footer { color: var(--muted); font-size: 12px; margin-top: 40px; border-top: 1px solid var(--border); padding-top: 16px; }
"""


def esc(s) -> str:
    return html.escape(str(s))


def _pill_class(raw: int) -> str:
    return "sp-hi" if raw >= 10 else ("sp-mid" if raw >= 7 else "sp-lo")


def _bar_class(pct: float) -> str:
    if pct >= 95:
        return "var(--accent)"
    if pct >= 85:
        return "var(--green)"
    if pct >= 70:
        return "var(--yellow)"
    return "var(--red)"


def _fmt(v, suffix="", dash="—"):
    return f"{v}{suffix}" if v is not None else dash


def hero_card(strategy: str, res: dict) -> str:
    m = res["meta"]
    t = res.get("telemetry", {})
    pct = m["overall_pct"]
    color = STRAT_COLORS.get(strategy, "var(--blue)")
    circumference = 314  # 2πr, r=50
    offset = circumference - circumference * pct / 100.0
    return f"""
    <div class="hero-card">
      <div class="score-circle">
        <svg width="110" height="110"><circle class="track" cx="55" cy="55" r="50"/>
        <circle class="fill" cx="55" cy="55" r="50" stroke="{color}" stroke-dasharray="{circumference}" stroke-dashoffset="{offset:.0f}"/></svg>
        <div class="score-center"><div class="num" style="color:{color}">{pct}%</div><div class="label">weighted</div></div>
      </div>
      <div class="hero-side">
        <div class="sname" style="color:{color}">{esc(STRAT_LABELS.get(strategy, strategy))}</div>
        <div class="srow">score <b>{m["total_weighted"]}/{m["total_max_weighted"]}</b></div>
        <div class="srow">questions <b>{m.get("num_questions", len(res.get("per_question", [])))}</b></div>
        <div class="srow">avg latency <b>{_fmt(t.get("avg_latency_sec"), "s")}</b></div>
        <div class="srow">total cost <b>{_fmt(t.get("total_cost_usd"), "", "n/a")}</b></div>
      </div>
    </div>"""


def telemetry_table(results: dict[str, dict]) -> str:
    rows = []
    for s, res in results.items():
        t = res.get("telemetry", {})
        color = STRAT_COLORS.get(s, "var(--blue)")
        rows.append(
            f'<tr><td style="color:{color};font-weight:700">{esc(s)}</td>'
            f'<td class="num">{_fmt(t.get("avg_latency_sec"), "s")}</td>'
            f'<td class="num">{_fmt(t.get("p50_latency_sec"), "s")}</td>'
            f'<td class="num">{_fmt(t.get("p95_latency_sec"), "s")}</td>'
            f'<td class="num">{_fmt(t.get("avg_cost_usd"), " $", "n/a")}</td>'
            f'<td class="num">{_fmt(t.get("total_cost_usd"), " $", "n/a")}</td>'
            f'<td class="num">{_fmt(t.get("avg_tool_calls"))}</td>'
            f'<td class="num">{_fmt(t.get("avg_num_turns"))}</td></tr>'
        )
    return f"""
    <table class="tele-table">
      <tr><th>strategy</th><th>avg latency</th><th>p50</th><th>p95</th><th>avg cost</th><th>total cost</th><th>avg tool calls</th><th>avg turns</th></tr>
      {''.join(rows)}
    </table>"""


def category_section(results: dict[str, dict]) -> str:
    strategies = list(results)
    base = strategies[0]
    cats: list[str] = []
    for res in results.values():
        for c in res.get("by_category", {}):
            if c not in cats:
                cats.append(c)
    rows = []
    for cat in cats:
        lines = []
        base_pct = results[base]["by_category"].get(cat, {}).get("pct")
        for s in strategies:
            entry = results[s]["by_category"].get(cat)
            if not entry:
                continue
            pct = entry["pct"]
            delta_html = ""
            if s != base and base_pct is not None:
                d = round(pct - base_pct, 1)
                cls = "pos" if d > 0 else ("neg" if d < 0 else "zero")
                delta_html = f'<span class="delta {cls}">{"+" if d > 0 else ""}{d}</span>'
            color = STRAT_COLORS.get(s, "var(--blue)")
            lines.append(f"""
        <div class="strat-line">
          <div class="strat-label" style="color:{color}">{esc(s)}</div>
          <div class="bar-track"><div class="bar-fill" style="width:{pct}%;background:{color}"></div></div>
          <div class="strat-val">{pct}%{delta_html}</div>
        </div>""")
        rows.append(f'<div class="cat-row"><div class="cat-name">{esc(cat.replace("_", " "))}</div>{"".join(lines)}</div>')
    return f'<div class="cat-grid">{"".join(rows)}</div>'


def question_table(results: dict[str, dict]) -> str:
    strategies = list(results)
    per_q: dict[str, dict[str, dict]] = {}
    q_info: dict[str, dict] = {}
    for s, res in results.items():
        for e in res.get("per_question", []):
            per_q.setdefault(e["id"], {})[s] = e
            q_info.setdefault(e["id"], e)
    head_cells = "".join(f"<th>{esc(s)}</th>" for s in strategies)
    rows = []
    for qid in sorted(per_q):
        info = q_info[qid]
        cells = []
        for s in strategies:
            e = per_q[qid].get(s)
            if e is None:
                cells.append("<td>—</td>")
                continue
            raw = e["raw_total"]
            lat = e.get("latency_sec")
            err = f' title="{esc(e["error"])}"' if e.get("error") else ""
            cells.append(
                f'<td{err}><span class="score-pill {_pill_class(raw)}">{raw}/11</span>'
                + (f'<span class="lat">{lat}s</span>' if lat is not None else "")
                + "</td>"
            )
        rows.append(
            f'<tr><td class="q-id">{esc(qid)}</td>'
            f'<td class="q-text">{esc(info["question"][:140])}</td>'
            f'<td><span class="diff-badge diff-{esc(info["difficulty"])}">{esc(info["difficulty"])}</span></td>'
            + "".join(cells)
            + "</tr>"
        )
    return f"""
    <div class="table-wrap"><table class="q-table">
      <tr><th>id</th><th>question</th><th>diff</th>{head_cells}</tr>
      {''.join(rows)}
    </table></div>"""


def build_html(results: dict[str, dict]) -> str:
    heroes = "".join(hero_card(s, r) for s, r in results.items())
    n_q = max((r["meta"].get("num_questions", 0) for r in results.values()), default=0)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Bluetooth Wiki — Search Strategy Comparison</title>
<style>{CSS}</style>
</head>
<body>
<div class="container">
  <div class="header">
    <h1>Search Strategy Comparison</h1>
    <div class="meta">
      <span>generated {date.today().isoformat()}</span>
      <span>{n_q} questions</span>
      <span>strategies: {', '.join(esc(s) for s in results)}</span>
    </div>
  </div>
  <div class="method-note">
    <strong>Method:</strong> each strategy answers the same eval questions through the same agent and system prompt;
    only the <code>search_wiki</code> retrieval backend differs. Scores are LLM-as-Judge (5 dimensions, difficulty-weighted
    per <a href="rubric.md">rubric.md</a>). Latency is wall-clock per <code>agent.ask()</code>. The point of comparison is the
    <em>quality ↔ time/cost trade-off</em>, not quality alone.
  </div>
  <div class="section"><div class="section-title">Overall</div><div class="hero-grid">{heroes}</div></div>
  <div class="section"><div class="section-title">Latency &amp; Cost</div>{telemetry_table(results)}</div>
  <div class="section"><div class="section-title">By Category (Δ vs {esc(next(iter(results)))})</div>{category_section(results)}</div>
  <div class="section"><div class="section-title">Per Question</div>{question_table(results)}</div>
  <div class="footer">
    Sources: {', '.join(f'<code>eval/results_search_{esc(s)}.json</code>' for s in results)} ·
    generated by <code>scripts/generate_search_report.py</code>
  </div>
</div>
</body>
</html>"""



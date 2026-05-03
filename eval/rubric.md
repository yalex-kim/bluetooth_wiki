# Evaluation Rubric: RAG vs LLM-Wiki

## Overview

Each of the 30 questions is scored across 5 dimensions. Scores are summed per question,
then aggregated by category and overall. The comparison is run on the **same 30 questions**
against both systems; all other variables (model, temperature, system prompt) are held constant.

---

## Scoring Dimensions

### 1. Factual Accuracy (0–3)

Is every claim in the answer correct relative to the Bluetooth spec?

| Score | Criteria |
|-------|----------|
| 3 | All stated facts are correct. No errors. |
| 2 | Mostly correct; one minor inaccuracy (wrong minor version, slightly off number). |
| 1 | Core answer is directionally right but contains at least one significant error. |
| 0 | Wrong answer, or no answer given. |

**Grader note**: Use `key_facts` in `dataset.json` as the checklist. A fact is "correct" only if it matches the reference answer — not if it sounds plausible.

---

### 2. Completeness (0–3)

Does the answer cover all the key facts listed in `key_facts`?

| Score | Criteria |
|-------|----------|
| 3 | Covers ≥ 90% of key facts. |
| 2 | Covers 60–89% of key facts. |
| 1 | Covers 30–59% of key facts. |
| 0 | Covers < 30% of key facts, or omits the central point entirely. |

---

### 3. Citation Quality (0–3)

Does the answer cite the correct spec version, volume, or section?

| Score | Criteria |
|-------|----------|
| 3 | Correct spec version + volume/part referenced (e.g. "Core 5.3, Vol 6, Part B"). |
| 2 | Correct spec version mentioned, no section detail. |
| 1 | Vague reference ("the BLE spec says…") or approximate version. |
| 0 | No citation, or wrong spec version cited. |

---

### 4. Hallucination Penalty (−3–0)

Did the answer introduce facts not in the spec or outright fabricate content?

| Score | Criteria |
|-------|----------|
| 0  | No hallucinated content. |
| −1 | One minor fabricated detail (fake HCI command name, wrong parameter range). |
| −2 | Multiple fabrications or one significant fabrication that would mislead a developer. |
| −3 | Answer is substantially fabricated. |

**Grader note**: This is a penalty, not a bonus. A perfectly accurate but incomplete answer scores 0 here.

---

### 5. Usability (0–2)

Is the answer structured, actionable, and easy for an engineer to apply?

| Score | Criteria |
|-------|----------|
| 2 | Clear structure. If implementation is asked, steps are in order. If conceptual, explanation flows logically. |
| 1 | Understandable but poorly organized, too verbose, or missing actionable detail. |
| 0 | Confusing, walls of text, or impossible to apply. |

---

## Question Difficulty Weights

| Difficulty | Weight | Categories |
|------------|--------|------------|
| Easy | 1.0× | `version_facts` |
| Medium | 1.5× | `feature_explanation`, `version_comparison` |
| Hard | 2.0× | `cross_version_reasoning`, `implementation_hci` |
| Expert | 2.5× | `edge_cases` |

**Raw max per question**: 3 + 3 + 3 + 0 + 2 = **11 points**
**Weighted max**: easy=11, medium=16.5, hard=22, expert=27.5

---

## Aggregate Score Calculation

```
Per-question score = (Accuracy + Completeness + Citation + Hallucination_Penalty + Usability) × Weight

System score = Σ(per-question scores) / Σ(max weighted scores) × 100
```

This gives a 0–100 score for each system. Compute this **per category** and **overall**.

---

## Category Breakdown

| Category | Questions | Max Weighted Score | Focus |
|----------|-----------|--------------------|-------|
| `version_facts` (easy) | Q001–Q007 | 77 | Factual recall |
| `feature_explanation` (medium) | Q008–Q013 | 99 | Conceptual depth |
| `version_comparison` (medium) | Q014–Q018 | 82.5 | Cross-doc synthesis |
| `cross_version_reasoning` (hard) | Q019–Q022 | 88 | Multi-hop reasoning |
| `implementation_hci` (hard) | Q023–Q026 | 88 | Procedural completeness |
| `edge_cases` (expert) | Q027–Q030 | 110 | Precision under ambiguity |

---

## Evaluation Process

### Option A — LLM-as-Judge (Fast)

Use the judge prompt in `judge_prompt.md`. Feed each (question, reference_answer, system_answer) triple to Claude. Collect JSON scores. Compute totals.

**Recommended model**: claude-opus-4-7 (most consistent grading).
**Expected time**: ~30 min for 30 × 2 = 60 answers.

### Option B — Human Evaluation (Ground Truth)

Two raters score each answer independently. Use average. Cohen's kappa > 0.7 = acceptable inter-rater agreement.

### Option C — Hybrid (Recommended for Production Decision)

1. LLM-as-Judge first pass on all 60 answers.
2. Human review on: any answer where |RAG score − Wiki score| ≥ 3 (contested cases).
3. Human review on all `edge_cases` category (Q027–Q030).

---

## Interpretation Guide

| Overall Score Gap (Wiki − RAG) | Recommendation |
|-------------------------------|----------------|
| ≥ 20 points | Strong case for LLM-Wiki migration |
| 10–19 points | Migrate; focus on the category with the largest gap |
| 5–9 points | Marginal benefit; consider hybrid (wiki for concepts, RAG for raw spec lookup) |
| < 5 points | No significant difference; prioritize other factors (cost, latency) |

**Watch for**: High RAG scores on `version_facts` (easy factual lookup) are expected — RAG does well here.
The key differentiator categories are `version_comparison`, `cross_version_reasoning`, and `edge_cases`.

---

## Scoresheet Template

Copy this per system per run:

```
System: [RAG | LLM-Wiki]
Model: 
Date:
Evaluator:

| QID  | Accuracy | Completeness | Citation | Hallucination | Usability | Raw | Weight | Weighted |
|------|----------|--------------|----------|---------------|-----------|-----|--------|----------|
| Q001 |          |              |          |               |           |     | 1.0    |          |
| Q002 |          |              |          |               |           |     | 1.0    |          |
...
| TOTAL|          |              |          |               |           |     |        |          |
```

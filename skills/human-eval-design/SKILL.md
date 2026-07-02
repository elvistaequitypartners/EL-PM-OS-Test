---
name: human-eval-design
description: Use this skill when the user asks to "design a human evaluation", "human eval process", "annotation guidelines", "how to set up human review of AI outputs", "how to get humans to evaluate AI quality", "build a labeling process", "create annotation criteria", or wants to set up a structured process for humans to evaluate AI output quality.
version: 2.0.0
---

# Human Eval Design

You are designing a human evaluation process for AI outputs — the gold standard for evaluating quality that LLM-as-judge systems are calibrated against. Human evals are slower and more expensive, but they're the source of ground truth for every other evaluation method.

Framework: Hamel Husain + Shreya Shankar (Building eval systems, 2025), annotation methodology best practices.

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for the AI feature being evaluated. Understand: what are the failure categories from error analysis? What is the principal domain expert's quality bar?

## Step 2 — When to Run Human Evals

Run human evals:
- **When bootstrapping:** Before LLM-as-judge, to create the calibration dataset
- **When investigating a regression:** A metric dropped — sample and manually review to understand why
- **Periodically (ongoing):** Random sample of 50–100 live outputs per week/month to catch drift
- **When launching a new model or prompt change:** Before and after to validate quality didn't regress

Do NOT run human evals:
- On every inference in production (too slow and expensive)
- Without clear annotation guidelines (produces unreliable data)

## Step 3 — Annotation Design

**Binary annotation (Recommended for most cases):**
Each evaluator sees one (input, output) pair and marks: Thumbs Up (Good) / Thumbs Down (Bad).
Add: one mandatory reason for "Bad" selections (required for the error analysis feedback loop).

Pros: Fast (< 30 seconds per annotation), high agreement, easy to aggregate.
Cons: No nuance — doesn't tell you HOW bad something is.

**Rubric annotation (Use when more granularity is needed):**
Each evaluator rates 3–5 criteria on a 1–5 scale.

Example rubric for a PRD-writing feature:
| Criterion | 1 (Poor) | 3 (Acceptable) | 5 (Excellent) |
|---|---|---|---|
| Problem clarity | Vague or missing | Present but imprecise | Sharp, specific, evidence-based |
| User story quality | Generic or feature-framed | Adequate | Demand-side, outcome-oriented |
| Acceptance criteria | Missing or not testable | Partially testable | All binary and independently testable |
| Success metrics | Output-oriented | Mixed | All outcome-oriented and measurable |

## Step 4 — Annotation Guidelines

Write clear, specific annotation guidelines. The most common source of low agreement is ambiguous guidelines.

**For each criterion, define:**
- What PASS looks like (with 1–2 examples)
- What FAIL looks like (with 1–2 examples)
- The edge case: what if the output is partially correct?
- What to do if you're unsure (escalate to the principal domain expert)

**Golden examples:** Before the actual annotation, provide 5–10 examples with the "correct" answer labeled. This calibrates the annotator to the quality bar before they start.

## Step 5 — Agreement and Reliability

**Inter-annotator agreement:** If using multiple annotators, measure: % of cases where both annotators agree.
- > 85% agreement: The guidelines are clear and the task is well-defined
- 70–85% agreement: Guidelines need clarification on the gray areas
- < 70% agreement: The task definition is unclear; redesign guidelines

**When to use one annotator vs. two:**
- Binary annotation: One annotator is fine for most cases. Two annotators + tiebreaker for high-stakes evals.
- Rubric annotation: Two annotators + reconciliation for all cases.

## Step 6 — Annotation Tooling

For different scales:

**Under 200 annotations/week:** Google Sheets or Notion database. Simple, free, easy to set up.

**200–2,000 annotations/week:** Label Studio (free, open source) or Argilla. More structure, better workflows.

**2,000+ annotations/week:** Scale AI, Labelbox, or similar professional annotation platforms.

## Step 7 — Feedback Loop

The annotation process is only valuable if it feeds back into improvement:

1. Annotators flag Bad outputs
2. Bad outputs are clustered by failure category (error analysis)
3. Most common failures become new eval test cases
4. Eval suite is updated to catch those failures automatically
5. Model/prompt is updated to fix the failures
6. Annotation sample confirms the fix didn't create new failures

This is the continuous improvement flywheel.

## Step 8 — Output

Produce:
- Annotation interface design (fields, criteria, format)
- Annotation guidelines document (per-criterion definitions with examples)
- Golden examples set (5–10 labeled examples for calibration)
- Agreement measurement plan
- Sampling strategy: how many outputs to review per week and how to select them (random vs. targeted)

---
name: eval-suite-design
description: Use this skill when the user asks to "design an eval suite", "build evals for my AI feature", "create an evaluation framework", "how do I evaluate my AI", "what evals should I run", "build an eval system", or wants to create a systematic evaluation framework for an AI-powered product feature. Typically run after error-analysis has identified the failure categories to prioritize.
version: 2.0.0
---

# Eval Suite Design

You are designing an evaluation suite for an AI product feature — a systematic set of tests that catches real failure modes before they reach users. The goal is a suite that the team actually runs and acts on, not one that gets ignored.

Framework: Hamel Husain + Shreya Shankar (Building eval systems, 2025), Aman Khan (Beyond vibe checks, 2025).

Key principle: "Evals quietly decide whether your AI product thrives or dies. The ability to write great evals is rapidly becoming the defining skill for AI PMs in 2025 and beyond." — Aman Khan, Lenny's Newsletter (2025)

## Step 1 — Load Context

Read the error analysis output (from the error-analysis skill or user input) to understand which failure categories to target. Read `memory/personal/${USER}.md` for the AI feature context.

## Step 2 — Three Types of Evals

For each failure category, select the appropriate eval type:

**Type 1 — Code-based evals (deterministic):**
Best for: Failures with objectively correct / incorrect answers. Format compliance. Structural checks.
Examples:
- Output contains required sections (assert "## Problem" in output)
- Output is within length bounds (assert len(output) < 2000)
- Output is valid JSON (try parse; fail if exception)
- Required fields are non-empty (assert output.get('metric') is not None)
Pros: Fast, cheap, perfectly reliable
Cons: Only works for objective correctness — can't evaluate quality

**Type 2 — Human evals:**
Best for: Subjective quality, domain-specific correctness, complex reasoning, new failure categories being discovered.
Format: Annotators see (input, output) pairs and rate: Thumbs up / Thumbs down, or score on a rubric (1–5).
Pros: Highest accuracy; catches nuanced failures
Cons: Slow, expensive, can't scale; requires clear annotation guidelines
Use for: Calibration, sampling for quality assurance, training LLM-as-judge

**Type 3 — LLM-as-judge:**
Best for: Subjective quality at scale; failures that require reasoning to detect; when human evals are too slow.
Structure: A separate LLM (usually a stronger model) reviews (input, output) pairs and provides a judgment.
Pros: Scalable; can evaluate complex quality; can explain its reasoning
Cons: Not perfectly reliable; needs calibration against human evals; can be biased

## Step 3 — Eval Design Per Failure Category

For each top failure category (from error analysis):

**Name:** [Failure category name]
**Eval type:** [Code-based / Human / LLM-as-judge]
**What to test:** [Specific aspect of the output being evaluated]
**Test cases needed:** [How many? Where do they come from?]
**Pass/fail criteria:** [What counts as pass? What counts as fail?]
**Automation plan:** [When does this eval run — on every PR? Daily? Weekly?]

## Step 4 — LLM-as-Judge Prompt Design

If using LLM-as-judge, write the judge prompt following best practices:

```
You are evaluating an AI assistant's response for [failure type].

**Input to the AI assistant:**
{input}

**AI assistant's response:**
{response}

**Evaluation criteria:**
[Criterion 1]: [Clear definition of what good looks like]
[Criterion 2]: [Clear definition of what good looks like]

**Scoring:**
- PASS: The response [specific pass condition]
- FAIL: The response [specific fail condition]

**Your output:**
First, briefly explain your reasoning (1–2 sentences).
Then output: PASS or FAIL
```

Key principles for judge prompts:
- Binary outputs (PASS/FAIL) are more reliable than numeric scores
- Include examples of PASS and FAIL in the prompt when possible
- The judge should explain its reasoning before giving the verdict (chain-of-thought)
- Calibrate the judge against 50+ human annotations before trusting it

## Step 5 — The Principal Domain Expert Model

From Hamel Husain: designate one "benevolent dictator" for quality — one person whose judgment defines what PASS/FAIL means for subjective evals. This prevents annotation conflicts and anchors the LLM-as-judge calibration.

This person:
- Reviews 50–100 human annotation cases to establish the quality bar
- Resolves disagreements between annotators
- Periodically reviews LLM-as-judge outputs to catch drift

## Step 6 — Eval Suite Structure

Design the full suite as three layers:

**Layer 1 — Pre-commit (fast):** Code-based evals only. Run on every code change. Must complete in < 60 seconds. Catches format and structural failures.

**Layer 2 — Pre-deploy (medium):** Code-based + LLM-as-judge on a representative sample. Run before any deployment. Should complete in < 10 minutes.

**Layer 3 — Production monitoring (ongoing):** LLM-as-judge on a sample of live outputs + human eval on flagged outputs. Run continuously or weekly.

## Step 7 — Output

Produce:
- Eval suite design (one eval design per failure category)
- LLM-as-judge prompt(s) for subjective failure categories
- Three-layer eval structure with run frequency and completion time targets
- Minimum viable suite: which 3 evals to implement first to get 80% of the value?
- Measurement plan: how will you know if the evals are improving product quality over time?

---
name: llm-as-judge
description: Use this skill when the user asks to "set up LLM as a judge", "write an LLM judge prompt", "automate quality evaluation", "use Claude to evaluate outputs", "build an automated eval", "LLM-based evaluation", or wants to create a scalable automated evaluation system where one LLM grades the outputs of another LLM.
version: 2.0.0
---

# LLM-as-Judge Setup

You are setting up an LLM-as-judge evaluation system — a scalable way to automatically evaluate AI output quality by using a stronger or specialized LLM to grade the outputs of the product's AI.

Framework: Hamel Husain + Shreya Shankar (Building eval systems, 2025), Anthropic's evaluation methodology.

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for the AI feature being evaluated. Read the error analysis output if available to understand the failure categories to target.

## Step 2 — When to Use LLM-as-Judge

Use LLM-as-judge when:
- Human evaluation is the gold standard but too slow or expensive to run at scale
- The failure mode requires reasoning to detect (not just structural checking)
- You need to evaluate thousands of outputs on a regular cadence
- You've calibrated the judge against human annotations and trust it

Do NOT use LLM-as-judge when:
- You haven't calibrated it against human evals first (calibration is mandatory)
- The task has an objectively correct answer (use code-based evals instead)
- The failure mode is one the judge model is known to be bad at (e.g., detecting subtle factual errors in specialized domains)

## Step 3 — Judge Architecture Options

**Option A — Binary (Recommended for most cases):**
Judge outputs PASS or FAIL with a brief explanation. Simple, reliable, easy to aggregate.

**Option B — Rubric (Use when more granularity is needed):**
Judge scores each of 3–5 criteria on a 1–5 scale. Good for quality tracking over time.

**Option C — Comparative (Use when evaluating prompt variants):**
Judge sees two outputs side-by-side and picks the better one. Best for A/B testing prompt changes.

**Option D — Error detection (Use when targeting specific failure categories):**
Judge specifically looks for a known failure type (e.g., "does this output contain any unsupported factual claims?").

## Step 4 — Judge Prompt Template

Structure every judge prompt with these sections:

```markdown
# Evaluation Task

You are evaluating the quality of an AI assistant's response. Your role is to act as an expert reviewer and provide an objective assessment.

## Context
[Brief description of what the AI assistant is supposed to do]

## What you're evaluating for
[Specific quality criteria — be precise about what PASS and FAIL mean]

## The evaluation

**User input:**
{{input}}

**AI assistant's response:**
{{output}}

## Instructions
1. Analyze the response against the criteria above
2. Write your reasoning in 2–3 sentences
3. State your verdict: PASS or FAIL

## Output format
Reasoning: [Your 2–3 sentence analysis]
Verdict: [PASS or FAIL]
```

## Step 5 — Calibration Protocol

Before deploying LLM-as-judge in production, calibrate it:

1. Collect 100 (input, output) pairs
2. Have the principal domain expert (or 2 human annotators) label each: PASS or FAIL
3. Run the judge on the same 100 pairs
4. Calculate agreement rate: (matching judgments) / 100
5. Target: > 85% agreement with human labels

If agreement is < 85%:
- Add more examples to the judge prompt
- Tighten or clarify the evaluation criteria
- Try a different model (claude-opus-4-6 is more accurate as a judge for complex quality)
- Split one rubric criterion into two more specific criteria

## Step 6 — Avoiding Common Judge Failures

**Position bias:** Judge tends to prefer responses in a certain format or length. Fix: randomize the order of criteria in the prompt and run the same evaluation multiple times.

**Verbosity bias:** Judge rates longer responses as better even when they're not. Fix: explicitly state in the prompt "Length is not a quality signal. Evaluate based on [specific criteria]."

**Self-evaluation bias:** An LLM tends to give high ratings to outputs that look like its own generation style. Fix: use a different model as judge than the model being evaluated.

**Instruction following:** If the judge doesn't follow the output format, extract the verdict with a regex or second parsing step.

## Step 7 — Integration Pattern

Provide a Python pseudocode template for integrating LLM-as-judge into the evaluation pipeline:

```python
import anthropic

def evaluate_output(user_input: str, ai_output: str, judge_prompt: str) -> dict:
    client = anthropic.Anthropic()

    judge_input = judge_prompt.replace("{{input}}", user_input).replace("{{output}}", ai_output)

    response = client.messages.create(
        model="claude-opus-4-6",  # Use strongest model as judge
        max_tokens=500,
        messages=[{"role": "user", "content": judge_input}]
    )

    verdict_text = response.content[0].text
    verdict = "PASS" if "Verdict: PASS" in verdict_text else "FAIL"

    return {"verdict": verdict, "reasoning": verdict_text, "input": user_input, "output": ai_output}

# Run on a sample
results = [evaluate_output(inp, out, JUDGE_PROMPT) for inp, out in test_cases]
pass_rate = sum(1 for r in results if r["verdict"] == "PASS") / len(results)
print(f"Pass rate: {pass_rate:.1%}")
```

## Step 8 — Output

Produce:
- Judge prompt (ready to use, adapted to the user's failure category)
- Calibration protocol with target agreement threshold
- Integration pseudocode
- One week calibration plan: collect 100 cases → human label → compare → iterate

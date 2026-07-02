---
name: regression-testing
description: Use this skill when the user asks to "prevent regressions in AI quality", "regression testing for AI", "how do I know if a prompt change broke something", "before/after evaluation for model changes", "catch quality regressions", or wants to set up a process that catches when a model update, prompt change, or system change has degraded AI output quality compared to before.
version: 2.0.0
---

# AI Regression Testing

You are setting up a regression testing framework for an AI feature — a systematic process that catches quality degradations caused by model changes, prompt changes, or data/context changes before they reach users.

Framework: Hamel Husain + Shreya Shankar (Building eval systems, 2025), software testing principles applied to AI.

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for the AI feature being protected. Read the eval suite design if available — regression tests are a subset of the broader eval suite, focused on the specific failure modes the team has already identified and fixed.

## Step 2 — What Triggers a Regression?

AI regressions can be caused by:
- **Model updates:** The underlying LLM changes (e.g., Claude version update)
- **Prompt changes:** The system prompt or few-shot examples are modified
- **Context changes:** The data passed to the model (retrieved documents, user context) changes
- **Tool/API changes:** External tools the model calls change their behavior
- **Distribution shift:** The types of inputs coming from users have changed over time

The regression test suite should catch all of these, not just obvious changes.

## Step 3 — Building the Regression Test Set

The regression test set is a curated collection of (input, expected behavior) pairs. "Expected behavior" means the output should PASS a specific eval.

**Sources for the test set:**
1. **Past failures that were fixed:** If you fixed a failure in v1.0, add a test that would have caught it. This prevents it from recurring silently.
2. **Edge cases from error analysis:** The failure categories identified in error analysis become test cases.
3. **Representative happy path examples:** The most common, important use cases should have at least one test each.
4. **Boundary cases:** Inputs that are at the edge of the system's capability or scope.

**Size guidance:**
- Minimum viable: 20–30 carefully chosen test cases (covers major failure categories)
- Good: 50–100 test cases (covers failure categories + representative happy paths)
- Comprehensive: 200+ test cases (needed for high-stakes AI features)

## Step 4 — Regression Test Execution

**When to run:**
- On every PR that changes the system prompt, model version, or retrieval pipeline
- On every scheduled model update (when the underlying model is upgraded)
- Weekly (to catch silent regressions from distribution shift)

**Pass/fail definition:**
The test suite passes if: (1) every individual test case passes its specific eval, AND (2) the aggregate pass rate doesn't drop by more than [threshold]% from the baseline.

Set the threshold based on the feature's criticality:
- Core feature: < 2% regression acceptable
- Secondary feature: < 5% regression acceptable
- Experimental feature: < 10% regression acceptable

## Step 5 — Regression Report Structure

When a regression is detected, produce a report:

**What changed:** Which eval(s) failed? What does the failure pattern look like?

**Affected input types:** Are regressions concentrated on certain types of inputs (short inputs, specific user segments, specific task types)?

**Severity:** How many test cases failed? What's the regression % vs. baseline?

**Root cause hypothesis:** What change (model, prompt, context) most likely caused this?

**Rollback recommendation:** Should the change be reverted immediately, or is this a degradation that can be fixed forward?

**Fix plan:** If fixing forward, what changes to the prompt or system would address the regression?

## Step 6 — CI/CD Integration

Connect regression tests to the deployment pipeline:

```python
# Pseudocode: regression gate in deployment pipeline
def run_regression_gate(eval_suite, test_cases, baseline_pass_rate, threshold=0.02):
    results = [run_eval(test_case, eval_suite) for test_case in test_cases]
    current_pass_rate = sum(1 for r in results if r.passed) / len(results)
    regression = baseline_pass_rate - current_pass_rate

    if regression > threshold:
        raise DeploymentBlockedError(
            f"Regression detected: {regression:.1%} quality drop vs. baseline. "
            f"Blocking deployment. Review failing cases: {[r for r in results if not r.passed]}"
        )

    return {"pass_rate": current_pass_rate, "regression": regression, "status": "PASS"}
```

## Step 7 — Regression Triage Process

When a regression is flagged:

1. Identify which test cases failed (which failure categories?)
2. Compare failing outputs to the passing outputs from before the change
3. Determine root cause: is this a prompt issue, model issue, or retrieval issue?
4. Decide: revert (fastest) or fix forward (if the cause is known and the fix is simple)
5. After fixing, run the full regression suite before deploying
6. Update the test set: add the new failing cases as permanent regression tests

## Step 8 — Output

Produce:
- Regression test set design (how many cases, which failure categories to cover, sources)
- Pass/fail thresholds and regression % tolerances
- Deployment gate integration plan
- Regression triage process (who does what when a regression is caught)
- The first 10 regression test cases to implement (highest-priority failures from error analysis)

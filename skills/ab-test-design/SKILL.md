---
name: ab-test-design
description: Use this skill when the user asks to "design an A/B test", "how should I test this", "experiment design", "how do I run an experiment", "test this feature", "set up a split test", "how many users do I need", "statistical significance", "how do I know if this test worked", or wants to design a rigorous experiment to test a product hypothesis.
version: 2.0.0
---

# A/B Test Design

You are helping the user design a rigorous A/B test — one that produces trustworthy, actionable results rather than ambiguous data. Most A/B tests in practice are designed poorly and lead to incorrect conclusions. The goal is to fix that.

Framework: Statistical testing principles, Lenny Rachitsky's experimentation guide, Ronny Kohavi (Trustworthy Online Controlled Experiments).

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for product stage (pre-PMF products usually shouldn't be running A/B tests — qualitative research is more efficient) and analytics tool. Read `context/company/analytics-baseline.md` for baseline metrics needed for sample size calculation.

**Pre-PMF warning:** If the product is pre-PMF, flag: "A/B testing works best when you have enough traffic to detect effects and when the product direction is relatively stable. At this stage, qualitative user research often gives you more signal faster. Still want to proceed?"

## Step 2 — Test Design Elements

For a well-designed A/B test, define each element:

**Hypothesis:**
"If we [change], then [metric] will [increase/decrease] by [amount] because [reason]."
- The hypothesis must be falsifiable (there must be a result that would prove it wrong)
- The "because" is important — it forces you to think about the mechanism, not just the correlation

**Primary metric (what the test will be judged on):**
- Must be the metric the feature is designed to move
- Must be measurable within the test window
- Must be sensitive enough to detect realistic effect sizes

**Guardrail metrics (what must not get worse):**
- Core business metrics that should be protected even if the primary metric improves
- Example: even if the new onboarding increases activation, it shouldn't tank 7-day retention

**Control vs. treatment:**
- Control = current experience (baseline)
- Treatment = new experience being tested
- One change at a time — if multiple changes are made, it's impossible to know which caused the effect

## Step 3 — Sample Size Calculation

Calculate the required sample size before starting the test:

**Inputs needed:**
- Baseline conversion rate for the primary metric (from `analytics-baseline.md` or user input)
- Minimum detectable effect (MDE): the smallest improvement worth caring about
- Statistical power: 80% is standard (means 80% chance of detecting a real effect)
- Significance level: 5% (p < 0.05) is standard (5% chance of a false positive)

**Rule of thumb:** To detect a 10% relative improvement with 80% power, you typically need ~1,600 users per variant. For a 5% relative improvement, you need ~6,400 per variant.

If the user doesn't have an analytics tool that does this automatically, provide the calculation: use the approximate formula or direct them to an online calculator.

**Duration estimation:** Users needed ÷ daily traffic to the tested area = test duration in days. Flag if this exceeds 4 weeks — tests longer than 4 weeks are at high risk of confounders.

## Step 4 — Test Validity Checks

Before launching, verify:
- **No leakage:** Users in control shouldn't be able to see the treatment experience
- **Consistent assignment:** A user should always see the same variant
- **SRM check planned:** Sample Ratio Mismatch (if the control and treatment don't have equal traffic, something's wrong)
- **Novelty effect consideration:** New UI elements get extra attention initially — plan for this in the analysis window

## Step 5 — Analysis Plan

Define before launch:
- How long will the test run? (Set end date — don't peek and stop early)
- Who is the final decision-maker?
- What p-value counts as significant? (0.05 unless there's a reason otherwise)
- What happens if the test is inconclusive? (No change, run longer, redesign?)
- What happens if the treatment wins by exactly the MDE? (Ship, or run follow-up test?)

## Step 6 — Output

Produce:
- Hypothesis (falsifiable, with mechanism)
- Test design summary (control, treatment, primary metric, guardrails)
- Sample size requirement and estimated test duration
- Validity checklist
- Analysis plan
- One thing that could invalidate this test if not controlled for

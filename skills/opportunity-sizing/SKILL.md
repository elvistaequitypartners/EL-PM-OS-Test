---
name: opportunity-sizing
description: Use this skill when the user asks to "size this opportunity", "how big is this problem", "opportunity sizing", "how many users are affected", "estimate the impact", "what's the ROI", "is this worth building", "how do I prioritize this against other opportunities", or wants to quantify the potential value of solving a specific problem. Do NOT use this skill for full market sizing (TAM/SAM/SOM) — use the market-users/tam-sizing skill for that.
version: 2.0.0
---

# Opportunity Sizing

You are helping the user size a specific product opportunity — not the total addressable market, but the realistic impact of solving a specific user problem within the current product context.

Framework: Lenny Rachitsky's opportunity sizing model, OST opportunity scoring, RICE framework.

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for product stage, user base size, and current metrics. Read `context/company/analytics-baseline.md` for baseline metrics to anchor estimates. Read `context/product/roadmap.md` for prioritization context.

## Step 2 — Define the Opportunity Precisely

Before sizing, ensure the opportunity is precisely framed:
- Which user segment is affected?
- What specific struggle or unmet need are we sizing?
- What would users do differently if this problem were solved?

Vague opportunities can't be sized accurately. Help the user tighten the definition if needed.

## Step 3 — Size the Affected Population

Estimate: how many users currently experience this problem?

Work through:
1. **Total user base:** From memory or analytics baseline
2. **Segment filter:** What % of users are in the affected segment?
3. **Frequency filter:** Of those users, what % encounter this problem regularly (weekly or more)?
4. **Severity filter:** Of those, what % are meaningfully blocked vs. mildly annoyed?

**Affected users = Total base × Segment % × Frequency % × Severity %**

If exact numbers aren't available, use ranges: low / mid / high estimate.

## Step 4 — Estimate the Impact Per User

For affected users, estimate what solving the problem is worth:

**Retention impact:** Would solving this meaningfully reduce churn? If the product's 30-day retention is X%, what would it be if this problem were gone? Translate to: users retained × average lifetime value.

**Engagement impact:** Would solving this increase feature adoption or session frequency? Translate to: additional sessions × conversion rate.

**Acquisition impact:** Would solving this reduce a key friction point in activation or onboarding? Translate to: improvement in activation rate × new users/month.

**Revenue impact (if applicable):** Would solving this unlock a new pricing tier or reduce downgrade pressure?

## Step 5 — RICE Score

Calculate a RICE score for prioritization:

- **Reach:** How many users per quarter are affected? (Use Step 3 estimate)
- **Impact:** How much does it move the key metric per user? (1 = minimal, 3 = moderate, 9 = massive)
- **Confidence:** How confident are you in the Reach and Impact estimates? (20% = guess, 80% = validated)
- **Effort:** How many person-weeks to build and ship?

**RICE = (Reach × Impact × Confidence) / Effort**

## Step 6 — Output

Present:
- Sizing estimate: low / mid / high range of affected users
- Impact estimate: what metric moves and by how much (with confidence level)
- RICE score and how it compares to other known roadmap items (if any are in memory)
- Recommendation: is this large enough to prioritize? What would make it larger or smaller?
- Key sizing assumption: what number, if wrong, would most change this analysis?

Note the difference between the opportunity size (how big the problem is) and the solution potential (how much of the problem your specific solution can actually solve).

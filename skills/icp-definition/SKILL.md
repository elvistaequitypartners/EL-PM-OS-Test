---
name: icp-definition
description: Use this skill when the user asks to "define our ICP", "ideal customer profile", "who is our best customer", "who should we target", "which customers should we focus on", "who buys fastest", "who gets the most value", "find our ICP", or wants to identify the specific type of customer most likely to buy, succeed, and expand.
version: 2.0.0
---

# ICP Definition — Ideal Customer Profile

You are helping the user define their Ideal Customer Profile — the specific type of customer who gets the most value, converts fastest, expands most, and churns least. ICP is not about who you want to sell to — it's about who is naturally drawn to you and succeeds with you.

Framework: April Dunford (beachhead ICP), Lenny Rachitsky (B2B GTM guide), JTBD demand-side thinking.

Key principle: The ICP is discovered, not invented. Look at your best existing customers to find it.

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for product stage, business model, existing customer context. Read `context/product/personas.md` for existing persona definitions.

## Step 2 — Analyze Best Existing Customers (if applicable)

If the product has existing customers, start with the best ones:

**Define "best":** Customers who: (1) pay the most or expand fastest, (2) churn least, (3) see the fastest time to value, (4) refer others, (5) give the best product feedback.

For the top 10–20 "best" customers, look for patterns:
- **Firmographics:** Industry, company size, geography, funding stage, team size
- **Role of buyer:** Who initiated the purchase? Who was the champion? Who signed?
- **Trigger:** What happened before they bought? What changed that made them look?
- **Outcome:** What result did they achieve? How do they describe success?
- **Time to value:** How quickly did they activate? How quickly did they see ROI?

## Step 3 — ICP Dimensions

For each dimension, identify the sweet spot (not the full range — the narrow band where your best customers concentrate):

**Industry / Vertical:** Which industries get the most value? Are there industries where value is structural (e.g., compliance requirements make our product essential)?

**Company size:** Where is the sweet spot? (Size affects: budget, decision-making speed, sophistication, need for integration)

**Stage:** Series A? Bootstrapped? Enterprise? Each has different buying behavior, budget cycles, and value drivers.

**Geographic:** Any concentration? Regulatory environment that makes value higher in some regions?

**Team characteristics:** Which team composition makes the product work best? (e.g., "companies with at least 1 PM and at least 5 engineers")

**Trigger event:** What must have happened recently for a company to be ready to buy? (Job change, funding round, reorg, new competitive pressure, hitting a growth stage)

**Tech stack:** What other tools do ICP customers use that signal readiness? (e.g., "uses Linear or Jira" = our integration adds immediate value)

## Step 4 — ICP Profile

Write the ICP profile:

**Company-level ICP:**
- Industry: [Specific vertical(s)]
- Size: [Employee range or ARR range]
- Stage: [Funding stage or growth stage]
- Geography: [If relevant]
- Tech stack signals: [What tools indicate readiness]
- Trigger event: [What must have recently happened]

**Contact-level ICP (the champion and buyer):**
- Champion role: [Who gets value and advocates internally]
- Buyer role: [Who has budget authority — may be different from champion]
- Champion pain: [What the champion is struggling with that our product solves]
- Buyer motivation: [What the buyer cares about — ROI, risk reduction, team capability]

## Step 5 — Anti-ICP

Define who is NOT a good fit:
- Which segment looks similar but churns fast?
- Which segment buys but takes too much support?
- Which segment takes too long to close?

This is as important as the ICP — it saves sales and CS time, and prevents the product from drifting toward the wrong segment.

## Step 6 — ICP Scoring Criteria

For use in sales and marketing qualification, create an ICP score:

| Criterion | Weight | Scoring |
|---|---|---|
| [Key ICP dimension 1] | [%] | Yes = full points; No = 0 |
| [Key ICP dimension 2] | [%] | Yes = full points; Partial = half |
| Trigger event present | [%] | Yes = full points; No = 0 |
| Champion identified | [%] | Yes = full points; No = 0 |

Total score ≥ 75% = strong ICP fit; 50–75% = marginal; < 50% = poor fit

## Step 7 — Output

Produce:
- ICP profile (company-level + contact-level)
- Anti-ICP profile
- ICP scoring criteria for sales qualification
- Top 3 signals that quickly identify an ICP customer in the field
- Offer to update `context/product/personas.md` and `memory/personal/${USER}.md` with ICP findings

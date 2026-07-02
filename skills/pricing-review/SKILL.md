---
name: pricing-review
description: Use this skill when the user asks to "review our pricing", "help me think through pricing", "should we change our price", "pricing strategy", "how should we price this", "pricing tiers", "is our pricing right", "freemium vs. paid", or wants to evaluate or design their product's pricing model.
version: 2.0.0
---

# Pricing Review

You are helping the user evaluate or redesign their pricing model. Pricing is strategy made visible — it signals positioning, affects who buys, and determines who stays.

Framework: Lenny Rachitsky (AI feature monetization data), Palle Broe (How should you monetize your AI features), Patrick Campbell (value-based pricing), April Dunford (positioning-informed pricing).

Key insight from Palle Broe's analysis of 44 tech incumbents: 59% bundle AI features in existing packages; 23% offer as an add-on; 18% build standalone AI products. For products with clear customer value and high variable costs, direct monetization is best.

## Step 1 — Load Context

Read `memory/user-profile.md` for product stage, business model, and current bets. Read `context/company/competitors.md` for competitive pricing context.

## Step 2 — Pricing Model Selection

Evaluate which model fits:

**Flat subscription:** Simple, predictable revenue; good when value doesn't vary much by usage.
Best for: Tools used at a consistent rate; B2C or SMB.

**Usage-based / metered:** Price scales with value delivered; aligns costs with revenue.
Best for: AI-powered features with significant per-use costs (API calls, compute); enterprise customers with variable volume.

**Tier-based (Good/Better/Best):** Multiple tiers; works well when value delivered varies significantly by customer segment.
Best for: When you have distinct ICP segments with different willingness to pay and different feature needs.

**Freemium:** Free tier drives adoption; paid tier captures value for power users.
Best for: When the free tier has a real viral or word-of-mouth effect; when converting 2–5% of free users to paid is sufficient.

**Per-seat:** Simple, scales with team size.
Best for: Collaboration tools; B2B where value scales with the number of users.

## Step 3 — Value Metric Identification

The value metric is what you charge for — the thing that scales as customers get more value.

Good value metrics:
- Are easy for customers to understand
- Scale as customer value scales (power users pay more)
- Are easy for you to track and enforce

Poor value metrics:
- Don't connect to value (e.g., charging per API call when users care about the quality of outputs)
- Create friction that reduces adoption (e.g., per-seat pricing for a tool that needs wide adoption to work)
- Are gamed by customers (e.g., sharing one account)

## Step 4 — Willingness to Pay Analysis

Estimate willingness to pay for the ICP:

**Van Westendorp price sensitivity meter:**
Ask (or infer from context):
- At what price is the product too cheap? (Makes them doubt quality)
- At what price is it a great deal?
- At what price is it starting to feel expensive but worth it?
- At what price is it too expensive?

The acceptable price range is between "too cheap" and "too expensive" responses.

**Competitive anchoring:**
What do alternatives cost? How does our product's value compare? If we're 10x more valuable, we shouldn't be 10x more expensive — but we shouldn't be the same price as an inferior alternative.

## Step 5 — Freemium Assessment

If evaluating freemium:

**The freemium test:** Is the free tier genuinely useful enough to drive adoption, but limited enough to justify upgrading?

Common freemium mistakes:
- Too generous: users get everything they need for free and never upgrade
- Too restrictive: users can't see enough value to know they should upgrade
- Wrong limit: the limit is on the wrong dimension (limiting features vs. limiting usage vs. limiting output quality)

**For PM Operating System specifically** (as a reference model):
- Free: 20 core skills, 2 commands, no memory persistence → shows quality, creates need to upgrade for memory
- Solo: Full skill library, all 4 commands, full memory layer → the natural upgrade when the user wants memory to persist
- Pro: All MCP connectors, proactive check-ins, gossip mode → for power users who want the full experience

## Step 6 — Output

Produce:
- Pricing model recommendation with rationale
- Value metric identification
- Tier design (if applicable) with what's in each tier and why
- Price point recommendations with willingness to pay rationale
- Competitive pricing context
- One pricing assumption to validate: "We're assuming [X] — here's how to test it"

---
name: ai-feature-monetization
description: Use this skill when the user asks specifically about "how to monetize AI features", "should AI be a separate tier", "pricing for AI capabilities", "how to charge for AI", "AI add-on vs. bundle", "AI feature pricing strategy", or is adding AI capabilities to an existing product and wants to decide how to monetize them. This is a specialized version of pricing-review focused on AI feature economics.
version: 2.0.0
---

# AI Feature Monetization

You are helping the user decide how to monetize AI features specifically — a distinct challenge from general pricing because AI features have meaningful variable costs (API inference) and often deliver value in a way that's hard to measure per-use.

Framework: Palle Broe (How should you monetize your AI features, Lenny's Newsletter 2024 — analysis of 44 tech incumbents), Lenny Rachitsky (AI monetization patterns).

Key data from Palle Broe: Of 44 leading tech incumbents:
- **59% bundle** AI features in existing packages — no separate charge
- **23% offer as an add-on** — separate AI tier or add-on price
- **18% build standalone AI products** — separate product entirely

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for product stage, business model, and existing pricing. Read `context/company/competitors.md` for competitive pricing context.

## Step 2 — The Three Monetization Models

**Model 1 — Bundle (59% of incumbents):**
AI features are included in existing plans. No separate pricing.

When to use:
- AI feature is a product improvement, not a new product (enhances existing value rather than creating a new use case)
- The marginal cost of AI inference is low relative to subscription revenue
- Bundling protects against competitive unbundling (competitor offers AI for free)
- User acquisition and retention value of "AI included" outweighs direct monetization

Risk: If AI inference costs are high and usage is uncapped, you lose money on high-usage customers.
Mitigation: Soft limits or fair use policies on AI feature usage.

**Model 2 — Add-on (23% of incumbents):**
AI features are in a separate tier or add-on price point.

When to use:
- AI feature is genuinely new value, not just a product improvement
- There's a clear segment willing to pay more specifically for AI
- AI inference costs are significant and variable
- You need to signal that AI is premium (price communicates value)

Risk: Adds friction to adoption; users have to actively decide to pay for AI.
Mitigation: Free trial of AI features; show clear ROI before paywall.

**Model 3 — Standalone (18% of incumbents):**
AI is a separate product with its own pricing.

When to use:
- AI capability is a genuinely different product that serves a different (or expanded) use case
- The AI product can be sold to users who don't use the core product
- You want to build a separate go-to-market motion

Risk: Splits focus; dilutes brand; harder to sell.
When it works: When the AI product has clear standalone value (like PM Operating System — it's a plugin that adds genuine PM capability, not just an AI wrapper on an existing feature).

## Step 3 — Variable Cost Analysis

For AI-powered features, calculate the cost structure:

**Cost per session / per use:**
- Average input tokens per request × input token cost
- Average output tokens per request × output token cost
- Tool calls / retrieval costs if applicable

**At scale:**
- Estimated AI cost per active user per month
- What % of subscription revenue does this represent?

**Threshold analysis:**
- At current pricing, how many AI uses per month can a customer make before they're unprofitable?
- Is a fair use policy (e.g., "X AI requests per month") needed to protect margins?

## Step 4 — Decision Framework

Use this decision tree:

1. Is the AI feature a product improvement (enhances existing use case) or new value (entirely new use case)?
   - Improvement → lean toward Bundle
   - New value → consider Add-on or Standalone

2. Is the marginal cost per user per month < 10% of their subscription revenue?
   - Yes → Bundle is financially sustainable
   - No → Add-on or usage-based pricing needed

3. Is there a clear segment willing to pay more specifically for AI?
   - Yes → Add-on or premium tier
   - No → Bundle (treat as competitive necessity)

4. Is the AI product compelling enough to stand alone without the core product?
   - Yes → consider Standalone
   - No → Bundle or Add-on

## Step 5 — Output

Produce:
- Recommendation (Bundle / Add-on / Standalone) with rationale
- Variable cost estimate (cost per active user per month at current model tier)
- Margin analysis (at what usage level does the current pricing become unprofitable?)
- Competitive context (what are competitors doing? Is "AI included" becoming table stakes?)
- Implementation recommendation: if Add-on, what's the upgrade trigger? If Bundle, what's the fair use policy?

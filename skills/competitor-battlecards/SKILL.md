---
name: competitor-battlecards
description: Use this skill when the user asks for "competitor battlecards", "battlecard for [competitor]", "how do we beat [competitor]", "how do we handle objections about [competitor]", "competitive win/loss", "sales competitive guide", "how should sales talk about competitors", or needs a structured competitive comparison for sales, customer success, or internal strategy purposes.
version: 2.0.0
---

# Competitor Battlecards

You are creating competitive battlecards — structured one-page guides that help sales, customer success, and the product team understand specific competitors and articulate our differentiators confidently.

Frameworks: April Dunford (Obviously Awesome — positioning against alternatives), Hamilton Helmer (7 Powers), Lenny Rachitsky (competitive differentiation).

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for product context and current bets. Read `context/company/competitors.md` if it exists — use as a starting point. If WebSearch is available, research the specified competitor.

## Step 2 — Research the Competitor

For each competitor, gather:

Using WebSearch if available:
- Product offering and positioning
- Pricing (public if available)
- Recent changes, launches, or news
- Customer reviews (G2, Capterra, Product Hunt, Reddit, App Store)
- Target segment
- Key strengths based on reviews
- Key weaknesses based on reviews

## Step 3 — Battlecard Structure

For each competitor, produce a one-page battlecard:

---

**[Competitor Name] Battlecard**

**Who they are:** [One sentence description — what they build and who they serve]
**Best for:** [The customer profile they're ideal for — be honest]
**Price:** [If public]
**Key differentiators:** [Their 3 strongest genuine advantages]

**Where we win:**
| Dimension | Us | [Competitor] | Why We Win |
|---|---|---|---|
| [Dimension 1] | [Our capability] | [Their capability] | [Honest differentiator] |
| [Dimension 2] | [Our capability] | [Their capability] | [Honest differentiator] |
| [Dimension 3] | [Our capability] | [Their capability] | [Honest differentiator] |

**Where they win:**
(Be honest — your team needs to know where competitors are stronger to have credible conversations)
- [Area 1]: They are better at [X] for [Y type of customer]
- [Area 2]: They are better at [X] for [Y type of customer]

**When we lose and why:**
- [Loss scenario 1]: We tend to lose when the prospect [situation]. Handle by: [approach]
- [Loss scenario 2]: We tend to lose when the prospect [situation]. Handle by: [approach]

**Common objections and responses:**

*"[Competitor] has more integrations"*
> "[Honest, confident response that acknowledges the point and reframes toward our strength]"

*"[Competitor] is cheaper"*
> "[Response]"

*"[Competitor] is more established"*
> "[Response]"

**Trap to avoid:**
[The one thing to never say when this competitor comes up — often a claim we can't back up or a dismissal that makes us look defensive]

**How to qualify:**
Ask: "[Question that helps determine whether this prospect is better served by us or by [Competitor]"

---

## Step 4 — Competitive Response Principles

Add a section of general principles for competitive conversations:

1. **Lead with the customer's problem, not our features.** Ask: "What's most important to you?" before positioning.
2. **Acknowledge genuine competitor strengths.** Dismissing them loses credibility. "They're strong at X, and if X is your priority, they might be the right choice. Here's what we're strong at..."
3. **Use specifics.** "We have better memory" is weak. "We maintain context across sessions so you never re-brief — here's what that looks like..." is strong.
4. **Know when to walk away.** If a prospect's primary need is X and a competitor genuinely does X better, say so. Referrals come back.

## Step 5 — Output

Produce battlecard(s) for each competitor specified. Offer to:
- Save to `context/company/competitors.md`
- Save each card to `outputs/battlecard-[competitor]-[date].md`

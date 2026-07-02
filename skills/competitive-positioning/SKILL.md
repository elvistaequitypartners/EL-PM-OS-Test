---
name: competitive-positioning
description: Use this skill when the user asks for "competitive analysis", "who are our competitors", "competitive landscape", "how do we compare to X", "competitive positioning", "how do we differentiate", "what's our competitive advantage", "are we differentiated", or wants to understand the competitive context and define how to win against alternatives. Also use this skill when preparing for a board meeting or investor conversation that includes competitive positioning.
version: 2.0.0
---

# Competitive Positioning

You are helping the user understand the competitive landscape and define a defensible position — one that makes winning sustainable, not just situational.

Frameworks: Hamilton Helmer (7 Powers), April Dunford (Obviously Awesome — 5-component positioning), Lenny Rachitsky (differentiation guide, citing Michael Porter).

Key principle from Lenny/Porter: "Competing to be unique is ultimately more sustainable than competing to be the best." — Lenny Rachitsky, Differentiating Your Product (2022)

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for product stage and current bets. Read `context/company/competitors.md` if it exists. If not, proceed to research.

## Step 2 — Map the Competitive Landscape

Identify competitors across three types:

**Direct competitors:** Products that solve the same problem for the same user segment with a similar approach

**Indirect competitors:** Products that solve the same problem differently, or a different problem that our users also have

**Status quo:** What users do today if they don't use any of the above — could be spreadsheets, manual processes, hiring someone, or doing without

The competitive set should be the user's competitive set, not the investor's. Ask: "What would a user try if they decided not to use our product?" That's the true competitive landscape.

If WebSearch access is available, run parallel research:
- Search "[product category] competitors [year]" — find who else is in this space
- Search "[top competitor] reviews" — find what users love and hate about alternatives
- Search "[product category] market" — find recent funding, launches, or announcements

## Step 3 — Competitive Comparison Matrix

For each competitor, capture:
- Primary strength (what they do best)
- Primary weakness (what users complain about)
- Target user segment (is it the same as ours or different?)
- Pricing model
- Key differentiator

Build a comparison table. Identify: where is there white space? Where does every competitor have the same weakness?

## Step 4 — 7 Powers Analysis (Hamilton Helmer)

Evaluate which of Helmer's 7 durable competitive moats apply to the current product:

1. **Scale economies:** Does our cost per unit decrease as we grow? (Applies mainly to infrastructure-heavy products)
2. **Network effects:** Does the product get better as more users join? (Direct: each user adds value for all others; Indirect: more supply attracts more demand)
3. **Switching costs:** Is it painful for users to leave once they've invested in the product? (Data, integrations, workflow embedment, team training)
4. **Branding:** Do we command trust and a price premium that competitors can't easily replicate?
5. **Cornered resource:** Do we have exclusive access to a talent, data, or partnership that competitors can't get?
6. **Counter-positioning:** Do we have a business model that established competitors can't adopt without hurting themselves?
7. **Process power:** Do we have accumulated know-how and processes that create compounding advantages over time?

Rate each power: Strong / Emerging / Absent / Opportunity to build.

## Step 5 — Dunford Positioning (5 Components)

Apply April Dunford's 5-component positioning framework:

1. **Competitive alternatives:** What does the user do if they don't choose us?
2. **Unique attributes:** What do we do that no alternative does?
3. **Value those attributes enable:** What can users accomplish because of those unique attributes?
4. **Who cares most:** Which user segment gets the most value from those attributes?
5. **Market category:** What is the simplest frame for the category we operate in that makes our value obvious?

Use this to produce a positioning statement:
"For [target segment] who [struggle], [product name] is the [market category] that [unique value]. Unlike [alternatives], we [unique differentiator]."

## Step 6 — Output

Produce:
- Competitive landscape overview (who the real competitors are and why)
- Comparison matrix (strengths/weaknesses per competitor)
- 7 Powers assessment (which moats are strong, emerging, absent)
- Dunford positioning statement
- Top 3 recommendations: what to emphasize in positioning, what to build to strengthen moats, what competitive threats to monitor

Offer to save the competitive landscape to `context/company/competitors.md`.

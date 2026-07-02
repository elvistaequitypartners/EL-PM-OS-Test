---
description: Run a competitive intelligence analysis — landscape mapping, battlecards, 7 Powers moat comparison, positioning gaps, and monitoring plan
argument-hint: <competitor name, market category, or "full landscape">
allowed-tools: [Read, Write, Glob, WebSearch, Agent]
---

# /competitive-intel

You are a senior PM partner conducting competitive intelligence. This chains: landscape mapping → competitor deep-dives → battlecard generation → moat comparison → positioning gap analysis. The goal is actionable competitive insight, not a generic feature comparison matrix.

Frameworks: Hamilton Helmer (7 Powers), April Dunford (Obviously Awesome), Michael Porter (competing to be unique, not best), Lenny Rachitsky (differentiation guide).

## Input

The user has invoked this command with: `$ARGUMENTS`

- If a specific competitor name: deep-dive on that competitor
- If a market category: map the full landscape
- If "full landscape": comprehensive competitive analysis
- If empty: ask "Which competitor or market category do you want to analyze?"

## Step 1 — Load Memory & Context

Read in parallel:
- `memory/user-profile.md` — product context, current positioning, known competitors
- `context/company/competitors.md` (if it exists — previous analysis)
- `context/company/mission.md` (if it exists)
- `context/product/personas.md` (fallback: `context/product/personas-template.md`)

### No-Context Fallback

If `memory/user-profile.md` doesn't exist or has no competitive context, competitive intel is one of the best commands to run cold — WebSearch provides the context. Ask:

1. "What does your product do?" (one sentence — needed to identify the competitive set)
2. "Who do you think your main competitors are, if any?"

If the user isn't sure about competitors, that's fine — use WebSearch to discover them. After completing, offer: "Want me to save this competitive landscape to your PM Operating System memory so it's available for future strategy reviews?"

## Step 2 — Landscape Mapping

Identify competitors across three types:

**Direct:** Same problem, same user, similar approach
**Indirect:** Same problem, different approach — or different problem, same user
**Status quo:** What users do with no product (spreadsheets, manual process, hiring someone, doing nothing)

The status quo is often the real competitor. Ask: "What would users try if they decided not to use our product?"

Use WebSearch to research (run in parallel):
- "[product category] competitors [year]"
- "[top competitor] reviews" — what users love and hate
- "[product category] market" — recent funding, launches, acquisitions

## Step 3 — Competitor Deep-Dives

For each key competitor (top 3–5), research and capture:

| Dimension | Details |
|---|---|
| **Product** | Core offering, key features, recent launches |
| **Target user** | Who they serve, ICP overlap with us |
| **Positioning** | How they describe themselves, market category |
| **Pricing** | Model, tiers, how it compares to us |
| **Strengths** | What users love (from reviews, social proof) |
| **Weaknesses** | What users complain about (from reviews, support forums) |
| **Traction signals** | Funding, team size, growth signals, recent hires |
| **Threat level** | High / Medium / Low — to our specific product |

## Step 4 — Battlecard Generation

For each key competitor, produce a sales/positioning battlecard:

```
═══════════════════════════════════════
BATTLECARD: [Competitor Name]
═══════════════════════════════════════

THEY SAY: [Their positioning — how they describe themselves]
WE SAY:   [Our counter-positioning — how we differentiate]

THEIR STRENGTHS (acknowledge honestly):
• [Strength 1 — and how we address it]
• [Strength 2 — and how we address it]

THEIR WEAKNESSES (where we win):
• [Weakness 1 — and what we do instead]
• [Weakness 2 — and what we do instead]

WHEN THEY WIN: [Scenarios where they're the better choice]
WHEN WE WIN:   [Scenarios where we're the better choice]

LANDMINE QUESTIONS (questions to ask prospects that expose their weaknesses):
• [Question 1]
• [Question 2]
• [Question 3]

OBJECTION HANDLING:
"But [competitor] has [feature]..."
→ [Response — reframe around value, not features]
═══════════════════════════════════════
```

## Step 5 — 7 Powers Moat Comparison

Compare moat strength across competitors:

| Power | Us | Competitor A | Competitor B | Competitor C |
|---|---|---|---|---|
| Scale economies | [S/E/A] | [S/E/A] | [S/E/A] | [S/E/A] |
| Network effects | [S/E/A] | [S/E/A] | [S/E/A] | [S/E/A] |
| Switching costs | [S/E/A] | [S/E/A] | [S/E/A] | [S/E/A] |
| Branding | [S/E/A] | [S/E/A] | [S/E/A] | [S/E/A] |
| Cornered resource | [S/E/A] | [S/E/A] | [S/E/A] | [S/E/A] |
| Counter-positioning | [S/E/A] | [S/E/A] | [S/E/A] | [S/E/A] |
| Process power | [S/E/A] | [S/E/A] | [S/E/A] | [S/E/A] |

S = Strong, E = Emerging, A = Absent

Identify: where do competitors have moats we don't? Where do we have moats they can't easily replicate?

## Step 6 — Positioning Gap Analysis

Map the competitive landscape on key dimensions:

Identify 2–3 dimensions that matter most to users (not features — outcomes). Plot where each competitor sits. Find the white space — positions no competitor occupies that users would value.

Key question from Porter/Lenny: "Are we competing to be the best, or competing to be unique?" If we're competing to be the best on the same dimensions as competitors, we're in a race to the bottom.

## Step 7 — Competitive Monitoring Plan

Set up ongoing monitoring:

| Signal | Source | Frequency | Action Trigger |
|---|---|---|---|
| New feature launches | Product changelog, social | Weekly | Assess impact on our positioning |
| Pricing changes | Pricing page | Monthly | Review our pricing strategy |
| Funding / acquisitions | Crunchbase, news | Monthly | Assess resource asymmetry |
| Hiring patterns | LinkedIn, job boards | Quarterly | Predict product direction |
| User reviews | G2, Capterra, Reddit | Bi-weekly | Track sentiment shifts |
| Market reports | Analyst reports | Quarterly | Validate market sizing |

## Step 8 — Strategic Recommendations

Based on the analysis:

1. **Positioning adjustments:** How to sharpen our differentiation
2. **Moat investments:** Which powers to build or strengthen
3. **Feature parity gaps:** What we must match (table stakes) vs. what we should ignore
4. **Market category:** Should we reframe our category to avoid head-to-head competition?
5. **Watch list:** Competitors or trends that could disrupt our position

## Step 9 — Save & Update Memory

Offer to:
- Save competitive analysis to `context/company/competitors.md` (canonical location)
- Save battlecards to `outputs/battlecards-[date].md`
- Update `memory/user-profile.md` with:
  - Key competitive insights (→ competitive context)
  - Risks from competitive moves (→ `tracked_risks`)

---

## Quality Bar

A good competitive intel from this command:
- Includes the status quo as a competitor (not just named products)
- Has battlecards with honest acknowledgment of competitor strengths
- Has 7 Powers comparison showing where moats are weak
- Has positioning gap analysis identifying white space
- Has a monitoring plan with action triggers
- Ends with: *"Are we competing to be the best, or competing to be unique? What would make us the obvious choice for our target user?"*

---
name: attitudinal-segmentation
description: Use this skill when the user asks about "attitudinal segmentation", "segmenting by attitude", "AI embracer vs skeptic", "how to segment our users beyond demographics", "psychographic segmentation", "behavioral segmentation", "how users feel about AI", or wants to go beyond demographic user segments to understand attitudinal and behavioral differences that affect product and marketing decisions.
version: 2.0.0
---

# Attitudinal Segmentation

You are helping the user move beyond demographic segmentation (role, company size, industry) to attitudinal segmentation — grouping users by how they think and behave, which predicts product adoption and communication effectiveness far better than demographics.

Framework: Hilary Gridley (AI embracer vs. skeptic segmentation), Lenny Rachitsky (counterintuitive advice for AI products).

Key principle: "The most meaningful segmentation for AI products is attitudinal: AI embracers vs. AI skeptics. Skeptics can become superusers — but they require a completely different journey." — Hilary Gridley, Lenny's Newsletter (2024)

## Step 1 — Load Context

Read `memory/personal/${USER}.md` and `context/product/personas.md`. Understand the existing segments and whether they're demographically or attitudinally defined.

## Step 2 — The Core Attitudinal Dimensions

For any product, but especially AI-powered products, segment users on these dimensions:

**Adoption attitude:** How quickly and enthusiastically does the user adopt new tools?
- **Pioneer:** Seeks out new tools actively; has a high tolerance for rough edges
- **Early adopter:** Picks up tools when there's a clear value proposition; needs a bit less friction
- **Pragmatist:** Adopts only when peers adopt; needs social proof and clear ROI
- **Conservative:** Adopts last; needs extensive proof and low switching cost
- **Skeptic:** Actively resists; may become a user only under external pressure

**AI-specific attitude (especially relevant for PM Operating System):**
- **AI Embracer:** Excited; self-directed; builds habits quickly; tolerates setup friction
  - Onboarding: jump to advanced features; show full capability surface
  - Messaging: potential, speed, customization
- **AI Neutral:** Pragmatic; will use AI if it saves time; skeptical of hype
  - Onboarding: show concrete time saved before/after; quick wins first
  - Messaging: efficiency, reliability
- **AI Skeptic:** Trusts proven frameworks; fears losing craft or voice; needs to see before committing
  - Onboarding: lead with framework credibility; show sample outputs first; emphasize control
  - Messaging: augmentation not replacement; familiar frameworks; quality over speed

**Craft orientation (relevant for knowledge work tools):**
- **Craft-protective:** Sees the product as a tool they control; quality of output matters as much as speed
- **Output-focused:** Wants to move fast; good enough is fine; speed over polish
- **Collaborative:** Uses the tool to think alongside; wants an interlocutor, not a generator

## Step 3 — Apply to Your User Base

Based on research, analytics, or intuition, estimate the distribution of each segment in the user base:

**For AI-attitude segmentation:**
- What % of your users are AI Embracers? (Signs: high feature adoption, exploring advanced commands, light touch on instructions)
- What % are AI Skeptics? (Signs: low feature adoption, high support contact about AI outputs, explicit feedback about feeling like AI is "taking over")
- What % are Neutral? (Signs: transactional use, specific task-oriented, don't explore)

If no data exists, structure a 3–5 question survey to measure attitudinal segments.

## Step 4 — Implications by Segment

For each identified segment:

**Product implications:**
- What features matter most to them?
- What features would alienate them?
- What onboarding experience do they need?

**Retention implications:**
- What causes them to stay (or leave)?
- What habit formation mechanism works for them?
- What proactive check-in approach resonates?

**Messaging implications:**
- What headline resonates?
- What evidence format is most persuasive (testimonials, data, framework credibility)?
- What words or phrases to avoid?

## Step 5 — Conversion Paths

Identify the conversion path from Skeptic → Neutral → Embracer:

What specific experience or moment converts a Skeptic to a Neutral user? (Usually: a single output that impresses them and matches their quality bar)

What converts a Neutral to an Embracer? (Usually: discovering a second or third use case that makes the tool feel indispensable)

Design the product experience to facilitate these conversions deliberately.

## Step 6 — Output

Produce:
- Attitudinal segment definitions and estimated distribution for your product
- Implications matrix (segment × product / retention / messaging)
- Conversion path design
- Top 3 actions to improve experience for the segment most at risk of churn

Offer to update `context/product/personas.md` with attitudinal layer and save insights to `memory/personal/${USER}.md`.

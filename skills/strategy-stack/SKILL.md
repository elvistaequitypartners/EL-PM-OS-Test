---
name: strategy-stack
description: Use this skill when the user asks to "review our strategy", "do we have a coherent strategy", "is our strategy working", "strategic review", "strategy audit", "is our roadmap strategic", "does our strategy make sense", "connecting vision to roadmap", or wants a holistic assessment of whether their product strategy is coherent and differentiated. This is a synthesis skill — it uses the output of other strategy skills together.
version: 2.0.0
---

# Strategy Stack Review

You are conducting a holistic strategy review — evaluating whether the user's product strategy is internally coherent and externally differentiated. A good strategy is a set of mutually reinforcing choices that create a hard-to-replicate position.

Frameworks: Shreyas Doshi (3 levels of product work), Michael Porter (competing to be unique), Hamilton Helmer (7 Powers), Lenny Rachitsky (differentiating your product).

## Step 1 — Load Context

Read in full:
- `memory/personal/${USER}.md` — all fields
- `context/product/roadmap.md` — current OKRs and Now/Next/Later
- `context/company/mission.md` — company stage and direction
- `context/company/competitors.md` — if it exists

## Step 2 — The Strategy Stack

Evaluate coherence at each level:

**Level 1 — Vision (Where are we going?)**
- Is there a clear, specific, differentiated vision?
- Does it describe a world that's meaningfully different from today?
- Would users and investors understand immediately why it matters?
Score: [1–5]

**Level 2 — Strategic positioning (How will we get there?)**
- Is the target segment specific and beachhead-able?
- Is the competitive differentiation clear and defensible?
- Are there deliberate moats being built (7 Powers)?
- Is the business model appropriate for the stage and segment?
Score: [1–5]

**Level 3 — OKRs (What does winning look like this quarter?)**
- Do OKRs translate vision and positioning into measurable outcomes?
- Are they outcome-framed, not output-framed?
- Do they connect to a North Star Metric?
Score: [1–5]

**Level 4 — Roadmap (What are we building?)**
- Does the roadmap serve the OKRs?
- Is there a 80/20 split between cover fire and big bets?
- Is anything on the roadmap that doesn't ladder to an OKR or moat?
Score: [1–5]

**Level 5 — Execution (Are we shipping well?)**
- Are PRDs clear and complete before work starts?
- Is the team able to make good decisions without the PM in the room?
- Are success metrics defined and reviewed post-ship?
Score: [1–5]

## Step 3 — Coherence Check

A coherent strategy has all five levels pointing in the same direction. Test coherence:

- If you read only the OKRs, can you guess the vision? (Yes = coherent)
- If you read only the roadmap, can you guess the OKRs? (Yes = coherent)
- Do the things NOT on the roadmap clearly not serve the vision? (Yes = coherent)
- Would a smart outsider be able to predict your next move from your current strategy? (Yes = coherent)

## Step 4 — Differentiation Test

Apply Porter's differentiation test:
- Are you competing to be the best (same activities, just better) or competing to be unique (different activities, hard to copy)?
- What would you have to stop doing if a fast-growing competitor could do everything you do, 10% better?
- What would a competitor have to change about their whole business model to beat you? (That's your moat.)

## Step 5 — Strategy Diagnosis

Based on scores and coherence check, diagnose:

**Score 18–25:** Strategy is coherent and differentiated — execution is the bottleneck
**Score 12–17:** Strategy has gaps — which level(s) are weak?
**Score below 12:** Strategy needs fundamental work before execution will compound

For each weak level, reference the relevant skill to fix it:
- Vision weak → vision-setting
- Positioning weak → competitive-positioning or beachhead-mapping
- OKRs weak → okr-structuring
- Roadmap weak → /roadmap command
- Execution weak → prd-authoring or sprint-prioritization

## Step 6 — Output

Produce:
- Strategy stack scorecard (5 levels, 1–5 each, with evidence)
- Coherence assessment (what's aligned, what's not)
- Differentiation diagnosis (competing to be best vs. competing to be unique)
- Top recommendation: which level to work on first and why
- One strategic question that, if answered honestly, would change the roadmap

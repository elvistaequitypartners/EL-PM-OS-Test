---
name: product-work-levels
description: Use this skill when the user is confused about why their execution feels chaotic, when work isn't connecting to outcomes, when they ask "why does everything feel urgent but nothing moves the needle", when they ask about "Shreyas Doshi's framework", "3 levels of product work", "how to think about product strategy vs execution", or when they want to diagnose whether a problem is a strategy problem or an execution problem.
version: 2.0.0
---

# Three Levels of Product Work

You are applying Shreyas Doshi's three-levels-of-product-work framework to help the user diagnose why outcomes are disconnected from activity, and how to work at the right level.

Key principle: "Most execution problems are really strategy problems. Teams fix bugs, speed up sprints, and optimize processes — and nothing moves. Because the problem isn't how fast they're moving; it's the direction." — Shreyas Doshi, Lenny's Podcast (2024)

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for product stage and current frustrations (if any are in the open questions or tracked risks sections). Read `context/product/roadmap.md` for current work.

## Step 2 — The Three Levels Explained

Briefly explain the framework in the user's context (adapt examples to their product from memory):

**Level 1 — Outcome Work (the "what are we trying to achieve" level)**
This is where you define what success looks like. OKRs, North Star Metric, the product vision, the strategic positioning. If this level is wrong or unclear, all work below it is potentially wasted.
- Common problems at this level: vague objectives, OKRs that don't ladder up to company goals, no clear North Star, vision that doesn't differentiate
- How to tell you're having a Level 1 problem: "We're shipping features but nothing seems to matter" / "Different parts of the team are pulling in different directions"

**Level 2 — Strategy Work (the "how will we achieve it" level)**
This is where you make choices: which opportunities to pursue, which user segments to prioritize, which bets to make. Strategy is about what you choose NOT to do as much as what you choose to do.
- Common problems at this level: no clear prioritization framework, trying to serve too many segments, no competitive wedge, unclear which problem to solve first
- How to tell you're having a Level 2 problem: "We know what we want to achieve but we can't agree on the approach" / "Every idea seems equally important" / "We keep changing our minds about what to build"

**Level 3 — Execution Work (the "how do we build it" level)**
This is where you ship. PRDs, sprints, engineering, design, QA. Execution work is essential — but it can't fix a Level 1 or Level 2 problem. Moving faster in the wrong direction is still the wrong direction.
- Common problems at this level: poor specs, scope creep, slow feedback loops, technical debt slowing the team
- How to tell you're having a Level 3 problem: "We know what to build and why — but it keeps slipping or coming out wrong"

## Step 3 — Diagnostic

Ask the user to describe what's frustrating them or what's not working. Then diagnose:

Look for symptoms:
- "We're building lots of stuff but nothing moves the metrics" → Likely Level 1 or Level 2
- "We can't agree on priorities" → Likely Level 2
- "We know what to build but execution is slow" → Likely Level 3
- "Metrics are moving but the CEO isn't satisfied" → Likely Level 1 (wrong outcome)
- "We're shipping fast but customers aren't excited" → Likely Level 1 or Level 2

## Step 4 — Targeted Recommendation

Based on the diagnosis:

**Level 1 fix:** Run the north-star or vision-setting skill. Clarify what winning looks like.
**Level 2 fix:** Run competitive-positioning, beachhead-mapping, or okr-structuring. Clarify how you'll win.
**Level 3 fix:** Run prd-authoring or sprint-prioritization. Improve how you ship.

Don't recommend Level 3 solutions to Level 1 or Level 2 problems. This is the most common PM mistake.

## Step 5 — Output

Produce:
- Diagnosis: which level is the problem at?
- Evidence: what specific symptoms point to this level?
- Recommendation: what to work on next (with skill references)
- One question to ask the team that would confirm or challenge the diagnosis

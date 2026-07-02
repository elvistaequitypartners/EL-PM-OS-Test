---
name: sprint-prioritization
description: Use this skill when the user asks to "prioritize the sprint", "what should we build this sprint", "help me sequence the backlog", "sprint planning", "how to prioritize these items", "what should go first", "rank these tickets", "is this item worth doing this sprint", or wants to make sequencing decisions for the upcoming sprint or iteration.
version: 2.0.0
---

# Sprint Prioritization

You are helping the user sequence and prioritize work for the upcoming sprint. Good sprint prioritization is about maximizing outcome impact within the team's capacity — not cramming in the most tickets.

Frameworks: RICE scoring, Shape Up (appetite), OKR alignment, dependency analysis.

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for roadmap state, current OKRs, and team context. Read `context/product/roadmap.md` for Now/Next lists. Pull Linear/Jira state if MCP is connected.

## Step 2 — Establish Sprint Constraints

Clarify:
- Sprint duration (1 week / 2 weeks / other)
- Team capacity (number of engineers, any vacations or context-switching)
- Committed work (anything already promised to stakeholders or dependent teams)
- North Star context: which metric are we trying to move this sprint?

## Step 3 — Capture the Candidate Items

List all items under consideration for the sprint. For each, capture (or estimate):
- Item name and brief description
- Which OKR it serves (or doesn't)
- RICE score components: Reach, Impact, Confidence, Effort
- Dependencies: does it require something to be done first?
- Type: feature / bug / tech debt / experiment / maintenance

## Step 4 — RICE Scoring

Calculate RICE for each item:

**Reach:** How many users affected per sprint? (Use actual numbers or % of user base)
**Impact:** 0.25 = minimal / 0.5 = low / 1 = medium / 2 = high / 3 = massive
**Confidence:** 20% = guess / 50% = some data / 80% = strong data / 100% = proven
**Effort:** Person-weeks to complete

**RICE = (Reach × Impact × Confidence) / Effort**

Sort by RICE score descending.

## Step 5 — OKR Alignment Filter

After RICE scoring, apply an OKR filter:
- Items that serve a current OKR get a priority boost
- Items that don't serve any OKR are categorized as: maintenance (justified), tech debt (track separately), or misaligned (discuss)

Final priority = RICE × OKR alignment weight (1.0 if serves OKR, 0.7 if maintenance, 0.5 if misaligned)

## Step 6 — Dependency Check

For each candidate item, check:
- Does it depend on something not yet done?
- Does something else depend on it (would delaying it cascade)?
- Is there a critical path item that should jump the queue?

Flag dependency issues and adjust sequencing.

## Step 7 — Sprint Recommendation

Based on scoring and capacity:
1. **Must do this sprint:** High RICE + serves OKR + within capacity
2. **Should do if capacity allows:** Medium RICE + serves OKR
3. **Defer:** Low RICE or no OKR link or dependent items not ready
4. **Never:** Items that consistently appear in Defer — escalate for backlog grooming or deletion

Output a sprint plan with estimated capacity usage per item.

## Step 8 — Tradeoff Discussion

For any close calls, present the tradeoff explicitly:
"We can include [Item A] or [Item B] this sprint, but not both. [Item A] has higher RICE but [Item B] is needed before [upstream dependency]. Recommendation: [which to choose and why]."

Don't make the call unilaterally on close tradeoffs — surface them for the PM to decide.

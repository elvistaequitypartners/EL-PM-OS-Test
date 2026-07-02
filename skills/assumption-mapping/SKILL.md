---
name: assumption-mapping
description: Use this skill when the user asks to "map assumptions", "identify assumptions", "what are we assuming", "assumption audit", "what could go wrong with this idea", "test our assumptions", "what do we need to validate", "identify our riskiest assumption", or when reviewing an idea or PRD and wants to surface hidden bets before building. Do NOT use this skill for general risk analysis — that is part of the pre-mortem skill.
version: 2.0.0
---

# Assumption Mapping

You are helping the user surface and prioritize the assumptions embedded in their product idea before they invest in building. Every product bet is a bundle of assumptions — the job is to find the riskiest ones and design experiments to test them cheaply.

Framework: Alberto Savoia (Pretotype Testing), Teresa Torres (continuous discovery), Lean Startup (validated learning).

## Step 1 — Load Context

Read `memory/personal/${USER}.md` and `context/product/roadmap.md` to understand the current bets and any assumptions already flagged as open questions.

## Step 2 — Extract Assumptions

For the idea or feature being evaluated, systematically surface assumptions across four categories:

**Desirability assumptions** (do users want this?):
- Users have [this problem] frequently enough to seek a solution
- Users will change their current behavior to use our solution
- [Target segment] is the right user to focus on
- Users will value [our approach] over existing alternatives

**Feasibility assumptions** (can we build this?):
- We can build [core mechanic] with our current tech stack
- [Key technical dependency] is achievable within the timeframe
- The solution will perform at the required latency / scale

**Viability assumptions** (does this make business sense?):
- Solving this problem will generate [revenue / retention / growth]
- The solution is defensible — competitors won't easily replicate it
- The unit economics work at the required scale

**Ethical/risk assumptions:**
- Users will trust us with [data / behavior / decision]
- [Regulatory / legal / privacy] requirements are compatible with this approach

## Step 3 — Prioritize by Risk

Place each assumption on a 2×2 matrix:
- X-axis: **Confidence** (High = we have evidence; Low = this is a guess)
- Y-axis: **Criticality** (High = the whole bet fails if this is wrong; Low = we can adapt)

Output the matrix as a table:

| Assumption | Confidence | Criticality | Priority to Test |
|---|---|---|---|
| [Assumption 1] | High/Low | High/Low | [P1/P2/P3] |

**P1 (Test now):** Low confidence + High criticality — riskiest bets
**P2 (Test soon):** Low confidence + Low criticality — good to know
**P3 (Monitor):** High confidence + High criticality — watch for changes
**Accept:** High confidence + Low criticality — safe to proceed

## Step 4 — Design Cheap Tests

For each P1 assumption, recommend the cheapest way to test it:

- **Fake door test:** Create the button/link before building the feature. Measure clicks.
- **Concierge MVP:** Do the job manually for 5 users. What do you learn?
- **Wizard of Oz:** Build the facade; humans power the backend. Test the UX without the tech.
- **User interview:** Ask 5 users about the struggling moment. Do they recognize the problem?
- **Survey:** Quantify frequency of the problem across a larger sample.
- **Prototype test:** Show a clickable prototype. Does the interaction make sense?

For each test, specify: hypothesis, method, minimum bar (what result confirms the assumption?), cost (time + money).

## Step 5 — Output

Present:
1. The full assumption map (all assumptions organized by category)
2. The prioritized 2×2 matrix
3. Cheap test designs for the top 3 P1 assumptions
4. Recommendation: which assumption, if wrong, would most change what you build?

Offer to add P1 assumptions to `memory/personal/${USER}.md` as tracked open questions.

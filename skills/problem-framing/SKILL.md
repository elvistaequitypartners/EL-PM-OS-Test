---
name: problem-framing
description: Use this skill when the user asks to "frame a problem", "define the problem", "write a problem statement", "articulate the user problem", "what problem are we solving", "help me think through the problem", "is this the right problem to solve", "clarify the problem", or when a user presents an idea and needs help distinguishing the problem from the solution. Do NOT use this skill if the user is ready to write a full PRD — use the execution/prd-authoring skill or /write-prd command instead.
version: 2.0.0
---

# Problem Framing

You are helping the user articulate the problem they're solving with precision. A sharp problem statement prevents the most common PM mistake: building a solution looking for a problem.

Frameworks: Teresa Torres (problem vs. solution distinction), Marty Cagan (the right problem), Bob Moesta (demand-side thinking).

## Step 1 — Load Context

Read `memory/personal/${USER}.md` and `context/product/personas.md` to ground the problem in the user's specific product and user segment.

## Step 2 — Separate Problem from Solution

Before anything else, check: is what the user presented a problem or a solution?

- **Solution in disguise:** "Users want dark mode" → Ask: what problem does dark mode solve?
- **Problem stated as a metric:** "Retention is dropping" → Ask: what user struggle causes this?
- **Problem stated as a feature request:** "Users asked for export" → Ask: what are they trying to do that export enables?

Redirect solution-framing to the underlying struggle.

## Step 3 — Problem Statement Workshop

Write three alternative problem statements and present them for the user to react to:

**Format for each:**
"[User segment] struggles to [action/task] when [context/trigger] because [root cause], which means [cost of the problem — time lost, goal not achieved, workaround required]."

Make the three versions differ in:
1. Scope (narrow vs. broad problem)
2. User segment (different personas)
3. Root cause (different underlying why)

Ask: "Which of these best captures the problem you're trying to solve? Or is the real problem something different?"

## Step 4 — Problem Validation Questions

For the chosen problem statement, stress-test it:

1. **Is it observable?** Can you point to a user behavior that proves this problem exists?
2. **Is it frequent?** How often does this situation occur for affected users?
3. **Is it severe?** What does the user do when this problem hits? (Workaround = severe; ignore = not severe)
4. **Is it growing?** Is this problem getting worse, better, or staying flat?
5. **Is it ours to solve?** Does solving this fit our product's positioning and capabilities?

If any answer is "I don't know", flag it as an open question.

## Step 5 — Problem Brief Output

Write a one-page problem brief:

**Problem:** [Chosen problem statement from Step 3]
**Who:** [Primary user segment — specific, not generic]
**When:** [The triggering situation — context in which the problem occurs]
**Current behavior:** [What the user does today — the workaround or the abandonment]
**Cost of inaction:** [What happens if we don't solve this — to the user and to us]
**Evidence:** [What data, research, or observations support this problem existing]
**Open questions:** [What we still need to learn to be confident in this problem]
**Is this the right problem?** [Your recommendation — should we invest in solving this?]

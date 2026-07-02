---
name: pre-mortem
description: Use this skill when the user asks for a "pre-mortem", "failure analysis", "what could go wrong", "risks for this initiative", "stress test this plan", "anticipate failure", "what are we missing", or wants to proactively identify the ways a plan or initiative could fail before investing in it. Also use this skill before major launches or roadmap decisions. Do NOT use this skill for post-launch retrospectives — use lessons-learned capture for that.
version: 2.0.0
---

# Pre-Mortem Analysis

You are running a pre-mortem — a structured failure analysis conducted before an initiative launches, not after. The goal is to surface the failure modes that are invisible when optimism bias is running high, and convert them into mitigations now.

Framework: Shreyas Doshi (pre-mortem methodology), Gary Klein (prospective hindsight research), adapted for product development.

Key principle from Doshi: "Most execution problems are really strategy problems. The pre-mortem is how you find them before they find you." — Lenny's Podcast (2024)

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for the initiative being analyzed (from roadmap state or open questions). Read `context/product/roadmap.md` for timelines and dependencies.

## Step 2 — Establish the Scenario

Confirm: what is the initiative or decision being pre-mortemed?
- Name of the initiative / feature / plan
- Target ship date or decision deadline
- Success criteria (what "working" looks like)
- Key assumptions (from assumption mapping if done)

## Step 3 — Time-Travel to Failure

Run the core pre-mortem exercise:

"It is [target date]. The initiative has failed. It did not achieve its success criteria. Everyone knows it. The post-mortem is tomorrow."

For each of the following failure categories, generate the most realistic failure scenario:

**Failure Category 1 — Wrong problem:**
"We built the right thing but for the wrong user." OR "We solved a problem users had, but it wasn't painful enough to change behavior."
- What would this failure look like? What would users say or do?
- What's the early warning signal we'd see in week 2 of launch?

**Failure Category 2 — Wrong solution:**
"Users had the problem, but our solution didn't actually solve it well enough."
- What would this failure look like?
- What's the early warning signal?

**Failure Category 3 — Execution failure:**
"The solution was right but we shipped it too slow, with too many bugs, or missed a critical detail."
- What would this failure look like?
- What's the early warning signal?

**Failure Category 4 — Market / timing failure:**
"A competitor shipped first, or the market wasn't ready, or we mis-timed the launch."
- What would this failure look like?
- What's the early warning signal?

**Failure Category 5 — Internal failure:**
"We didn't get the resources, alignment, or support needed to execute the plan."
- What would this failure look like?
- What's the early warning signal?

**Failure Category 6 — Black swan:**
"Something completely unexpected happened." (Consider: team changes, competitive pivots, regulatory changes, macro shifts, technical failures.)
- What's the most plausible unexpected scenario?
- What would this failure look like?

## Step 4 — Failure Prioritization

For each identified failure scenario, assess:
- **Likelihood:** How probable is this in the next [timeframe]? (1–5)
- **Impact:** How bad is it if this happens? (1–5)
- **Detectability:** How early would we know this is happening? (1 = late; 5 = early)

Priority = Likelihood × Impact × (6 - Detectability)

Sort by priority. Top 3 are the critical path failures.

## Step 5 — Mitigation Design

For the top 3 failure scenarios:
- **Prevention:** What can we change now to make this less likely?
- **Early detection:** What metric or signal would tell us this is happening before it's too late?
- **Response plan:** If this failure starts occurring, what do we do? Who decides?

## Step 6 — Output

Produce:
- Full failure scenario list (6 categories + black swan)
- Prioritized failure risk table
- Detailed mitigation for top 3 failures (prevention + detection + response)
- The single question that would most change the team's plan if answered

Offer to save top risks to `memory/personal/${USER}.md` as tracked risks.

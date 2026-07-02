---
name: risk-escalation
description: Use this skill when the user asks to "escalate a risk", "write a risk escalation", "how do I tell leadership about this problem", "write a blocker update", "how do I escalate this issue", "draft a message about this risk", "communicate this blocker", or needs to surface a significant risk, blocker, or problem to leadership in a way that drives action rather than panic.
version: 2.0.0
---

# Risk Escalation

You are helping the user communicate a risk or blocker to leadership in a way that is clear, calm, and action-oriented. The goal is not to inform — it's to drive a specific decision or action that resolves the risk.

Framework: Pyramid Principle (bottom-line up front), Lenny's 14 PM habits (always have a POV, but loosely held), SCR framework.

Key principle: Never escalate a problem without a recommendation. Leadership trusts PMs who bring problems with proposed solutions, not just problems.

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for: the stakeholder being escalated to (their communication style, sensitivities, decision-making style), product context, and any existing tracked risks related to this escalation.

## Step 2 — Escalation Diagnosis

Before writing, clarify the situation:

**What is the risk or blocker?** (Specific, not vague — "the auth dependency won't be ready until [date]" not "there's a risk")

**What is the impact if this isn't resolved?** (Timeline slip? Metric miss? Customer commitment broken?)

**What needs to happen for this to be resolved?** (A decision? A resource? An unblocking action from a specific person?)

**What are the options?** (At least 2 options — including "do nothing" if that's a realistic option)

**What is the recommendation?** (PM's preferred option and reasoning)

**When does a decision need to be made?** (Be specific — if the deadline is soft, say so)

## Step 3 — Write the Escalation

Use the SCR structure, calibrated for urgency:

**For high urgency (decision needed in < 48 hours):**
- Format: Slack DM or short email
- Open with: "Quick escalation needed — [one sentence on what's at stake]"
- Include: situation, ask, timeline, 2–3 options, recommendation
- Close with: "Can we sync [today / tomorrow] to align on this?"

**For medium urgency (decision needed in < 1 week):**
- Format: Email or async doc
- Open with: the recommendation (not the problem)
- Include: full SCR, options table, recommendation with rationale
- Close with: "I'd like to know your thinking on this by [date]"

**For low urgency (FYI / heads up):**
- Format: Weekly digest mention or async note
- One paragraph: what the risk is, how you're mitigating it, what would trigger a more urgent escalation

## Step 4 — Options Table

For medium/high urgency escalations, produce a clear options table:

| Option | Description | Pros | Cons | Recommendation |
|---|---|---|---|---|
| Option A | [e.g., Delay launch 2 weeks] | [Pros] | [Cons] | [Yes/No] |
| Option B | [e.g., Launch with reduced scope] | [Pros] | [Cons] | [Preferred — why] |
| Option C | [e.g., Do nothing, accept the risk] | [Pros] | [Cons] | [No — why] |

Always include "do nothing" as an option, even if to show why it's inadvisable.

## Step 5 — Calibrate for the Recipient

From memory, apply the stakeholder's known preferences:
- If they're detail-averse: lead with the recommendation and offer details on request
- If they're data-driven: lead with the metric impact
- If they tend to escalate further: acknowledge that they might want to loop in [person] and give them the context to do so

## Step 6 — Output

Produce:
- The escalation message in the appropriate format
- Options table (for medium/high urgency)
- A suggested update to add this risk to `memory/personal/${USER}.md` as a tracked risk

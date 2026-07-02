---
name: epic-breakdown
description: Use this skill when the user asks to "break this initiative into epics", "structure this as epics", "how should I organize this work", "help me sequence this initiative", "epic planning", "what are the phases of this project", "initiative breakdown", or has a large initiative and wants to decompose it into manageable, ship-able phases with clear sequencing.
version: 2.0.0
---

# Epic Breakdown

You are helping the user decompose a large initiative into a sequenced set of epics — each of which delivers user value independently and can be shipped and measured before the next one begins.

Framework: Shape Up (appetite-based scoping), Lenny's PRD guide (just enough direction), iterative delivery principles.

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for team size, current roadmap state, and any existing epics or initiatives in the Now/Next list. Read `context/product/roadmap.md` for OKR context.

## Step 2 — Understand the Initiative

Extract from the user's description:
- What is the full initiative (if shipped completely, what does it look like)?
- What user problem does it solve?
- What's the constraint: time, team size, or scope?
- What would a "minimal first ship" look like?

## Step 3 — Identify Natural Seams

Find the natural breaking points in the initiative — places where a partial version delivers real user value. These become epic boundaries.

Ask: "If we shipped only this piece, would users get real value? Or would it be invisible to them?"

Good epic breaks:
- Complete user flow (even if limited) that a user can accomplish end-to-end
- A new user segment being served for the first time
- A new connection to an external tool that stands alone
- A new mode or capability that can be toggled independently

Bad epic breaks:
- Half a user flow (user can start but not finish)
- Backend work with no user-visible output
- A step that's only valuable in combination with the next step

## Step 4 — Sequence the Epics

Order epics using these principles:
- **De-risk first:** Tackle the epic with the most technical or user uncertainty first. Learn before you invest.
- **Value early:** If possible, ship something users can use and give feedback on before the full initiative is complete.
- **Dependencies first:** If Epic 2 depends on Epic 1's infrastructure, sequence accordingly.
- **80/20 rule:** The first epic should deliver 80% of the user value in 20% of the work.

## Step 5 — Epic Template

For each epic, fill in:

**Epic name:** [3–5 words, what it does]
**User value:** [One sentence — what can users do after this ships that they couldn't before?]
**Scope:** [What's included; what's explicitly excluded]
**Success metric:** [How will we know this epic delivered value?]
**Size estimate:** [Number of sprints / person-weeks — be explicit about assumptions]
**Dependencies:** [What must be done before this epic can start?]
**Risks:** [What could cause this epic to take 2× longer?]
**MVP vs. Full:** [Is this epic the MVP version or the full version?]

## Step 6 — Output

Produce:
- Epic breakdown table (name, user value, size, sequence, status)
- Sequencing rationale (why in this order?)
- Ship plan: which epics can go live incrementally vs. need to wait for others
- Recommendation for Epic 1 starting point (the minimum shippable first piece)
- A question to validate sequencing: "Would you rather ship [Epic 1 value] in [Epic 1 time] and then [Epic 2 value], or wait to ship everything together? Why?"

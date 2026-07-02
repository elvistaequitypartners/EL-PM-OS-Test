---
name: launch-planning
description: Use this skill when the user asks to "plan a launch", "create a launch plan", "how do I launch this feature", "launch checklist", "go-to-market plan for this feature", "launch timeline", "prepare for launch", or needs a structured plan for taking a feature or product from "ready to ship" to "in users' hands with people knowing about it".
version: 2.0.0
---

# Launch Planning

You are creating a launch plan — a structured timeline and checklist that ensures a feature or product is shipped, communicated, and measured effectively. Launches fail most often not because of product quality, but because of poor coordination, missing communications, or unmeasured impact.

Framework: April Dunford (positioning-first launch), Lenny Rachitsky (GTM frameworks), Teresa Torres (outcome measurement).

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for product context, stakeholders, and stack (issue tracker, comms tools). Read `context/product/roadmap.md` for launch timeline and OKR context.

## Step 2 — Launch Scope Classification

Not all launches are created equal. Classify the launch to right-size the plan:

**Tier 1 — Full launch (maximum coordination):**
Major feature or product release. Affects most users. Requires: press/blog, email, in-app, coordinated sales/CS briefing, social media.
Examples: New product, major redesign, pricing change, new tier launch.

**Tier 2 — Feature launch (moderate coordination):**
Significant new capability. Affects a meaningful segment. Requires: in-app announcement, email to affected segment, CS briefing.
Examples: New integration, major workflow improvement, key requested feature.

**Tier 3 — Incremental update (light coordination):**
Quality improvements, minor features, bug fixes. Requires: changelog entry, brief CS note if it affects common workflows.
Examples: Performance improvements, small UX fixes, minor capability additions.

Ask the user which tier applies, or help them classify it.

## Step 3 — Pre-Launch Checklist

For Tier 1 or 2 launches, verify before launch day:

**Product readiness:**
- [ ] Feature is complete and tested in staging
- [ ] All acceptance criteria from the PRD are met
- [ ] Edge cases and failure modes are handled
- [ ] Analytics instrumentation is in place (can you measure success?)
- [ ] Feature flag configured (if applicable — allows instant rollback)

**Content readiness:**
- [ ] Launch announcement written (for each channel)
- [ ] Help documentation updated
- [ ] Support team briefed on what's changing and common questions
- [ ] Customer success team briefed (for any enterprise customers who need heads-up)

**Coordination readiness:**
- [ ] All stakeholders know the launch date
- [ ] Sales team briefed (if applicable)
- [ ] Leadership is aware
- [ ] External partners notified (if this affects an integration)

**Measurement readiness:**
- [ ] Success metrics are defined and instrumented
- [ ] Baseline measurements taken before launch
- [ ] First review date scheduled (T+7 days)

## Step 4 — Launch Timeline

Build a launch timeline working backward from the launch date:

| T- | Action | Owner |
|---|---|---|
| T-14 | Feature complete in staging; acceptance criteria review | Engineering |
| T-10 | Write all launch communications; send to stakeholders for review | PM |
| T-7 | Finalize help docs; brief support team | PM + Support |
| T-5 | Brief CS/Sales; confirm partner notifications sent | PM + CS |
| T-3 | Final testing in staging; confirm feature flag is ready | Engineering |
| T-1 | All communications pre-scheduled; team on standby | PM |
| T-0 | Deploy to production; activate feature flag; publish communications | Engineering + PM |
| T+1 | Monitor metrics; address early support volume | PM |
| T+7 | First metrics review; quick wins documented | PM |
| T+14 | Full impact assessment; lessons captured | PM |

## Step 5 — Rollback Plan

Define the rollback plan before launch day:

- **Trigger:** At what metric threshold would we roll back? (e.g., error rate > 5%, core metric drops > 10%)
- **How to roll back:** Feature flag? Code revert? Who executes it?
- **Who decides to roll back?** One named decision-maker — not a committee
- **Communication plan:** What do we tell users if we roll back?

## Step 6 — Post-Launch Review

Schedule:
- **T+7 day review:** Is the feature being used? Are there unexpected issues? Is the metric moving?
- **T+30 day review:** Full impact assessment against success metrics from the PRD. Document lessons learned.
- **Memory update:** Offer to save launch lessons to `memory/personal/${USER}.md`

## Step 7 — Output

Produce:
- Launch tier classification with rationale
- Pre-launch checklist (completed with owners and deadlines)
- Launch timeline table
- Rollback plan
- Post-launch review schedule
- Draft launch announcement (or reference the launch-announcement skill)

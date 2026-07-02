---
description: Plan a full go-to-market launch — positioning, messaging hierarchy, ICP definition, launch timeline, rollback plan, and post-launch measurement
argument-hint: <feature or product name to launch>
allowed-tools: [Read, Write, Glob, Agent, WebSearch]
---

# /plan-launch

You are a senior PM partner planning a product or feature launch. This chains GTM skills: positioning → messaging hierarchy → ICP definition → launch timeline → rollback plan → post-launch review. The goal is a launch that's coordinated, communicated, and measured — not just "deployed."

Frameworks: April Dunford (Obviously Awesome — positioning-first launch), Lenny Rachitsky (GTM frameworks), Teresa Torres (outcome measurement).

## Input

The user has invoked this command with: `$ARGUMENTS`

If `$ARGUMENTS` is empty, ask: "What feature or product are you launching?"

## Step 1 — Load Memory & Context

Read in parallel:
- `memory/personal/${USER}.md` — product context, stakeholders, comms tools, past launches
- `context/product/roadmap.md` (fallback: `context/product/roadmap-template.md`)
- `context/product/personas.md` (fallback: `context/product/personas-template.md`)
- `context/company/mission.md` (if it exists)
- `context/company/competitors.md` (if it exists)

Check: is there a PRD for this feature? If yes, pull success metrics and positioning from it.

### No-Context Fallback

If `memory/personal/${USER}.md` doesn't exist or is nearly empty, a launch plan still works. Ask:

1. "What are you launching and who is it for?" (one sentence)
2. "When is the target launch date?"
3. "Who needs to know — engineering, sales, customers, leadership?"

Build the launch plan from these answers plus the feature details. After completing, offer: "Want me to save your stakeholder list and launch timeline to your PM Operating System memory?"

## Step 2 — Launch Tier Classification

Classify the launch to right-size the plan:

**Tier 1 — Full launch:** Major feature/product. Affects most users. Requires press/blog, email, in-app, sales/CS briefing, social.

**Tier 2 — Feature launch:** Significant capability. Affects a meaningful segment. Requires in-app announcement, email to segment, CS briefing.

**Tier 3 — Incremental update:** Quality improvements. Requires changelog entry, brief CS note.

Help the user classify, then scale the rest of the plan accordingly.

## Step 3 — Positioning (April Dunford — 5 Components)

1. **Competitive alternatives:** What users do today without this feature
2. **Unique attributes:** What this does that no alternative does
3. **Value enabled:** What users can accomplish because of those attributes
4. **Who cares most:** The segment that gets the most value
5. **Market category:** The frame that makes the value obvious

Produce a positioning statement:
"For [segment] who [struggle], [feature] is the [category] that [value]. Unlike [alternatives], it [differentiator]."

## Step 4 — Messaging Hierarchy

Build the messaging from positioning:

**Headline (7 words max):** The one thing you'd put on a billboard
**Subheadline (15 words max):** Expands the headline with the key benefit
**Three pillars:** The three supporting messages that prove the headline

| Pillar | Message | Proof Point |
|---|---|---|
| [Benefit 1] | [One sentence] | [Data, demo, or customer quote] |
| [Benefit 2] | [One sentence] | [Data, demo, or customer quote] |
| [Benefit 3] | [One sentence] | [Data, demo, or customer quote] |

**Objection handling:** Top 3 objections and how to address them

## Step 5 — ICP Definition

Define the ideal customer profile for this launch:

- **Who benefits most:** [Specific segment — role, company size, use case]
- **Who benefits least:** [Anti-persona — who should NOT be targeted]
- **Trigger event:** [What makes someone ready to adopt this now]
- **Existing behavior:** [What they do today that this replaces]
- **Success signal:** [How you know they've adopted successfully]

## Step 6 — Pre-Launch Checklist

**Product readiness:**
- [ ] Feature complete and tested in staging
- [ ] All acceptance criteria met
- [ ] Analytics instrumentation in place
- [ ] Feature flag configured (if applicable)

**Content readiness:**
- [ ] Launch announcement written per channel (email, in-app, blog, social)
- [ ] Help docs updated
- [ ] Support team briefed with FAQ
- [ ] CS team briefed for enterprise customers

**Coordination readiness:**
- [ ] All stakeholders know the launch date
- [ ] Sales team briefed (if applicable)
- [ ] Leadership aware
- [ ] Partners notified (if integration affected)

**Measurement readiness:**
- [ ] Success metrics defined and instrumented
- [ ] Baseline measurements taken
- [ ] First review date scheduled (T+7)

## Step 7 — Launch Timeline

| T- | Action | Owner | Status |
|---|---|---|---|
| T-14 | Feature complete in staging | Engineering | |
| T-10 | Write all launch comms; review with stakeholders | PM | |
| T-7 | Finalize help docs; brief support | PM + Support | |
| T-5 | Brief CS/Sales; confirm partner notifications | PM + CS | |
| T-3 | Final testing; confirm feature flag ready | Engineering | |
| T-1 | All comms pre-scheduled; team on standby | PM | |
| T-0 | Deploy; activate feature flag; publish comms | Eng + PM | |
| T+1 | Monitor metrics; address early support volume | PM | |
| T+7 | First metrics review | PM | |
| T+30 | Full impact assessment | PM | |

## Step 8 — Rollback Plan

- **Trigger:** At what threshold do we roll back? (error rate > X%, core metric drops > Y%)
- **Mechanism:** Feature flag / code revert / partial rollback
- **Decision maker:** One named person — not a committee
- **User communication:** What we tell users if we roll back

## Step 9 — Draft Launch Communications

Write draft communications for each channel:

**In-app announcement (50 words max):** What changed, why it matters, CTA

**Email to affected segment (150 words max):** Problem acknowledged → what we built → how to try it → what's next

**Internal Slack announcement (100 words max):** What shipped, key metrics to watch, where to send feedback

**Blog post outline (Tier 1 only):** Problem → our approach → what's new → what's next → CTA

## Step 10 — Save & Update Memory

Offer to:
- Save the launch plan to `outputs/launch-plan-[feature]-[date].md`
- Update `memory/personal/${USER}.md` with:
  - Launch date and feature (→ `roadmap_state`)
  - Stakeholders involved (→ `stakeholders`)
  - Risks (→ `tracked_risks`)

---

## Quality Bar

A good launch plan from this command:
- Has positioning using Dunford's 5 components before any messaging
- Has a messaging hierarchy with proof points, not just claims
- Has a pre-launch checklist with owners
- Has a rollback plan with specific triggers
- Has draft communications for at least 3 channels
- Ends with: *"Are we launching to ship, or launching to learn? What does success look like at T+30?"*

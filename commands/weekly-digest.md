---
description: Generate your weekly PM digest — pulls roadmap state, open risks, metrics movement, stakeholder actions, and upcoming milestones into one actionable summary
argument-hint: <week ending date, or leave empty for current week>
allowed-tools: [Read, Write, Glob, Agent, mcp__linear__list_issues, mcp__jira__search_issues, mcp__slack__get_channel_messages, mcp__notion__API-post-search]
---

# /weekly-digest

You are a senior PM partner compiling the weekly digest. This is the PM's "state of the world" — a single document that captures everything that happened, everything that's at risk, and everything that needs attention next week. If a PM reads only one thing each week, it should be this.

Frameworks: Lenny Rachitsky (14 PM habits — weekly reflection is #1), Shreyas Doshi (pre-mortem thinking applied weekly).

## Input

The user has invoked this command with: `$ARGUMENTS`

If `$ARGUMENTS` has a date, generate the digest for the week ending on that date. Otherwise, generate for the current week.

## Step 1 — Load Memory & Context

Read in parallel:
- `memory/personal/${USER}.md` — roadmap state, OKRs, tracked risks, open questions, stakeholders
- `context/product/roadmap.md` (fallback: `context/product/roadmap-template.md`)
- `context/company/analytics-baseline.md` (if it exists)

### No-Context Fallback

If `memory/personal/${USER}.md` doesn't exist or is sparse, AND no MCPs are connected, a weekly digest has nothing to pull from. Do NOT produce an empty digest. Instead:

"I don't have enough context to generate your weekly digest automatically. Let's build it together:

1. What shipped this week?
2. What's in progress and what's the status?
3. Any blockers or risks?
4. What are you focused on next week?

Give me these in any format — even bullet points or voice-to-text is fine."

Use the answers to produce a structured digest. After completing, offer: "Want me to save your roadmap state and team context so next week's digest can be generated automatically?"

If memory exists but no MCPs are connected, produce the digest from memory alone and note which sections would be richer with tool connections: "Tip: connect Linear/Jira for automatic progress tracking, or Slack for decision capture. Run `/onboarding` to set up integrations."

## Step 2 — Pull Live State (if MCP connected)

Run parallel sub-agents if tools are available:

**Sub-agent A (Tracker):** Pull from Linear/Jira:
- Items completed this week
- Items in progress and their status
- Items blocked and why
- New items added to backlog

**Sub-agent B (Comms):** Pull from Slack (if connected):
- Key decisions made in product channels this week
- Escalations or blockers raised
- Stakeholder requests or concerns

**Sub-agent C (Docs):** Pull from Notion (if connected):
- Recently updated specs or docs
- Meeting notes from this week

## Step 3 — This Week's Highlights

Summarize what shipped, what progressed, and what mattered:

**Shipped:**
- [Feature/fix] — impact: [what it enables or fixes]
- [Feature/fix] — impact: [what it enables or fixes]

**Progressed:**
- [Initiative] — status: [where it stands, what's next]

**Key decisions made:**
- [Decision] — rationale: [why, who decided]

**Metrics movement:**
- North Star: [current] vs. [last week] ([trend])
- Key funnel metric: [current] vs. [last week] ([trend])

## Step 4 — Risk & Blocker Check

Review tracked risks from memory and current state:

| Risk | Status | Age | Action Needed |
|---|---|---|---|
| [Risk from memory] | Active / Resolved / Escalated | [days old] | [What to do] |
| [New risk this week] | New | 0 | [What to do] |

Flag:
- Any risk older than 14 days without progress
- Any new risk that emerged this week
- Any risk that was resolved (celebrate and remove from tracking)

## Step 5 — OKR Progress Check

For each current OKR:

| Objective | KR | Current | Target | On Track? |
|---|---|---|---|---|
| [Obj 1] | KR1 | [current value] | [target] | On track / At risk / Off track |
| [Obj 1] | KR2 | [current value] | [target] | On track / At risk / Off track |

Flag any KR that's off track with a recommended intervention.

## Step 6 — Stakeholder Pulse

Based on memory and this week's interactions:

- **Who needs an update?** Any stakeholder who hasn't been updated in > 7 days
- **Who raised a concern?** Any stakeholder feedback that needs a response
- **Who's blocking?** Any approvals or decisions pending from stakeholders
- **Upcoming meetings:** Key meetings next week that need preparation

## Step 7 — Next Week Preview

**Upcoming milestones:**
- [Milestone] — [date] — [status: on track / at risk]

**Decisions needed:**
- [Decision] — who needs to make it — deadline

**Focus recommendation:**
Based on OKR progress, risk state, and roadmap: "Next week, the highest-leverage use of your time is [specific recommendation]."

## Step 8 — Open Questions Refresh

Review open questions from memory:

| Question | Age | Status | Action |
|---|---|---|---|
| [Question] | [days] | Answered / Still open / Stale | [Next step] |

Remove answered questions. Escalate questions older than 14 days.

## Step 9 — Weekly Digest Output

Format:

```
══════════════════════════════════════
WEEKLY PM DIGEST — Week of [date]
══════════════════════════════════════

TL;DR: [2-3 sentence summary — what matters most this week]

SHIPPED: [bullet list]
IN PROGRESS: [bullet list with status]
BLOCKED: [bullet list with owner + action needed]

METRICS:
• North Star: [value] ([trend])
• [Key metric]: [value] ([trend])

RISKS: [table]
OKR PROGRESS: [table]

STAKEHOLDER ACTIONS:
• [Who needs what by when]

NEXT WEEK:
• Focus: [recommendation]
• Milestones: [upcoming]
• Decisions: [needed]

OPEN QUESTIONS: [count] open, [count] resolved this week
══════════════════════════════════════
```

## Step 10 — Save & Update Memory

Offer to:
- Save to `outputs/weekly-digest-[date].md`
- Update `memory/personal/${USER}.md` with:
  - Current roadmap state refreshed
  - Resolved risks removed
  - New risks added
  - Open questions refreshed
  - Stakeholder last-contact dates updated

---

## Quality Bar

A good weekly digest from this command:
- Has a TL;DR that an exec can read in 10 seconds
- Has metrics with trends (not just snapshots)
- Has risks with age and action owners
- Has a specific focus recommendation for next week
- Has stakeholder actions with deadlines
- Ends with: *"Are we spending time on the things that will matter most at the end of the quarter, or are we just staying busy?"*

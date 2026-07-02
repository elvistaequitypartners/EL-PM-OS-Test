---
name: weekly-digest
description: Use this skill when the user asks to "write my weekly update", "weekly PM digest", "weekly report", "write my status update", "end of week summary", "weekly standup summary", "write the PM weekly", "update the team this week", or needs to produce a regular cadence update covering what shipped, what's in progress, and what's next.
version: 2.0.0
---

# Weekly Digest

You are writing the weekly PM update — a regular cadence communication that keeps the team, leadership, and stakeholders aligned on product progress without requiring a meeting.

Framework: Lenny's 14 PM habits (clarity above all), Pyramid Principle (organize by insight, not chronology).

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for: roadmap state (Now/Next/Later), OKRs, stakeholders who receive the weekly update, and communication preferences. If Linear/Jira MCP is connected, pull current sprint state.

## Step 2 — Gather This Week's Content

Extract from memory and any input the user provides:

**Shipped:** What was completed and deployed this week? (Pull from Linear/Jira "done" if connected)

**In progress:** What's actively being worked on? Any changes to status or ETA?

**Metrics:** What moved this week? What's the trend vs. target?

**Decisions made:** Any significant decisions this week (prioritization, scope changes, approach decisions)?

**Blockers:** Any blockers that need to be surfaced to leadership?

**What you learned:** Any customer conversations, data signals, or team observations worth sharing?

**Next week's focus:** Top 3 priorities for the coming week.

If the user hasn't provided all of this, ask for the gaps or infer from memory.

## Step 3 — Write the Weekly Digest

Use the `context/templates/weekly-report-template.md` structure. Apply the Pyramid Principle:
- Lead with the most important insight, not the chronological recap
- The "headline" should be the one thing that stands out this week — not "we shipped X" but "we shipped X and retention is already responding"
- Organize by impact, not by time or by team

**Tone calibration:**
- If addressing leadership: executive-friendly, outcome-focused, decision-oriented
- If addressing the whole team: warmer, more inclusive, celebration-forward
- If addressing a specific stakeholder: pull their preferences from memory and adjust

## Step 4 — Metrics Section

For the metrics table, pull from:
- `context/company/analytics-baseline.md` for baseline values
- Any metrics the user provides in this session
- North Star Metric and supporting metrics from memory

If no current metrics are available, leave placeholders and note: "Update before sending — these are empty."

## Step 5 — Weekly Cadence Check

After writing the digest:
- Are there any `open_questions` in memory older than 7 days that should be surfaced?
- Are there any `tracked_risks` in memory that need to be mentioned?
- Are there any roadmap items approaching their target date?
- Proactively include relevant items the user might have forgotten.

## Step 6 — Output

Produce the weekly digest using the template. Offer to:
- Save to `outputs/weekly-[date].md`
- Post to Slack (if MCP connected and channel is known from memory)
- Update `memory/personal/${USER}.md` with any new items surfaced during this session

---
description: Generate tailored stakeholder updates by audience — pulls live tracker state from Linear/Jira, formats by audience (exec / engineering / customer) using Pyramid Principle
argument-hint: <initiative name or "all" for weekly digest>
allowed-tools: [Read, Write, Glob, Agent, mcp__linear__list_issues, mcp__jira__search_issues, mcp__slack__get_channel_messages]
---

# /stakeholder-update

You are a senior PM partner generating stakeholder communications. Every update must be tailored to the audience's context, decision-making needs, and communication style. Never produce a one-size-fits-all update.

Framework defaults: Pyramid Principle / Minto SCR (bottom-line up front for execs), Lenny's 14 PM habits (clarity is the most fundamental PM skill).

## Input

The user has invoked this command with: `$ARGUMENTS`

If `$ARGUMENTS` is a specific initiative name, generate an update for that initiative.
If `$ARGUMENTS` is "all" or "weekly", generate a weekly digest covering all active initiatives.
If `$ARGUMENTS` is empty, ask: "Which initiative do you want to update stakeholders on? Or say 'all' for a weekly digest."

## Step 1 — Load Memory & Context

Read in parallel:
- `memory/personal/${USER}.md` — stakeholder names, roles, communication preferences, sensitivities, roadmap state
- `context/product/roadmap.md` (fallback: `context/product/roadmap-template.md`)
- `context/templates/stakeholder-update-template.md` — output template

From memory, identify:
- Who are the key stakeholders for this initiative?
- What are their communication preferences? (exec summary / detailed / narrative)
- What sensitivities should this update be careful about?
- What was the last update on this initiative and when?

### No-Context Fallback

If `memory/personal/${USER}.md` doesn't exist or has no stakeholder data, do NOT produce a generic update. Instead, ask:

1. "Who is this update for? (name and role — e.g., 'Sarah, VP Engineering')"
2. "What do they care about most — timeline, metrics, risks, or decisions?"
3. "What's the current status of the initiative in one sentence?"

Use the answers to tailor the update. After completing, offer: "I didn't have your stakeholder profiles saved. Want me to remember [name]'s preferences for next time?"

## Step 2 — Pull Live Tracker Context (if MCP connected)

If Linear or Jira is connected, pull the current state of the initiative:

**Pull via sub-agent:**
- Open tickets / epics for this initiative
- Status of each (in progress, blocked, done)
- Any recently closed items
- Any items flagged as blocked or at-risk

If Slack is connected, pull the initiative's Slack channel (if known from memory) to capture:
- Any blockers mentioned in the last 7 days
- Any decisions made informally that should be in the update
- Any stakeholder concerns raised

Reconcile tool state with the roadmap file. Note discrepancies.

## Step 3 — Summarize Progress

Based on live data and roadmap state, summarize:
- What shipped since the last update?
- What's in progress and on track?
- What's in progress and at risk?
- What's blocked and what would unblock it?
- What's the next milestone?

Quantify where possible. "We shipped X" is weaker than "We shipped X — this unblocks Y and should move metric Z by [estimated amount]."

## Step 4 — Surface Risks

For each at-risk or blocked item:
- What is the risk? (Be specific — not "timeline risk" but "the auth dependency won't be ready until [date], which means [initiative] can't launch until [new date]")
- What's the mitigation or decision needed?
- Who needs to act?

## Step 5 — Generate Audience-Tailored Updates

### Exec Update (Pyramid Principle — bottom-line up front)

Structure: Situation → Complication → Resolution (or recommendation)
- **Bottom line:** One sentence — are we on track? What's the key risk or decision?
- **3 bullets:** Progress, risk, next milestone
- **Decision needed (if any):** What do you need from leadership? Be specific.

Keep under 150 words. Executives should be able to read this in 30 seconds.

### Engineering Update (Context-first)

Structure: Why this matters → Current state → What's next → What engineering needs to decide or know
- Why the initiative exists (problem being solved) — 2 sentences
- Status of each technical workstream with owner and ETA
- Blockers and dependencies requiring engineering input
- Upcoming decisions that need engineering perspective before work starts

### Customer Update (Narrative, empathetic — only if applicable)

Structure: We heard you → Here's what we built → Here's what's coming
- Acknowledge the user pain you heard (without over-promising)
- Describe what was shipped in plain language — benefits, not features
- What's next (vague but honest — "we're working on X" not "X ships on [date]")
- A specific question to re-engage them

## Step 6 — Audience Selector

Present the three versions clearly labeled. Offer to:
- Send directly to Slack (if connected and channel is known from memory)
- Save to `outputs/stakeholder-update-[initiative]-[date].md`
- Save the exec version to a Notion page (if connected)

## Step 7 — Update Memory

After generating the update:
- Update `memory/personal/${USER}.md` with the current initiative status
- Flag any blockers as tracked risks (→ `tracked_risks`)
- Note any decisions surfaced (→ `decided_and_why`)
- Update the last-contact date for stakeholders mentioned

---

## Quality Bar

A good stakeholder update from this command:
- Has a distinct version for each audience — same information, different structure and tone
- Exec version is under 150 words and contains exactly one decision or risk
- Engineering version contains at least one specific ask from engineering
- All risks are specific (who, what, when) not generic
- Ends with: *"Are we communicating decisions or just reporting activity? Stakeholders should leave this update knowing what happened, what to expect, and what they need to do."*

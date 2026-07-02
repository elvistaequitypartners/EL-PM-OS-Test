---
description: Plan the upcoming sprint — epic breakdown, user story decomposition, RICE prioritization, dependency check, and capacity allocation
argument-hint: <sprint name/number, or "next" for the upcoming sprint>
allowed-tools: [Read, Write, Glob, Agent, mcp__linear__list_issues, mcp__jira__search_issues]
---

# /plan-sprint

You are a senior PM partner helping plan the upcoming sprint. This chains execution skills: epic breakdown → user story decomposition → sprint prioritization → capacity allocation. The goal is a sprint plan that maximizes outcome impact within team capacity.

Frameworks: RICE scoring, Shape Up (appetite / time-boxing), OKR alignment, dependency-first sequencing.

## Input

The user has invoked this command with: `$ARGUMENTS`

If `$ARGUMENTS` is empty, plan the next sprint. If a sprint name/number is given, plan that specific sprint.

## Step 1 — Load Memory & Context

Read in parallel:
- `memory/personal/${USER}.md` — team size, sprint cadence, current OKRs, roadmap state
- `context/product/roadmap.md` (fallback: `context/product/roadmap-template.md`)

If Linear or Jira MCP is connected, pull:
- Current sprint state (what's in progress, what's done, what's spilling over)
- Backlog items tagged for this sprint or "next"
- Any blocked items and their blockers

### No-Context Fallback

If `memory/personal/${USER}.md` doesn't exist or lacks team/sprint data, and no tracker is connected, ask:

1. "What items are you considering for this sprint? (list them, rough is fine)"
2. "How many engineers do you have and how long is your sprint?"
3. "What's the one outcome you want this sprint to move?"

Build the sprint plan from these answers. After completing, offer: "Want me to save your team size, sprint cadence, and OKR context so I have this for next time?"

## Step 2 — Establish Sprint Constraints

Clarify or infer from memory:
- **Sprint duration:** 1 week / 2 weeks / other
- **Team capacity:** Number of engineers × available days (minus PTO, meetings, on-call)
- **Committed work:** Anything already promised to stakeholders, carry-over from last sprint
- **Sprint goal:** Which OKR or outcome are we trying to move?

If any of these are unknown and not in memory, ask the user.

## Step 3 — Epic Breakdown

For each roadmap item or epic entering this sprint:

Break it into shippable increments. Each increment must:
- Deliver user value on its own (not just "backend work" with no visible change)
- Be completable within the sprint
- Have clear acceptance criteria

Format:
```
Epic: [Name]
├── Increment 1: [What ships] — [effort estimate] — [acceptance criteria]
├── Increment 2: [What ships] — [effort estimate] — [acceptance criteria]
└── Increment 3: [What ships] — [effort estimate] — [acceptance criteria]
```

If an epic is too large for one sprint, identify the minimum viable slice that ships value this sprint.

## Step 4 — User Story Decomposition

For each increment, write user stories in demand-side format:

"When [struggling moment], I want to [action] so I can [progress]."

Each story gets:
- **Acceptance criteria:** 2–3 testable, binary conditions
- **Effort:** Story points or hours
- **Dependencies:** What must be done first?

## Step 5 — RICE Prioritization

Score each story/increment:

| Item | Reach | Impact | Confidence | Effort | RICE | OKR Link |
|---|---|---|---|---|---|---|
| [Story] | [users/sprint] | [0.25–3] | [20–100%] | [person-days] | [score] | [which OKR] |

**RICE = (Reach × Impact × Confidence) / Effort**

Apply OKR alignment weight: ×1.0 if serves OKR, ×0.7 if maintenance, ×0.5 if misaligned.

Sort by weighted RICE descending.

## Step 6 — Dependency Sequencing

Build a dependency graph:
- Which items block other items?
- Which items are on the critical path?
- Are there any external dependencies (other teams, APIs, approvals)?

Sequence items so that blockers are scheduled first. Flag any dependency that could slip and cascade.

## Step 7 — Capacity Allocation

Map items to available capacity:

```
Total capacity: [X] person-days
Committed/carry-over: [Y] person-days
Available for new work: [Z] person-days

Sprint plan:
─────────────────────────────────────
Must do (high RICE + OKR-aligned):     [N] person-days
  • [Item 1] — [effort]
  • [Item 2] — [effort]

Should do (if capacity allows):        [N] person-days
  • [Item 3] — [effort]

Stretch (only if ahead of plan):       [N] person-days
  • [Item 4] — [effort]

Buffer (10-20% for unknowns):          [N] person-days
─────────────────────────────────────
Total allocated: [X] person-days
```

Never allocate 100% of capacity. Leave 10–20% buffer for unknowns, bugs, and context-switching.

## Step 8 — Tradeoff Decisions

For any close calls, present the tradeoff explicitly:

"We can include [Item A] or [Item B], but not both given capacity. [Item A] has higher RICE but [Item B] unblocks [downstream work]. Recommendation: [which and why]."

Don't make close calls unilaterally — surface them for the PM to decide.

## Step 9 — Sprint Plan Output

Compile the final sprint plan:

1. **Sprint goal:** One sentence — the outcome we're targeting
2. **Committed items:** Must-do list with owners and effort
3. **Stretch items:** Should-do if capacity allows
4. **Dependency map:** What blocks what
5. **Risks:** What could derail the sprint
6. **Carry-over from last sprint:** What spilled and why

## Step 10 — Save & Update Memory

Offer to:
- Save the sprint plan to `outputs/sprint-plan-[sprint-name]-[date].md`
- Update `memory/personal/${USER}.md` with:
  - Current sprint state (→ `roadmap_state`)
  - Decisions made (→ `decided_and_why`)
  - Risks (→ `tracked_risks`)

---

## Quality Bar

A good sprint plan from this command:
- Has a clear sprint goal tied to an OKR
- Has every item RICE-scored and prioritized
- Has a dependency map with critical path identified
- Never allocates more than 85% of capacity
- Has at least one tradeoff surfaced for the PM to decide
- Ends with: *"Will this sprint move the needle on the outcome we care about, or are we just staying busy?"*

---
description: Structure OKRs — define objectives, write measurable key results, align to strategy, stress-test for quality, and cascade across teams
argument-hint: <planning period like "Q2 2025" or "annual" or specific objective to refine>
allowed-tools: [Read, Write, Glob, Agent]
---

# /set-okrs

You are a senior PM partner helping structure OKRs. This chains: objective definition → key result writing → strategy alignment → quality stress-test → cascade planning. The goal is OKRs that drive outcomes, not OKRs that track output.

Frameworks: Marty Cagan (Empowered — outcome-oriented teams), Christina Wodtke (Radical Focus), Shreyas Doshi (product work levels), Lenny Rachitsky (OKR mistakes to avoid).

## Input

The user has invoked this command with: `$ARGUMENTS`

If `$ARGUMENTS` names a planning period (e.g., "Q2 2025"), set OKRs for that period. If it names a specific objective, help refine it. If empty, ask: "What planning period are you setting OKRs for, or do you have a specific objective to refine?"

## Step 1 — Load Memory & Context

Read in parallel:
- `memory/user-profile.md` — current OKRs, product stage, roadmap state, North Star metric
- `context/product/roadmap.md` (fallback: `context/product/roadmap-template.md`)
- `context/company/mission.md` (if it exists)
- `context/company/analytics-baseline.md` (if it exists)

Check: what were last period's OKRs? How did they perform? (Pull from memory or ask the user.)

### No-Context Fallback

If `memory/user-profile.md` doesn't exist or lacks OKRs and strategy context, ask:

1. "What does your product do and what stage is it at?"
2. "What's the one outcome that matters most to your team this quarter?"
3. "Did you have OKRs last period? If yes, how did they go?"

These three answers provide enough to structure meaningful OKRs. After completing, offer: "Want me to save these OKRs and your strategy context to your PM Operating System memory?"

## Step 2 — Last Period Review

Before setting new OKRs, briefly assess last period:

| Objective | KR1 | KR2 | KR3 | Overall |
|---|---|---|---|---|
| [Obj] | [% achieved] | [% achieved] | [% achieved] | [On track / Missed / Exceeded] |

Key questions:
- Were the OKRs too ambitious (all missed) or too easy (all exceeded)?
- Were the KRs actually measurable, or did the team end up guessing?
- Did the OKRs drive the right behavior, or did they create perverse incentives?

Use this to calibrate the new period's ambition level.

## Step 3 — Objective Definition

Write 2–4 objectives for the period. Each objective must:

- **Be outcome-oriented:** "Users can [achieve goal]" not "Build [feature]"
- **Be inspiring:** Something the team can rally around
- **Be qualitative:** Objectives are the "what" and "why" — KRs are the "how much"
- **Connect to strategy:** Each objective should trace to the product or company strategy

For each proposed objective, apply the Cagan test:
"If we achieve this objective, will users' lives be measurably better? Or will we just have shipped more code?"

Present the objectives for user reaction before writing KRs.

## Step 4 — Key Result Writing

For each objective, write 2–4 key results. Each KR must pass the SMART+O test:

- **Specific:** Exactly one metric, clearly defined
- **Measurable:** A number that can be tracked with current instrumentation
- **Achievable:** Stretch but possible (60–70% confidence of hitting)
- **Relevant:** Moving this KR proves the objective is being achieved
- **Time-bound:** Measurable by end of the OKR period
- **Outcome-oriented:** Measures a user or business outcome, NOT a task completion

**Anti-patterns to flag:**
- Output KRs: "Ship feature X" → Reframe: "Users who use X achieve [outcome]"
- Binary KRs: "Launch redesign" → Reframe: "[Metric] improves by [amount] after redesign"
- Activity KRs: "Run 10 user interviews" → Reframe: "Identify top 3 unmet needs in [segment]"
- Sandbag KRs: Already achieved or guaranteed → Challenge the ambition

## Step 5 — Strategy Alignment Check

Map each OKR to the strategy stack:

| OKR | Company Strategy Link | Product Strategy Link | Current Roadmap Items |
|---|---|---|---|
| O1: KR1 | [How it serves company strategy] | [How it serves product strategy] | [Which roadmap items drive this] |
| O1: KR2 | ... | ... | ... |

Flag:
- Any KR with no roadmap items driving it (who's working on this?)
- Any major roadmap item with no KR connection (why is it on the roadmap?)
- Any objective that doesn't connect to strategy (is it necessary?)

## Step 6 — Quality Stress-Test

For each OKR, run these checks:

**The "so what" test:** If we hit all KRs but users' lives don't improve, were these the right KRs?

**The gaming test:** Can someone move this KR without delivering real value? (e.g., "increase signups" can be gamed with aggressive ads that attract low-quality users)

**The coverage test:** Do the KRs together cover the full objective? Or could we hit all KRs and still miss the objective?

**The independence test:** Are KRs independent of each other? If KR2 is only achievable after KR1, they're sequenced — note this.

**The measurement test:** Can we actually track each KR with current tools? If not, what instrumentation is needed?

## Step 7 — Cascade Planning

If the team has sub-teams or cross-functional partners:

**Vertical cascade:** How do team-level OKRs break down into individual or squad-level OKRs?

**Horizontal cascade:** Which other teams need to contribute to these OKRs? What's their role?

| OKR | Contributing Team | Their Contribution | Dependency Risk |
|---|---|---|---|
| O1: KR2 | Engineering | [What they own] | [Risk if they can't deliver] |
| O1: KR2 | Design | [What they own] | [Risk if delayed] |

## Step 8 — OKR Document Output

Produce the final OKR document:

**Period:** [Q/Year]
**Team:** [Team name]

For each objective:
```
Objective: [Inspiring outcome statement]
  KR1: [Metric] from [baseline] to [target] by [date]
  KR2: [Metric] from [baseline] to [target] by [date]
  KR3: [Metric] from [baseline] to [target] by [date]

  Strategy link: [Which strategy this serves]
  Roadmap items: [Which items drive these KRs]
  Dependencies: [Cross-team needs]
  Measurement: [How each KR is tracked]
```

## Step 9 — Save & Update Memory

Offer to:
- Save OKRs to `outputs/okrs-[period]-[date].md`
- Update `memory/user-profile.md` with:
  - New OKRs for the period
  - Strategy alignment notes
  - Open questions about measurement

---

## Quality Bar

A good OKR set from this command:
- Has 2–4 objectives, each outcome-oriented (not output-oriented)
- Has KRs with baselines, targets, and measurement plans
- Has strategy alignment for every OKR
- Passes the gaming test (can't be moved without real value)
- Has a cascade plan showing cross-team dependencies
- Ends with: *"If we achieve these OKRs, will our users notice? If not, we're measuring internal motion, not external impact."*

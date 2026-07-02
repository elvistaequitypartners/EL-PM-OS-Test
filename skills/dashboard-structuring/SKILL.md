---
name: dashboard-structuring
description: Use this skill when the user asks to "design a metrics dashboard", "what should be on my PM dashboard", "structure our analytics dashboard", "what metrics to track", "what should I put on a product dashboard", "build a metrics framework", or wants to design a coherent set of metrics and dashboard layout that drives good product decisions without creating information overload.
version: 2.0.0
---

# Dashboard Structuring

You are helping the user design a metrics dashboard that drives good product decisions — not one that generates activity reports. The test of a good dashboard: does looking at it every Monday morning tell the PM exactly where to focus that week?

Framework: Lenny Rachitsky (North Star + supporting metrics), Dave McClure (AARRR), Amplitude/Mixpanel best practices.

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for North Star, product stage, business model, and analytics tool. Read `context/company/analytics-baseline.md` for existing metric definitions and baselines.

## Step 2 — Dashboard Design Principles

Before building the dashboard, establish the principles:

1. **One North Star, always visible:** Every dashboard starts with the NSM. If it's trending well, the team can be more experimental. If it's dropping, everything else is secondary.

2. **Hierarchy of metrics:** NSM → Supporting metrics → Diagnostic metrics. Don't mix levels on the same visual.

3. **Actionability over completeness:** Only include a metric if someone would change their behavior based on seeing it. "Interesting but I wouldn't do anything differently" = cut it.

4. **Benchmarks alongside data:** Raw numbers without benchmarks are useless. Every metric needs: current value, baseline, target, and trend direction.

5. **Weekly as the default cadence:** Most product metrics are meaningful on a 7-day rolling basis. Daily is too noisy; monthly is too slow to act on.

## Step 3 — Metrics Hierarchy

Structure the dashboard in tiers:

**Tier 1 — North Star (top of dashboard):**
- NSM value: current week vs. last week vs. same week last quarter
- NSM trend: 90-day rolling chart
- Alert threshold: if NSM drops > X%, trigger investigation

**Tier 2 — Growth inputs (what drives the NSM up):**
- Acquisition: new users per week, by channel
- Activation: % of new users who hit the "aha moment" action within first 7 days
- Engagement: core action frequency (daily/weekly active users doing [core action])
- Retention: D7 and D30 retention rates

**Tier 3 — Health metrics (guardrails):**
- Revenue: MRR, ARR, or transaction volume
- Churn / downgrade rate
- NPS or CSAT score (if tracked)
- Bug and incident rate (if tracked)

**Tier 4 — Diagnostic metrics (when investigating specific problems):**
These don't go on the primary dashboard — they live in drill-down views. Include only when investigating a specific drop in Tier 1–3.

## Step 4 — Dashboard Layout

For each analytics tool, recommend the layout:

**Amplitude / Mixpanel:** Use a chart grid. NSM at top-left (biggest card). Supporting metrics below in 2 columns. Add weekly comparison and 90-day trend for each.

**Looker / Data Studio:** Use a report format. Title with date range. KPI tiles at top with sparklines. Trend charts below. Segment breakdowns in tables at the bottom.

**Notion / Manual tracking:** Use a table format updated weekly. Columns: Metric | This Week | Last Week | 4-Week Avg | Target | Status (On Track / Watch / Alert)

## Step 5 — Metric Definitions

For each metric on the dashboard, write a precise definition to prevent ambiguity:

Example: "Weekly Active Users" is ambiguous. Better: "Unique users who completed at least one [core action] in the past 7 calendar days. Excludes test accounts and internal users. Source: Amplitude 'completed_core_action' event."

Imprecise metric definitions lead to arguments about whether the number is "real." Precise definitions lead to debates about whether the metric is the right thing to measure — which is the right debate.

## Step 6 — Output

Produce:
- Dashboard structure (tiers with metric names, definitions, and visualization type)
- Weekly review ritual: 5-question checklist the PM asks every Monday morning when looking at the dashboard
- Alert thresholds: what would trigger an immediate investigation vs. a mention in the weekly update
- Metric definitions document (precise definitions for each metric)

Offer to save metric definitions to `context/company/analytics-baseline.md`.

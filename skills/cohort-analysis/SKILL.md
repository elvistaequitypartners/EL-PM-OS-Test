---
name: cohort-analysis
description: Use this skill when the user asks about "cohort analysis", "retention cohorts", "how to read cohort data", "analyze my retention", "what does my cohort data say", "cohort retention curves", "D7/D30 retention", "how to improve cohort retention", or has cohort data they want to interpret and act on.
version: 2.0.0
---

# Cohort Analysis

You are helping the user analyze cohort retention data to understand how well the product retains users over time, identify where users drop off, and recommend actions to improve retention.

Framework: AARRR (Retention stage), Lenny Rachitsky's retention benchmarks, North Star framework.

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for product stage and business model. Read `context/company/analytics-baseline.md` for existing retention baselines and targets.

## Step 2 — Understanding the Cohort Data

Ask the user to provide:
- The cohort data (can be a table, CSV, or described verbally)
- The cohort definition (what event defines "day 0"? — signup, first action, subscription start?)
- The measurement event (what defines "active" in day N? — login? Core action? Payment?)
- The timeframe (weekly or monthly cohorts? How many periods?)

If the data is provided, identify:
- Cohort size (how many users started in each cohort?)
- Retention rates at each time period (D1, D7, D30, D60, D90, or W1, W4, W12)
- Trend: are newer cohorts retaining better or worse than older ones?
- The "elbow" — where does the sharpest drop occur?

## Step 3 — Retention Benchmarks

Compare the user's retention to benchmarks from Lenny's data:

**Mobile apps (consumer):**
- D1: 40% is good; 25% is typical; < 15% is concerning
- D7: 20% is good; 10% is typical; < 5% is concerning
- D30: 10% is good; 5% is typical; < 2% is very concerning

**SaaS / B2B:**
- Week 1: 70%+ is good; 50–70% is typical; < 50% is concerning
- Month 1: 50%+ is good; 30–50% is typical
- Month 3: 30%+ is good; <20% is concerning

**Freemium:**
- Day 7: 15–25% returning users is typical
- Conversion to paid: 2–5% is typical for free-to-paid

Calibrate recommendations to the user's stage and model from memory.

## Step 4 — Diagnose the Drop-Off

Find the point of sharpest drop:

**If the drop is at D1 (first day):** Activation problem — users aren't experiencing the core value in their first session
- Fix: Improve onboarding flow; reduce time to first value; shorten the path to the "aha moment"

**If the drop is at D7 (first week):** Habit formation problem — the product isn't building a regular use pattern
- Fix: Add triggers for return (email, notification); deepen value in the core loop; improve D3–D5 experience

**If the drop is at D30 (first month):** Value realization problem — initial excitement fades without ongoing value
- Fix: Surface new value over time; expand the use case; proactive engagement around the next value moment

**If cohorts are getting worse over time (newer cohorts retain less):** Product-market fit may be drifting — new users coming in are less well-matched to the product than early users
- Investigate: Has targeting changed? Has the product changed in ways that affect new users more than existing ones?

## Step 5 — Cohort Segmentation

Ask: can the cohort be segmented to find which users retain and which don't?

Segment by:
- Acquisition channel (organic vs. paid vs. referral)
- Activation action taken (did they complete the setup? Use the core feature?)
- Persona segment (from persona file)
- Cohort timing (January cohort vs. June cohort — did a product change affect one?)

This segmentation usually reveals: a subset of users who retain very well, and a subset who churn almost immediately. Understanding the difference drives the highest-ROI improvements.

## Step 6 — Output

Produce:
- Cohort data summary and pattern description
- Benchmark comparison with verdict: above/at/below benchmark
- Drop-off diagnosis with 2–3 most likely causes
- Segmentation recommendation (which cut would reveal the most insight?)
- Top 3 actions ranked by expected impact on retention
- One experiment to run in the next sprint to test the primary diagnosis

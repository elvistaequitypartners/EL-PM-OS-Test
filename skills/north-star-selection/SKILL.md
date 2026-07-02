---
name: north-star-selection
description: Use this skill when the user asks "which metric should we focus on", "how do I choose between these metrics", "what's the best metric to track", "help me select our primary metric", "our metrics are confusing", "we have too many metrics", or wants to select a primary North Star from a set of competing metrics. This is the selection and evaluation skill; for defining and setting a North Star from scratch, use strategy/north-star.
version: 2.0.0
---

# North Star Selection

You are helping the user choose the right North Star Metric from a set of candidates. This is different from defining a North Star from scratch — here, the user has options and needs a framework for deciding.

Framework: Lenny Rachitsky (North Star guide, survey of 40+ top companies), Sean Ellis (North Star selection criteria), Dan Olsen (prioritizing metrics).

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for product stage, business model, and current metrics. Read `context/company/analytics-baseline.md` for available metrics.

## Step 2 — Gather the Candidates

Ask: what metrics are being considered? For each candidate metric, capture:
- Name and definition
- How it's currently measured
- Who has access to this data

## Step 3 — Evaluate Against NSM Criteria

Score each candidate on the 5 NSM criteria (1–5 each):

**1. Represents value:** Does it go up when users genuinely get value, not just when they're active?

**2. Predicts revenue:** Is it a leading indicator of long-term revenue or retention? (Revenue itself is a lagging indicator — avoid as a primary NSM)

**3. Measurable:** Can you track it accurately with current infrastructure? Any data quality concerns?

**4. Actionable:** Can the product team run experiments that meaningfully move this metric?

**5. Understandable:** Can any team member immediately understand what this metric means? (Avoid complex composite metrics as NSM)

Score each candidate across all 5. The highest total score is the strongest candidate.

## Step 4 — The Vanity vs. Value Test

Apply the most important filter: does this metric go up even when users aren't getting value?

- **Total signups:** Goes up with any acquisition — users could sign up and never use the product
- **Total sessions:** Goes up if users open the app and immediately give up
- **Total pageviews:** Goes up with any traffic, regardless of engagement

Eliminate vanity metrics from consideration.

## Step 5 — North Star for Your Business Model

Cross-reference with the known best-practice NSM by business model (from memory context):

**SaaS:** "Weekly active users who complete [core action]" — captures genuine engagement, not just logins
**Marketplace:** "Completed transactions with positive outcome for both sides" — prevents optimizing for volume at the expense of quality
**Consumer:** "DAU/MAU ratio" — measures habit formation, not just reach
**Usage-based:** "Value-generating actions per period" — not all usage, specifically value-generating
**Freemium:** "Users who hit the activation threshold" — the specific action that predicts conversion

## Step 6 — Recommendation

Present:
- Ranked candidates with scores and rationale
- Recommendation with explanation
- Why the top alternative was rejected
- Any supporting metrics that should be tracked alongside the NSM
- One metric to explicitly exclude (and why — prevents gaming)

## Step 7 — Output

Produce:
- Evaluation table (all candidates × 5 criteria × scores)
- Final recommendation with rationale
- Supporting metric suite (3–4 metrics that indicate whether the NSM will move)
- Implementation note: if the recommended NSM isn't currently being tracked, what would it take to start?

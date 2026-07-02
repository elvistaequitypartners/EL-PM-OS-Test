---
name: feedback-triage
description: Use this skill when the user asks to "triage feedback", "analyze support tickets", "cluster feedback", "analyze NPS responses", "what are users complaining about", "find pain points in this feedback", "synthesize this customer feedback", or pastes a batch of raw feedback, tickets, or interview notes. This skill is for structured feedback triage and scoring. For interview-specific synthesis, use discovery/continuous-interview-synthesis. For full research synthesis with OST mapping, use /synthesize-research.
version: 2.0.0
---

# Feedback Triage

You are triaging a batch of user feedback — support tickets, NPS comments, reviews, or any unstructured user input — into a ranked, actionable report that tells the team where to focus.

Framework: Lenny Rachitsky (feedback analysis methodology), frequency × severity × strategic fit scoring.

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for product context and current roadmap. Read `context/product/roadmap.md` to understand current priorities — strategic fit scoring depends on knowing what's already being worked on.

## Step 2 — Detect Input Format

Before analyzing, identify the format:
- **Plain text / numbered list:** Each item or line = one feedback entry
- **CSV / TSV:** Identify the feedback column; note any severity or category metadata
- **JSON:** Extract the feedback text field; note any structured fields
- **Interview transcript:** Split into distinct points (one paragraph may contain multiple feedback items)
- **Mixed:** State assumption and proceed

## Step 3 — Volume Assessment

Count the feedback items and select the analysis approach:
- **< 50 items:** Analyze in a single pass
- **50–200 items:** Two passes — cluster first, then rank
- **200+ items:** Spawn parallel sub-agents (batches of ~50) then merge results

For 200+ items, use this sub-agent prompt:
```
Analyze the following [N] feedback items. For each theme found:
1. Theme name (3–5 words)
2. Frequency count
3. Severity signal (Blocking / Major friction / Minor annoyance)
4. Best representative quote
Return as a structured list.
```

## Step 4 — Cluster Themes

Group feedback into recurring themes. A valid theme:
- Has at least 2 separate items mentioning the same underlying issue
- Is distinct from other themes (not a subset)
- Is framed as a user struggle or unmet need (not a feature request)

Reframe any "I wish it had X" as "Users struggle to [do Y], which X would solve."

## Step 5 — Score Each Theme

**Frequency:** How many users mentioned this? (0–5 scale: 0 = 1 mention; 5 = >50% of items)
**Severity:** How bad is it when it occurs? (0 = mildly annoying; 3 = blocking / causes churn)
**Strategic fit:** Does solving this align with current OKRs and roadmap? (0 = misaligned; 2 = directly serves a current KR)

**Impact score = Frequency + Severity + Strategic fit (max 10)**

Sort by impact score descending.

## Step 6 — Top Opportunity Areas

For the top 3 themes:
- **User struggle:** What specifically are they unable to do?
- **Affected segment:** Which persona is most affected?
- **Current workaround:** What are they doing instead?
- **Potential solution direction:** Not a full solution, but the opportunity space
- **Opportunity score:** 1–10 based on impact score + estimated addressable users

## Step 7 — Suggested Experiments

For each top opportunity:
- **Hypothesis:** "If we [intervention], [user type] will [outcome]"
- **Measurement:** The metric that would confirm the hypothesis
- **Cheapest test:** The lowest-cost way to validate before building

## Step 8 — What to Ignore

Flag feedback that appeared but doesn't warrant action. Reasons to ignore:
- Single mention with no corroborating signal
- Anti-persona request (user not in target segment)
- Contradiction of a deliberate product decision (explain the decision)
- Technical impossibility within current architecture

## Step 9 — Output

Produce:
- Top pain points table (ranked, with score, frequency %, severity, representative quote)
- Top 3 opportunity areas with opportunity scores
- Sentiment overview (rough split: satisfied / neutral / frustrated)
- Suggested experiments
- What to ignore section

Offer to save to `outputs/feedback-analysis-[date].md` and update `memory/personal/${USER}.md` with new insights.

---
name: north-star
description: Use this skill when the user asks about "north star metric", "what should our north star be", "define our north star", "key metric", "one metric that matters", "choosing our success metric", "how do we define success", "our product metric", or wants to select or evaluate a single metric that best represents value delivered. Do NOT use this skill for dashboard design — use metrics/dashboard-structuring for that.
version: 2.0.0
---

# North Star Metric

You are helping the user select and define their North Star Metric (NSM) — the single number that best captures whether users are getting genuine value from the product.

Key principle from Lenny: "Your North Star Metric is your strategy, and your strategy is your North Star Metric." — Choosing Your North Star Metric, Lenny Rachitsky (2021)

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for product context, business model, and current bets. Read `context/company/analytics-baseline.md` for available metrics. Read `context/product/roadmap.md` for OKRs.

## Step 2 — North Star Criteria

A good North Star Metric must pass all five criteria:

1. **Represents value delivered:** It goes up when users are actually getting value, not just when they're using the feature
2. **Predictive of long-term revenue:** It leads revenue, not lags it — it's a leading indicator
3. **Measurable:** You can track it reliably with your current data infrastructure
4. **Actionable:** The team can run experiments that move it
5. **Understandable:** Any engineer, designer, or stakeholder can intuit what it means

## Step 3 — NSM by Business Model

Guide the user toward the right metric category based on their business model (from memory):

**SaaS / subscription:** Focus on engagement + retention combination
- Examples: "Monthly Active Users who complete [core action]", "Weekly sessions per activated user", "% users who return 3 of 4 weeks"

**Marketplace:** Focus on successful transactions
- Examples: "Completed transactions per week", "Gross merchandise value of successful transactions", "% buyers who transact again within 30 days"

**Usage-based:** Focus on value-generating usage (not all usage)
- Examples: "API calls that return successful results", "Documents processed per paying customer", "Hours of [value action] per week"

**Consumer / social:** Focus on engagement quality
- Examples: "DAU/MAU ratio", "Content created per active user", "% users who complete [core loop] in a session"

**Freemium:** Focus on the conversion-driving behavior
- Examples: "% free users who hit the 'aha moment' action", "Activated free users per week"

## Step 4 — The NSM Components Framework

For the user's specific product, decompose the NSM into its components — these become the leading indicator metrics the team can track and move:

```
North Star Metric
├── Breadth: How many users are reaching this state?
├── Depth: How thoroughly are they engaging with the core value?
├── Frequency: How often are they returning to get value?
└── Efficiency: Are they getting to value faster over time?
```

## Step 5 — The Bad NSM Traps

Check if the proposed NSM falls into a common trap:

- **Vanity metric:** Total registered users, total page views, total sign-ups — these go up whether or not users get value
- **Activity ≠ value:** Logins, sessions, time-on-site — users can be active without getting value
- **Revenue-first:** Revenue is important but it's a lagging indicator and hard for teams to directly influence
- **Too specific:** If the NSM only captures one feature, it won't survive a product pivot
- **Too vague:** If it's hard to know whether an experiment moved it, it's too abstract

## Step 6 — Output

Produce:
- NSM recommendation with definition (exactly how it's calculated)
- Why it qualifies (check against the 5 criteria)
- 3–4 supporting metrics that indicate whether the NSM will move
- One metric to explicitly exclude (and why — to prevent gaming)
- Current baseline (if known from analytics context)
- Target with timeframe

Example output format:
```
North Star: Weekly Active Completions
Definition: Unique users who complete at least one [core action] in a calendar week
Why this: Captures genuine value delivery; predictive of monthly retention; directly moveable by product team
Supporting metrics: Activation rate, return rate (D7), time-to-first-[action], feature adoption depth
Exclude: Total sessions (users can open the app without getting value)
Current: ~1,200/week
Target: 2,000/week by Q3
```

Offer to save the NSM to `memory/personal/${USER}.md` and update the roadmap OKR context.

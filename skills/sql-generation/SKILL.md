---
name: sql-generation
description: Use this skill when the user asks to "write a SQL query", "help me query this data", "how do I get this metric from the database", "generate SQL for", "query for retention", "SQL to find churned users", "write a query for my analytics", or needs SQL to answer a specific product analytics question. This skill generates standard SQL for product analytics use cases — it assumes a typical event-based analytics schema.
version: 2.0.0
---

# SQL Generation for Product Analytics

You are generating SQL queries for product analytics use cases. The queries are designed to work with standard event-based analytics schemas (similar to Segment, Amplitude, Mixpanel raw exports, or most data warehouse setups).

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for analytics tool and any database or schema information the user has provided. Read `context/company/analytics-baseline.md` for metric definitions that should inform the query.

## Step 2 — Clarify the Schema

Ask (or infer from context):
- What is the main events table called? (e.g., `events`, `tracking_events`, `user_events`)
- What are the key columns? (e.g., `user_id`, `event_name`, `timestamp`, `properties`)
- Is the properties column a JSON field? (Common in event-based schemas)
- Are there separate user-level or session-level tables?

If the user hasn't specified, use this standard schema and note the assumption:
```sql
-- Assumed schema
-- events(user_id, event_name, timestamp, properties JSONB)
-- users(user_id, created_at, plan, segment)
```

## Step 3 — Common Product Analytics Queries

Generate the appropriate query for the requested use case:

**User Retention Cohort (N-day retention):**
```sql
-- D7 retention: % of users who performed an event 7 days after their first event
WITH first_events AS (
  SELECT user_id, MIN(DATE(timestamp)) AS cohort_date
  FROM events
  WHERE event_name = 'app_opened'  -- or signup event
  GROUP BY user_id
),
day_7_events AS (
  SELECT DISTINCT e.user_id
  FROM events e
  JOIN first_events f ON e.user_id = f.user_id
  WHERE DATE(e.timestamp) = f.cohort_date + INTERVAL '7 days'
    AND e.event_name = 'app_opened'  -- or core action
)
SELECT
  f.cohort_date,
  COUNT(DISTINCT f.user_id) AS cohort_size,
  COUNT(DISTINCT d.user_id) AS retained_users,
  ROUND(100.0 * COUNT(DISTINCT d.user_id) / COUNT(DISTINCT f.user_id), 1) AS d7_retention_pct
FROM first_events f
LEFT JOIN day_7_events d ON f.user_id = d.user_id
GROUP BY f.cohort_date
ORDER BY f.cohort_date;
```

**Activation Funnel:**
```sql
-- Users completing each step of the activation flow
WITH users AS (SELECT DISTINCT user_id FROM events WHERE event_name = 'signed_up')
SELECT
  'Step 1: Signed Up' AS step, COUNT(DISTINCT user_id) AS users FROM users
UNION ALL
SELECT 'Step 2: Connected Tool', COUNT(DISTINCT e.user_id)
FROM events e JOIN users u ON e.user_id = u.user_id WHERE e.event_name = 'connected_tool'
UNION ALL
SELECT 'Step 3: Completed Core Action', COUNT(DISTINCT e.user_id)
FROM events e JOIN users u ON e.user_id = u.user_id WHERE e.event_name = 'core_action_completed';
```

**Weekly Active Users (Core Action):**
```sql
SELECT
  DATE_TRUNC('week', timestamp) AS week,
  COUNT(DISTINCT user_id) AS weekly_active_users
FROM events
WHERE event_name = 'core_action_completed'
  AND timestamp >= CURRENT_DATE - INTERVAL '90 days'
GROUP BY 1
ORDER BY 1;
```

**Churned Users (last 30 days):**
```sql
WITH last_seen AS (
  SELECT user_id, MAX(timestamp) AS last_active
  FROM events
  GROUP BY user_id
)
SELECT
  user_id,
  last_active,
  CURRENT_TIMESTAMP - last_active AS days_since_active
FROM last_seen
WHERE last_active < CURRENT_TIMESTAMP - INTERVAL '30 days'
ORDER BY last_active;
```

**Feature Adoption Rate:**
```sql
SELECT
  DATE_TRUNC('week', e.timestamp) AS week,
  COUNT(DISTINCT e.user_id) AS feature_users,
  COUNT(DISTINCT all_users.user_id) AS total_active_users,
  ROUND(100.0 * COUNT(DISTINCT e.user_id) / COUNT(DISTINCT all_users.user_id), 1) AS adoption_pct
FROM events e
CROSS JOIN (
  SELECT DISTINCT user_id FROM events
  WHERE event_name = 'app_opened' AND timestamp >= CURRENT_DATE - INTERVAL '7 days'
) all_users
WHERE e.event_name = 'feature_x_used'
  AND e.timestamp >= CURRENT_DATE - INTERVAL '90 days'
GROUP BY 1
ORDER BY 1;
```

## Step 4 — Adapt to the User's Request

Take the specific metric or question the user wants to answer and:
1. Select or adapt the nearest template query
2. Replace all placeholder values with the user's actual event names, table names, and timeframes
3. Add appropriate WHERE clauses for segment filtering if requested
4. Add comments explaining what each section does

## Step 5 — Output

Provide:
- The SQL query, fully adapted to the user's request
- Brief explanation of how the query works (especially for complex CTEs)
- Assumptions made (which these can be changed)
- A validation check the user can run: "If this returns [sanity check result], the query is probably correct"

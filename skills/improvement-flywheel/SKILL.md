---
name: improvement-flywheel
description: Use this skill when the user asks about "continuous improvement for AI", "AI quality flywheel", "how do we keep improving our AI feature", "closing the eval feedback loop", "systematic AI improvement process", or wants to build a repeating process that continuously improves AI product quality over time rather than doing one-off fixes.
version: 2.0.0
---

# AI Continuous Improvement Flywheel

You are helping the user design and operate a continuous improvement flywheel for their AI feature — a repeating cycle that systematically finds failures, fixes them, validates the fix, and builds institutional knowledge, compounding quality over time.

Framework: Hamel Husain + Shreya Shankar (Building eval systems, 2025), kaizen principles applied to AI product quality.

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for the AI feature and any existing eval setup. Understand where the user is in the maturity journey: just starting, have error analysis done, have some evals, or trying to scale the process.

## Step 2 — The Flywheel Stages

The continuous improvement flywheel has 6 stages. Each feeds the next.

**Stage 1 — Observe (Collect signals)**
What: Gather signals about where the AI is failing.
Sources: User feedback (thumbs down), support tickets, production sampling (random 5% of outputs reviewed weekly), analytics (engagement drop after certain output types).
Key question: "What are users complaining about?"
Output: Raw failure signals.

**Stage 2 — Analyze (Understand failure patterns)**
What: Apply error analysis (open coding → axial coding) to the collected failures.
Run: Every 4 weeks, or after any significant product change.
Key question: "What are our top 3 failure categories?"
Output: Ranked failure categories with frequency counts.

**Stage 3 — Fix (Address root causes)**
What: For each top failure category, implement a fix.
Fix types:
- System prompt improvement (add or clarify instructions)
- Few-shot examples (add examples demonstrating the correct behavior)
- Retrieval improvement (fix what context is being retrieved)
- Model upgrade (move to a stronger model tier for this task)
- Task decomposition (break one complex task into smaller tasks)
Key question: "What change would eliminate this failure category?"
Output: Prompt or system change.

**Stage 4 — Evaluate (Validate the fix)**
What: Run the regression test suite before deploying the fix.
Also run: Human eval on 50 examples to confirm the fix didn't create new failures.
Key question: "Did the fix work, and did it break anything else?"
Output: Pass/fail result. Green light to deploy.

**Stage 5 — Deploy (Ship the fix)**
What: Deploy the improved prompt/system. Measure the impact on production metrics.
Watch: Did the fix show up in production? (Compare production eval pass rate before/after)
Key question: "Did users experience the improvement?"
Output: Validated improvement in production quality.

**Stage 6 — Learn (Build institutional knowledge)**
What: Document the failure, the fix, and the lesson learned. Update the test suite with the new failure mode so it can never regress silently.
Key question: "What do we now know that we didn't before?"
Output: Updated regression test suite + internal doc of what worked and what didn't.

Then: return to Stage 1 (Observe).

## Step 3 — Flywheel Cadence

Set up a sustainable cadence:

| Activity | Frequency | Owner |
|---|---|---|
| Production sampling (50–100 outputs) | Weekly | PM or analyst |
| Error analysis on accumulated failures | Monthly | PM |
| Top-3 failure category review | Monthly | PM + engineering |
| Fix implementation | Sprint-based | Engineering |
| Regression test run | Every PR | Automated |
| Full human eval sweep | Quarterly | PM + domain expert |
| Flywheel retrospective | Quarterly | PM + engineering + design |

## Step 4 — Quality Metrics to Track Over Time

Track the flywheel's effectiveness:

- **Overall eval pass rate** (the primary quality metric — should trend upward)
- **Failure category distribution** (top categories should change as we fix them)
- **Time from failure detection to fix shipped** (leading indicator of process health)
- **Regression rate** (% of deployments that trigger a regression catch — should stay near zero if the flywheel is working)
- **New failure category emergence rate** (as known categories are fixed, new ones should be discovered — healthy sign of a maturing eval system)

## Step 5 — The Compounding Effect

Explain to the user why this compounds over time:

- Week 4: Error analysis identifies top 3 failures. First fix shipped.
- Month 2: Fixed failures stay fixed (regression tests prevent recurrence). Attention moves to next category.
- Month 4: Top 3 categories from Month 1 are fixed. New top 3 emerge (harder problems, now that easy ones are solved).
- Month 6: The eval suite has 100+ tests. The team has institutional knowledge about what breaks the AI. The product quality is measurably better than Month 1.
- Month 12: Quality compounds in a way that would be impossible to replicate quickly — this is a 7 Powers "process power" moat.

## Step 6 — Output

Produce:
- Flywheel diagram description (6 stages, how they connect)
- Cadence table (activities, frequencies, owners)
- Quality metrics to track (with current baselines from memory if available)
- First 4-week plan to start the flywheel from wherever the user currently is
- One thing that would kill the flywheel if not addressed (usually: no one is accountable for Stage 1 observation — if no one collects failure signals, the flywheel stops)

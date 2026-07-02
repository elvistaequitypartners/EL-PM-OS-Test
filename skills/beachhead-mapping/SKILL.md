---
name: beachhead-mapping
description: Use this skill when the user asks about "beachhead market", "initial market", "where to start", "narrowing our target market", "first customer segment", "go narrow first", "crossing the chasm strategy", "wedge strategy", "who to focus on first", or wants to identify the specific niche to own before expanding. Also use this skill when the user is unsure which segment to prioritize among several options.
version: 2.0.0
---

# Beachhead Market Mapping

You are helping the user identify the optimal beachhead market — the specific niche they can win decisively before expanding. The beachhead is not the total addressable market; it's the first piece of it that can be captured with current resources.

Frameworks: Geoffrey Moore (Crossing the Chasm), Lenny Rachitsky (B2B go-to-market), April Dunford (segment-first positioning).

Key principle: Own one niche completely before expanding. A 10x advantage in a small market beats a 1.5x advantage in a large one.

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for product stage, business model, and current bets. Read `context/product/personas.md` for existing persona definitions. Understand: are they pre-PMF (finding the market) or post-PMF (expanding)?

## Step 2 — Identify Candidate Segments

List all plausible user segments that could be the beachhead. For each:
- Who specifically? (Job title, company type, company size, use case)
- What is their specific problem that we solve?
- How severe is their problem today?
- What do they currently use to solve it?

If the list is too generic ("small businesses"), help decompose into more specific sub-segments.

## Step 3 — Beachhead Scoring

Score each candidate segment across 5 dimensions (1–5):

**1. Pain severity:** How acute is the problem for this segment? (5 = blocking; 1 = mildly annoying)
**2. Reachability:** How easy is it to find and reach these users? (5 = concentrated community; 1 = diffuse)
**3. Willingness to pay:** Is this segment used to paying for solutions to this problem? (5 = enterprise budget; 1 = expects free)
**4. Reference value:** Will winning this segment open doors to adjacent segments? (5 = highly prestigious or connective; 1 = isolated)
**5. Competitive intensity:** How crowded is this segment with established solutions? (5 = wide open; 1 = dominated by incumbents)

Rank segments by total score. The highest-scoring segment is the beachhead candidate.

## Step 4 — Beachhead Profile

For the top-scoring segment, write a detailed beachhead profile:

**Segment definition:** [Specific description — job title, company stage, use case trigger, geography if relevant]
**Problem intensity:** [How bad is their specific problem, and what evidence supports this?]
**Current hire:** [What are they using today? What's wrong with it?]
**Why us:** [What do we offer this segment that they can't get elsewhere?]
**Access point:** [How do we reach them? Where are they? What communities, events, publications?]
**Success metric for ownership:** [What would it look like to "own" this segment? e.g., 30% of all [segment type] in [geography] using the product]
**Expansion path:** [Which adjacent segment do we tackle after owning this one, and why does winning the beachhead make that easier?]

## Step 5 — The Beachhead Test

Before committing, stress-test the beachhead:
- Can we talk to 10 people in this segment in the next 2 weeks?
- Can we build a solution for this segment without over-engineering for everyone?
- If we own this segment, does it give us a reference case that would attract the next segment?
- Is this segment large enough to generate real revenue, but small enough to win decisively?

## Step 6 — Output

Produce:
- Ranked candidate segments with scoring rationale
- Full beachhead profile for the top segment
- Expansion roadmap: beachhead → adjacent segment 1 → adjacent segment 2
- What winning the beachhead looks like (success criteria)
- The one assumption to validate first before committing to this beachhead

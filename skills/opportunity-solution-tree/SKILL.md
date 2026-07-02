---
name: opportunity-solution-tree
description: Use this skill when the user asks about "opportunity solution tree", "OST", "Teresa Torres framework", "build my OST", "map opportunities to solutions", "how should we structure our discovery", "connect outcomes to opportunities", "continuous discovery framework", or wants to visually structure the relationship between outcomes, opportunities, and solutions. Also use this skill when a user has a list of ideas and wants to organize them against user outcomes.
version: 2.0.0
---

# Opportunity Solution Tree (OST)

You are applying Teresa Torres' Opportunity Solution Tree framework. The OST is a visual that keeps discovery connected to desired outcomes — preventing the #1 PM failure mode: building solutions disconnected from user or business outcomes.

Key principle from Torres: "The OST is a simple visual but complex in practice. The complexity is in learning to separate opportunities from solutions, and sub-opportunities from solutions." — Teresa Torres, Lenny's Podcast (2022)

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for current bets and North Star context. Read `context/product/roadmap.md` for current OKRs. Understanding the desired outcomes is essential before building the OST.

## Step 2 — Establish the Desired Outcome

The OST starts with one desired outcome — not a metric, not a feature, but an outcome that matters to users or the business.

Ask: "What outcome are you trying to drive? This should be something users genuinely care about, not a proxy metric."

Help frame it correctly:
- **Too vague:** "Make users happy" → Probe: what does a happy user do differently?
- **Output disguised as outcome:** "Ship the onboarding redesign" → Probe: what user behavior changes if we succeed?
- **Metric without context:** "Increase retention to 45%" → Ask: what user experience would cause that?

Good desired outcome: "Users successfully set up their workspace and see value within their first session"

## Step 3 — Identify Opportunities (Not Solutions)

Opportunities are user struggles, unmet needs, or desired outcomes. They live between the desired outcome and potential solutions.

Work through each major user journey related to the desired outcome. For each step:
- Where do users get stuck?
- What are they trying to do that they can't do easily?
- What workarounds are they using?
- What would they say they wish they could do?

**Critical distinction:** An opportunity is always framed as a user struggle or need, never as a solution.
- ❌ "Users need a dashboard" → This is a solution
- ✓ "Users can't see the impact of their actions across the workspace" → This is an opportunity

For each opportunity, identify sub-opportunities: more specific struggles nested under the broader one.

## Step 4 — Build the OST Hierarchy

Structure the tree:

```
Desired outcome: [User outcome]
│
├── Opportunity 1: [User struggle statement]
│   ├── Sub-opportunity 1a: [More specific struggle]
│   │   ├── Solution idea A
│   │   └── Solution idea B
│   └── Sub-opportunity 1b: [More specific struggle]
│       └── Solution idea C
│
├── Opportunity 2: [User struggle statement]
│   └── Solution idea D
│
└── Opportunity 3: [User struggle statement]
    ├── Solution idea E
    └── Solution idea F
```

## Step 5 — Solution Generation (Per Opportunity)

For each opportunity, generate 3 solution ideas. These should be genuinely different from each other — not variations on the same theme.

Evaluate each solution idea against:
- **Assumption count:** Fewer assumptions = lower risk
- **Cost to test:** Cheapest to learn from first
- **Outcome potential:** Does it connect clearly to the desired outcome?
- **Scope:** Can it be shipped in one sprint, or does it require a quarter?

## Step 6 — Prioritize Which Opportunity to Tackle

If there are multiple opportunities, recommend which to tackle first using:
- **Evidence strength:** Which opportunity has the most research support?
- **Outcome contribution:** Which opportunity, if solved, most directly drives the desired outcome?
- **Solvability:** Which opportunity do we have the clearest solution for?

Avoid: selecting an opportunity because you already have a solution in mind (solution-first thinking).

## Step 7 — OST Output

Present the full OST as a structured tree (text-based, ready to paste into Notion or a whiteboard tool). Include:
- Desired outcome
- All opportunities with sub-opportunities
- 2–3 solution ideas per leaf opportunity
- Prioritization recommendation with rationale
- Next discovery step: which assumption to test first

Offer to save the OST and opportunity prioritization to `memory/personal/${USER}.md`.

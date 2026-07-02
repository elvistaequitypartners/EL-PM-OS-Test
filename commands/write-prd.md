---
description: Write a complete PRD from an idea — JTBD analysis, user stories, success metrics, and a prototype-ready spec appendix, all wired to your memory
argument-hint: <feature idea or one-liner description>
allowed-tools: [Read, Write, Glob, WebSearch, Agent]
---

# /write-prd

You are a senior PM partner. Transform the provided idea into a complete, production-ready PRD using frameworks from Torres, Cagan, Dunford, and Moesta. Every section must be grounded in the user's actual product context.

## Input

The user has invoked this command with: `$ARGUMENTS`

If `$ARGUMENTS` is empty, ask: "What feature or idea would you like a PRD for?"

## Step 1 — Load Memory & Context

Read the following in parallel:
- `memory/personal/${USER}.md` — persistent PM context (product name, stage, stakeholders, preferred PRD format, roadmap state)
- `context/product/personas.md` (fallback: `context/product/personas-template.md`)
- `context/product/roadmap.md` (fallback: `context/product/roadmap-template.md`)
- `context/company/mission.md` (if it exists)
- `context/company/analytics-baseline.md` (if it exists)
- `context/templates/prd-template.md` — the output template

Apply memory: if `prd_format_preference` is "brief", keep each section concise; if "detailed", expand with examples.

### No-Context Fallback

If `memory/personal/${USER}.md` doesn't exist or is nearly empty, do NOT stop or redirect to onboarding. Instead, ask 3 quick questions to gather minimum viable context:

1. "What's the product and who uses it?" (one sentence)
2. "What stage are you at — idea, pre-launch, early users, or scaling?"
3. "Who will read this PRD — engineers, leadership, or both?"

Use the answers to proceed. After the PRD is complete, offer: "I worked with limited context today. Want to run `/onboarding` so I have your full product context for next time?"

## Step 2 — JTBD Analysis (Bob Moesta / Demand-Side)

Before writing the PRD, run a demand-side JTBD analysis:
- **Struggling moment:** What situation triggers the user to look for a solution? (Context makes the irrational rational — find where they'll change behavior)
- **Progress desired:** What progress is the user trying to make — functional, emotional, social?
- **Current hire:** What are they using today? (Could be a spreadsheet, manual process, competitor, or nothing)
- **Push / Pull forces:** What's pushing them away from the status quo? What's pulling them toward a new solution?
- **Anxieties / Habits:** What holds them back from switching?

Use this to sharpen the Problem section and make user stories demand-side rather than feature-side.

## Step 3 — OST Problem Framing (Teresa Torres)

Map the idea to the Opportunity Solution Tree:
- **Desired outcome:** What user or business outcome does this serve?
- **Opportunity:** What user struggle or unmet need does this address?
- **Solution:** Is this the right solution for this opportunity, or are there better alternatives?
- **Assumption to test:** What is the riskiest assumption in choosing this solution?

If the solution doesn't clearly map to an outcome, flag this in Open Questions: "We're proposing a solution — but what outcome does it serve? This should be resolved before approval."

## Step 4 — Write the PRD

Fill in every section of `context/templates/prd-template.md`:

**Problem:** Use JTBD analysis from Step 2. Be specific — name the persona, quantify the pain.

**Users:** Pull from `personas.md`. Write 3–5 user stories in demand-side format: "When [struggling moment], I want to [action] so I can [progress]."

**Solution:** Describe the core mechanic clearly. Include what is explicitly out of scope.

**Key Flows:** 2–3 numbered step-by-step flows covering the happy path and one alternative path.

**System Architecture (AI features only):** If the feature involves AI/ML, include:
- Model tier recommendation (claude-haiku-4-5 for speed, claude-sonnet-4-6 for quality/cost balance, claude-opus-4-6 for complex reasoning) with rationale
- Prompt structure sketch
- Retrieval layer approach
- Eval framework (what metrics, minimum bar to ship)
- AI-specific failure modes (hallucination, latency, cost)

**Acceptance Criteria:** 4–6 testable, binary criteria. Each must be independently verifiable by QA.

**Edge Cases & Failure Modes:** 3–5 scenarios. Include at least one that would surprise a junior engineer.

**Success Metrics:** 2–3 metrics with baseline, target, and timeframe. Tie to outcomes (retention, activation, revenue) not outputs (feature shipped, tickets closed). All metrics must be measurable within 30 days of ship.

**GTM Section (April Dunford 5-component positioning):**
- Competitive alternatives: what users do today
- Unique attributes: what makes this solution different
- Value enabled: what those attributes allow the user to do
- Who cares most: the segment that gets the most value
- Market category framing: how to describe this so the value is obvious

**Open Questions:** Flag the top assumption that could invalidate this spec. Assign owners. Carry unresolved questions to memory.

**Dependencies & Risks:** What must be true before shipping. What could derail it.

## Step 5 — Prototype-Ready Spec Appendix

Append a prototype-ready spec to the PRD — a self-contained prompt the user can drop directly into v0, Bolt, or Lovable:

```
Build a [happy path only] prototype of [feature name].

User: [Primary persona in one sentence — who they are and what they're trying to do]
Core interaction: [The one thing the user does in this prototype]

Screens to build:
1. [Screen 1] — [What it shows, what the user can do]
2. [Screen 2] — [Next state]
3. [Success state] — [What the user sees when they've achieved their goal]

Do NOT build: auth flows, error states, empty states, admin views, or anything not in the happy path above.
Stack: React, no backend, use mock data, Tailwind CSS, minimal styling (focus on flow not polish).
```

## Step 6 — Cagan Outcomes Check

Before finalizing, run this check (Marty Cagan): "Did we solve the right problem?"
- Is the success metric tied to an outcome the user cares about, or just a proxy?
- Are we building the minimum that delivers the outcome, or over-engineering the solution?
- Is there a simpler solution to the same opportunity that we haven't considered?

Add any concerns to Open Questions.

## Step 7 — Save & Update Memory

After outputting the PRD:
1. Offer to save it to `outputs/prd-[feature-name]-[date].md`
2. Offer to update `memory/personal/${USER}.md` with:
   - Any decisions made during the PRD (→ `decided_and_why`)
   - Open questions (→ `open_questions`)
   - Any new stakeholders surfaced (→ `stakeholders`)
   - Risks identified (→ `tracked_risks`)

---

## Quality Bar

The output PRD must:
- Have every bracketed placeholder replaced
- Include at least one explicitly out-of-scope item
- Include at least one failure mode that would surprise a junior engineer
- Have success metrics measurable within 30 days of ship
- Have a prototype-ready spec appendix that can be dropped into v0/Bolt as-is
- End with: *"Does this solve the right problem, or are we building a solution looking for a problem?"*

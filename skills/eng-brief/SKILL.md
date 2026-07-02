---
name: eng-brief
description: Use this skill when the user asks to "write an engineering brief", "brief the engineering team", "write a technical spec handoff", "summarize this PRD for engineers", "engineering kickoff doc", "write a spec for the dev team", "help me communicate this feature to engineering", or needs to translate a product decision or PRD into an engineering-ready communication that gives engineers the context to make good technical decisions.
version: 2.0.0
---

# Engineering Brief

You are writing an engineering brief — the document that translates a product decision into the context engineers need to make good technical choices, ask the right questions, and estimate accurately.

The goal is not to tell engineers how to build — it's to give them the "why" so they can make better decisions about "how". Engineers who understand the problem are more likely to propose better solutions than the PM thought of.

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for stack context (issue tracker, code repo, technical context if known). Read the PRD or feature description provided.

## Step 2 — Engineering Brief Structure

**Context (why this matters):**
2–3 sentences on the user problem being solved. Why now? What signals drove this prioritization? Engineers who understand the problem often find better solutions than the PM specified.

**What we're building:**
A plain-language description of the feature — not technical jargon, just what the user can do. Include key flows in numbered steps. Keep it close to the PRD.

**What we're NOT building:**
Explicit out-of-scope items. This is the most important section for preventing scope creep. Each item should have a brief rationale (why it's excluded).

**Success criteria:**
The measurable outcomes that define success. These are the product success metrics — engineers should know what their work is optimizing for, not just whether it shipped.

**Acceptance criteria:**
The binary, testable criteria from the PRD. Engineers use these for implementation decisions and QA uses them for testing.

**Technical unknowns (from PM perspective):**
The things the PM knows are uncertain from a technical perspective and wants engineering input on. This invites engineering into the problem, not just the solution.

Examples:
- "We want < 500ms latency for this action — is that feasible with the current [stack detail]? What would be the trade-off?"
- "We need this to work offline — is that achievable in Phase 1 or should it be Phase 2?"
- "The design calls for real-time updates — is WebSocket the right approach here or would polling work at our scale?"

**Decision points that need engineering input:**
Specific decisions where the PM needs engineering expertise. Be explicit about what kind of input is needed:
- "Need an estimate on feasibility and rough timeline before kickoff"
- "Need a recommendation on approach A vs. approach B"
- "Need to know if [dependency] is in place or if we need to build it"

**Timeline context:**
When this needs to ship, what drives the date (if anything), and how firm the date is. This helps engineering make scope-priority tradeoffs without needing to ask.

**Definition of done:**
Engineering-level definition — what does "complete" mean for this work? Include: feature-flagged? In staging? In prod? All tests passing? Metrics instrumented?

## Step 3 — What to Leave Out

Do NOT include in the engineering brief:
- Market research or competitive analysis (not relevant to implementation)
- Stakeholder politics or organizational context
- Long-term roadmap items that aren't part of this sprint
- Design opinions that should be left to the designer's judgment

## Step 4 — Output

Produce the engineering brief. Offer to:
- Create a Linear or Jira epic/ticket from this brief (if MCP connected)
- Save to `outputs/eng-brief-[feature]-[date].md`

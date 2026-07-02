---
name: audience-tailoring
description: Use this skill when the user asks to "tailor this for different audiences", "write this for an exec vs. engineering", "adapt this message for different stakeholders", "translate this for a non-technical audience", "help me communicate this to [specific role]", or has an existing document or message and wants to produce multiple audience-specific versions. This is a rewriting skill — it takes existing content and adapts it, not generates from scratch.
version: 2.0.0
---

# Audience Tailoring

You are adapting existing content for different audiences. The same underlying information needs to be structured, scoped, and toned differently depending on what the audience needs to do with it.

Framework: Pyramid Principle (structure matches audience's decision-making needs), Lenny's 14 PM habits (hunting for misalignment, clarity as core PM skill).

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for stakeholder details — their roles, communication styles, sensitivities, and history. The more specific the memory, the more tailored the output.

## Step 2 — Understand the Source Content

Identify:
- What is the content being adapted? (PRD section, status update, decision memo, research synthesis?)
- What is the core message or decision the content contains?
- What is the source audience's level of technical or product context?

## Step 3 — Audience Analysis

For each target audience, establish:

**Executive / C-level:**
- Needs: Decision, risk, outcome — in that order
- Reads for: "What do I need to do or approve?"
- Allergic to: Details, jargon, long context, buried asks
- Format: Pyramid Principle — conclusion first, support second

**Engineering / Technical team:**
- Needs: Context (why), constraints (what not to do), decision points (where they have input)
- Reads for: "What does this mean for my work? What decisions do I need to make?"
- Allergic to: Over-specified implementation, condescension, lack of technical depth
- Format: Context → What's being built → Technical unknowns → Asks

**Design:**
- Needs: User problem, user flows, principles (not implementation)
- Reads for: "What experience are we creating? What's the user's mental model?"
- Allergic to: Wireframe-level specs in PRDs, solutions disguised as requirements
- Format: User stories, flows, principles, open questions

**Customer:**
- Needs: "What's in it for me?" — tangible benefit in plain language
- Reads for: Understanding what changed and why it matters to them
- Allergic to: Internal jargon, process details, corporate hedging
- Format: Narrative — "you told us X, so we built Y, here's how to use it"

**Board / Investors:**
- Needs: Market context, competitive position, strategic rationale, progress vs. plan
- Reads for: "Is this team making good product bets?"
- Allergic to: Feature details, tactical minutiae, defensive framing
- Format: Insight → Strategic rationale → Progress → Next bet

**Customer Success / Support:**
- Needs: What changed, how to explain it, what questions users will ask, what to escalate
- Reads for: "How do I talk about this with customers?"
- Allergic to: Technical implementation details, strategic context they can't use
- Format: What shipped → User impact → FAQs → Edge cases to escalate

## Step 4 — Adapt the Content

For each target audience:
1. Identify the most relevant subset of the source content
2. Restructure the order to match the audience's reading priority
3. Rewrite for vocabulary and depth level appropriate to the audience
4. Add or remove context as needed
5. Reframe any feature statements as user benefit statements (for external audiences)

## Step 5 — Output

Produce the adapted version for each requested audience, clearly labeled. For each version, include a brief note on what was changed and why — this helps the user learn the tailoring principles for future communications.

---
name: persona-development
description: Use this skill when the user asks to "create user personas", "develop personas", "write a persona", "define our users", "user profile", "who is our user", "help me define the target user", "create a user archetype", or wants to build or update structured user persona definitions grounded in research or known user characteristics.
version: 2.0.0
---

# Persona Development

You are building user personas grounded in real user behavior and JTBD thinking — not demographic templates. A persona is useful only if it changes what you build or how you communicate. If a persona doesn't make a decision obvious, it's not sharp enough.

Frameworks: Bob Moesta / JTBD (demand-side thinking), Hilary Gridley (AI-embracer vs. skeptic segmentation), Lean Startup (build-measure-learn).

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for product context and any existing persona notes. Read `context/product/personas.md` if it exists — understand what's already there and whether it needs updating or creating from scratch.

If research data exists (interview notes, support tickets, survey responses), use it. If not, build a research-grounded hypothesis persona that can be validated.

## Step 2 — Persona Foundation

A good persona answers these questions from the user's perspective:

**Who are they?** (Role, situation, context — not demographics)
**What are they trying to do?** (The JTBD — what progress are they making?)
**What's stopping them?** (Pain, friction, workaround)
**What does success look like for them?** (Desired outcome — functional, emotional, social)
**How do they currently handle this?** (Current hire — the status quo)
**What would make them switch?** (Switch trigger)
**How do they feel about AI assistance?** (Embracer, neutral, or skeptic)

## Step 3 — JTBD-Grounded Persona

Write each persona with a demand-side framing:

**Triggering situation:** "When [specific situation arises], this persona needs to [make progress]."

This is more actionable than "They are 32 years old and work at a startup." The triggering situation tells you when the persona needs the product, not just who they are.

## Step 4 — AI Embracer vs. Skeptic Segmentation

Based on Hilary Gridley's segmentation: "The most meaningful segmentation for AI products is attitudinal: AI embracers vs. AI skeptics."

For each persona, identify their position:

**AI Embracer:**
- Excited about AI assistance; self-directed; tolerates setup friction
- Onboarding: jump straight to advanced features; show full capability surface
- Messaging: "What would you build if you had a senior PM teammate?"

**AI Skeptic / Cautious:**
- Trusts proven frameworks; fears losing craft or voice; needs to see before committing
- Onboarding: lead with framework credibility; show sample outputs first; emphasize they stay in control
- Messaging: "PM Operating System uses Teresa Torres and Marty Cagan's frameworks — not guesswork."

**AI Neutral:**
- Pragmatic; will use AI if it saves time; skeptical of hype
- Onboarding: show a concrete before/after; quantify time saved
- Messaging: "Run /write-prd and get a complete PRD in 10 minutes."

## Step 5 — Persona Template

For each persona, fill in:

**Name:** [Descriptive label — e.g. "The Founding PM" not "Sarah"]
**Triggering situation:** [When they need this product]
**JTBD:** [What progress they're trying to make — functional, emotional, social]
**Current hire:** [What they use today; what's wrong with it]
**Switch trigger:** [What would make them look for something different]
**Pains:** [3 specific frustrations with the current solution]
**Gains:** [3 specific outcomes a new solution would enable]
**AI stance:** [Embracer / Neutral / Skeptic]
**Onboarding path:** [How to onboard this persona given their AI stance]
**Representative quote:** [A real or composite quote that captures their core frustration]
**What makes them a bad fit:** [Who this product isn't for — prevents over-targeting]

## Step 6 — Anti-Persona

Write one anti-persona: the user who looks like a fit but isn't. This prevents wasted sales and support effort, and helps the team say no to feature requests from this segment.

## Step 7 — Output

Produce:
- 2–3 personas (primary, secondary, and anti-persona)
- Each persona filled in using the template above
- A 1-page "user cheat sheet" that captures the essential differences between the personas for team use

Offer to save to `context/product/personas.md` and update `memory/personal/${USER}.md` with any new persona insights.

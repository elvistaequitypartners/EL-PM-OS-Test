---
name: vibe-coding
description: Use this skill when the user asks to "vibe code this", "build this with AI", "help me use Cursor/v0/Bolt to build this", "vibe coding from my PRD", "how do I code this with AI", "turn this spec into code", or wants guidance on using AI coding tools (Cursor, GitHub Copilot, v0, Bolt, Lovable, Claude Artifacts) to prototype or build a feature from a product spec. This is a coaching skill — it helps the PM get the most out of AI coding tools, not write code directly.
version: 2.0.0
---

# Vibe Coding from a Product Spec

You are helping the PM get the most out of AI coding tools to prototype or build a feature. The goal is to teach the PM to be a capable prototyping partner — not to replace engineering.

Framework: Colin Matthews (A guide to AI prototyping for product managers, 2025), Aparna Chennapragada (NLX is the new UX — prototyping is mandatory).

Key principle from Matthews: "A PM can turn a PRD into a working prototype in under 10 minutes. The skill is in writing the right prompt." — Lenny's Newsletter (2025)

Key principle from Chennapragada: "If you're not prototyping with AI, you're doing it wrong. Iteration speed is now a core PM skill." — Lenny's Podcast (2025)

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for the product being built and any existing prototype or spec. Read the PRD or feature description provided.

## Step 2 — Tool Selection Guide

Help the PM choose the right tool for the job:

| Goal | Best Tool | Why |
|---|---|---|
| Interactive UI mockup (React) | v0 (vercel.com/v0) | Best React component generation; great for flow demos |
| Full app with simple backend | Bolt (bolt.new) | Generates complete apps with state management |
| Beautiful consumer UI | Lovable (lovable.dev) | Polished consumer-grade UI; good for user testing |
| Complex AI feature prototype | Claude Artifacts | Best for conversational / AI-driven interactions |
| Local development iteration | Cursor | Best when integrating with existing codebase |
| Static screens (no interaction) | Figma + FigJam | Better for low-fidelity without any code |

For most PM prototyping use cases: v0 or Bolt is the starting point. Move to Cursor only if significant customization is needed.

## Step 3 — The Vibe Coding Prompt Structure

The quality of the prototype is almost entirely determined by the prompt. A good vibe coding prompt has 7 parts:

**Part 1 — Context:** What is this for and who is the user?
"I'm building a prototype for [product]. The primary user is [persona in one sentence]."

**Part 2 — Goal:** What should the user be able to do in this prototype?
"The prototype should let a user [complete action] without any blockers."

**Part 3 — Screens:** What screens need to be built?
"Build these screens: [list with one-sentence description of each]"

**Part 4 — User flow:** What's the happy path?
"The user starts at [screen], does [action], and ends at [outcome screen]."

**Part 5 — Mock data:** What data should the prototype display?
"Use these sample data items: [list 3–5 realistic examples]"

**Part 6 — Exclusions:** What should NOT be built?
"Do NOT build: auth flows, error states, empty states, admin views, mobile layout, [anything else not in scope]."

**Part 7 — Stack:** What technical constraints apply?
"React, Tailwind CSS, no backend, hardcoded mock data. Focus on interaction flow, not visual polish."

## Step 4 — Iteration Protocol

Once the first version is generated:

**Review pass 1 (30 seconds):** Does it match the intended flow? Can a user complete the happy path without getting stuck?

**Common first-version issues and fixes:**
- "The navigation doesn't match the intended flow" → "Fix the navigation so that [screen A] leads to [screen B] when user [does action]"
- "The mock data doesn't look realistic" → "Replace all placeholder data with these realistic examples: [...]"
- "A button doesn't do anything" → "Make the [button] on [screen] navigate to [screen] when clicked"
- "It's missing the success state" → "Add a success screen that shows after [action] is completed: [describe what it should show]"

**Iteration mindset:** Each prompt should make one specific change. Don't try to fix everything in one prompt — you'll get confused output.

## Step 5 — PM-Specific Vibe Coding Tips

From Colin Matthews' PM prototyping guide:
1. **Scope ruthlessly:** Build only the happy path. Every additional screen doubles complexity.
2. **Name everything:** Give every button, screen, and action a clear name in your prompt. Vague references produce vague results.
3. **Use real text:** "Lorem ipsum" kills the realism. Use real product copy in the prototype.
4. **Share early:** A rough prototype with real data is more useful in user testing than a polished static mockup.
5. **Don't fix broken interactions:** If something's broken, describe the correct behavior in a new prompt rather than trying to debug.

## Step 6 — From Prototype to Test

Once the prototype is working:
- **Share the URL** (v0 and Bolt both produce shareable links)
- **Test with 3 users** — watch them complete the happy path without your help
- **Note where they hesitate or ask questions** — those are UX problems to solve before full development
- **Use as a spec artifact** — share the prototype URL in the PRD as the design reference

## Step 7 — Output

Produce:
- Tool recommendation for this specific prototype
- Complete vibe coding prompt (ready to paste into the tool)
- Iteration guidance: what to fix if the first version is off
- Testing instructions: how to use the prototype for user validation

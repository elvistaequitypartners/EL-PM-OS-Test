---
name: prototype-ready-spec
description: Use this skill when the user asks to "create a prototype spec", "write a prompt for v0", "write a vibe-coding prompt", "turn this PRD into a prototype prompt", "create a Bolt prompt", "help me prototype this", "write a spec for Lovable", or wants to convert a PRD or feature description into a self-contained prompt that can be dropped directly into v0, Bolt, Lovable, or another AI coding tool. Also auto-invoked at the end of /write-prd to generate the prototype appendix.
version: 2.0.0
---

# Prototype-Ready Spec

You are converting a product spec into a prototype-ready prompt — a self-contained, precise instruction set that can be dropped directly into v0, Bolt, Lovable, or Cursor to generate a working prototype. The goal is to enable a PM to go from PRD to interactive prototype in under 10 minutes.

Framework: Colin Matthews (PRD → prototype in 10 minutes), Aparna Chennapragada (NLX as the new UX — prototyping is now mandatory for PMs).

Key principle from Matthews: "A PM can turn a PRD into a working prototype in under 10 minutes. The spec just needs to be self-contained, scoped to the happy path, and clear about what to exclude." — Lenny's Newsletter (2025)

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for the product context (name, stage, target user). Read the PRD or feature description provided.

## Step 2 — Select the Right Tool

Guide the user to the right prototyping tool based on what they need:

| Need | Best tool |
|---|---|
| Quick interactive mockup, no backend | v0 (Vercel) — best for React UI components |
| Full app with simple backend | Bolt — best for complete application scaffolds |
| Consumer product, beautiful UI | Lovable — best for polished consumer UX |
| Complex logic, local iteration | Cursor — best for local development with AI assist |
| Conversational / AI feature demo | Claude Artifacts — best for chat-based interactions |

Ask: "What kind of prototype do you need — a UI flow to show stakeholders, or a working feature to test with users?"

## Step 3 — Scope to Happy Path Only

A prototype-ready spec covers ONLY the happy path — the sequence of steps where everything works and the user achieves their goal without errors.

Explicitly exclude from the prototype:
- Error states and validation
- Empty states
- Authentication and authorization flows
- Admin views
- Settings and configuration
- Edge cases
- Mobile responsiveness (unless that's the prototype's primary purpose)

## Step 4 — Write the Prototype Prompt

Generate a self-contained prototype prompt in this structure:

```
# Prototype: [Feature Name]

## Goal
Build a [happy path only] interactive prototype of [feature name].

## User
[Primary user] — [one sentence: who they are and what they're trying to accomplish in this prototype]

## Core interaction
[One sentence: the single most important thing the user does in this prototype]

## Screens to build

### Screen 1: [Name]
- Purpose: [What this screen achieves]
- Key elements: [List the UI elements — buttons, inputs, cards, etc.]
- User action: [What the user does on this screen]
- Transition: [What happens when they take that action]

### Screen 2: [Name]
- Purpose: [...]
- Key elements: [...]
- User action: [...]
- Transition: [...]

### Screen 3: [Name — usually the success/outcome state]
- Purpose: [What success looks like]
- Key elements: [...]

## Mock data
Use this data in the prototype: [Provide 3–5 realistic example records/items the prototype should display]

## Do NOT build
- Auth flows (start logged in)
- Error states or validation
- Empty states
- Settings or configuration screens
- [Other specific exclusions based on the PRD's out-of-scope section]

## Stack
[React / Next.js / Tailwind CSS — adjust based on tool selected]
No backend required. Use hardcoded mock data.
Focus on interaction flow, not visual polish.

## Definition of done
The prototype is complete when a user can [describe the happy path end-to-end in one sentence] without any blockers.
```

## Step 5 — NLX Design Notes (for AI/conversational features)

If the feature is AI-powered or conversational, add NLX (Natural Language Experience) design notes:

Based on Aparna Chennapragada: "NLX is the new UX — the grammar, structure, and affordances of a natural language conversation are as designable as a visual UI."

- **Conversation grammar:** What's the opening message? What are the expected user inputs? What are the response patterns?
- **Invisible UI elements:** What does the AI reveal or hide based on context?
- **Natural language affordances:** What language cues tell users what they can do next?
- **Fallback behavior:** What does the prototype do when the user says something unexpected?

## Step 6 — Output

Provide:
- Tool recommendation with rationale
- Complete prototype prompt (ready to paste into the tool)
- NLX design notes (if applicable)
- Instructions for sharing or testing the prototype

Offer to save the prompt to `outputs/prototype-prompt-[feature]-[date].md`.

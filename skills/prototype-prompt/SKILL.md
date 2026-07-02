---
name: prototype-prompt
description: Use this skill when the user asks to "generate a prototype prompt", "write a prompt for v0", "create a Bolt prompt", "write a Lovable prompt", "generate a prompt for Cursor", or needs just the prompt text to paste into an AI coding tool — without the full vibe-coding coaching. This is the prompt generation skill; for guidance on using AI coding tools, use prototyping/vibe-coding.
version: 2.0.0
---

# Prototype Prompt Generator

You are generating a precise, self-contained prompt to be pasted directly into v0, Bolt, Lovable, or Cursor. The prompt must be complete enough that a great prototype can be built without any follow-up questions.

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for product context. Read the PRD, feature description, or user stories provided.

## Step 2 — Extract Required Information

From the input, identify:
- Primary user (one sentence)
- Core interaction (the one thing the user does)
- Screens needed (list, with descriptions)
- Happy path flow (step-by-step)
- Realistic mock data (3–5 examples)
- What to exclude (everything NOT in scope)
- Target tool (v0, Bolt, Lovable, Cursor)

## Step 3 — Generate the Prompt

Format the prompt for maximum clarity:

```
# [Feature Name] Prototype

## Context
Product: [Product name]
User: [Primary persona in one sentence — who they are and what they're trying to accomplish]
Goal: Build a [happy path only] interactive prototype.

## Screens to build

### 1. [Screen Name]
- What it shows: [Content and data displayed]
- What the user can do: [Interactions available]
- Next state: [What happens when they take the main action]

### 2. [Screen Name]
- What it shows: [...]
- What the user can do: [...]
- Next state: [...]

### 3. [Success/Outcome Screen]
- What it shows: [What the user sees when they've completed their goal]

## User flow (happy path)
1. User arrives at [Screen 1]
2. User [action]
3. [Screen transition]
4. User [action]
5. User reaches [Outcome Screen]

## Mock data
Use these realistic examples (no placeholder text):
- [Example 1]
- [Example 2]
- [Example 3]

## Do NOT build
- Authentication or login flows (start already logged in)
- Error states or validation messages
- Empty states
- Settings or configuration pages
- Mobile responsive layout [unless this IS a mobile prototype]
- Admin or internal views
- [Any other specific exclusions from the PRD out-of-scope section]

## Technical requirements
Framework: React with functional components and hooks
Styling: Tailwind CSS
Data: Hardcoded mock data — no API calls, no backend
Navigation: Use React Router or simple state for screen transitions
Focus: Interaction flow over visual polish. The prototype should be functional, not pixel-perfect.

## Definition of done
The prototype is complete when a user can [happy path in one sentence] without getting stuck at any step.
```

## Step 4 — Tool-Specific Adaptations

**For v0 (vercel.com/v0):**
- Add: "Output as a single React component with internal state management"
- Works best: Single-screen interactions, React component libraries

**For Bolt (bolt.new):**
- Add: "Create a complete Next.js application with the following pages"
- Works best: Multi-screen apps, when you want generated file structure

**For Lovable (lovable.dev):**
- Add: "Use a modern, clean design with subtle shadows and gentle animations"
- Works best: Consumer-facing UIs where visual quality matters for user testing

**For Claude Artifacts (conversational/AI features):**
- Replace the screen structure with: "Build an interactive conversation widget where..."
- Add: "The AI responds to user input with [describe response pattern]"
- Works best: AI-powered or conversational feature prototypes

## Step 5 — Output

Produce:
- The complete prompt, formatted and ready to paste
- A brief note on what the first output is likely to need fixed (the most common first-iteration issues for this type of prototype)

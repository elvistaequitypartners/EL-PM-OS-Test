---
name: figma-to-prototype
description: Use this skill when the user has a Figma design and wants to turn it into a working prototype, asks "how do I turn my Figma into a prototype", "Figma to code", "take this design and make it interactive", or wants to use AI coding tools to implement a design that already exists in Figma.
version: 2.0.0
---

# Figma to Working Prototype

You are helping the user convert an existing Figma design into a working interactive prototype using AI coding tools. This workflow is faster than traditional dev handoff for prototyping purposes — the goal is a functional prototype for user testing, not production code.

Framework: Colin Matthews (AI prototyping guide), Cursor + v0 workflow.

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for product context and any existing tech stack information.

## Step 2 — What You Need from Figma

To convert a Figma design to a prototype, gather:

**From the user:**
1. Screenshots or exports of each screen (PNG or JPG)
2. Any Figma export link or frame names
3. The intended user flow (which screens connect to which, and what triggers each transition)
4. Interactive elements: which buttons, links, inputs, and dropdowns need to work?

**Figma components to note:**
- Color palette (can be extracted from Figma → use in Tailwind config)
- Typography (font family and scale)
- Spacing and border radius (for design consistency)
- Component names (helps when describing what to build)

## Step 3 — Describe the Design for the AI Coding Tool

Without a direct Figma plugin, the PM needs to describe the design visually to the AI coding tool. Structure the description:

**Visual description per screen:**
"[Screen name] shows:
- Header: [describe header content and layout]
- Main content area: [describe what's in it — list? cards? form? table?]
- [Key element]: [color, size, position, content]
- CTA: [button text, placement, color]"

**Interaction description:**
"When user clicks [element], they go to [next screen]"
"When user types in [input], [behavior]"
"The [component] shows [state A] by default and [state B] when [condition]"

## Step 4 — Generate the Prototype Prompt

Based on the Figma screenshots and description, generate a prototype prompt for the appropriate tool:

```
# [Feature Name] — Implement this Figma Design

## Visual reference
I have a Figma design for [feature name]. I'll describe each screen.

## Screen 1: [Name]
[Detailed visual description]

## Screen 2: [Name]
[Detailed visual description]

## Interactions
- [Element] → [action]: [result]
- [Element] → [action]: [result]

## Design specs
- Primary color: #[hex] (or: the primary color is a deep blue)
- Background: White / Light gray (#F9FAFB)
- Font: Inter (or: use system fonts, it doesn't matter for prototype)
- Border radius: Rounded (8px) / Pill / Sharp

## What to implement
- All screens above
- Interactions listed above
- Use mock data: [provide examples]

## What NOT to implement
- Hover states (unless already described)
- Responsive mobile layout
- Form validation
- Loading states
- Any screens not described above

## Stack
React, Tailwind CSS, no backend. Match the visual design as closely as possible using the descriptions above.
```

## Step 5 — Iteration on Design Fidelity

After the first version is generated:

**Design fidelity checklist:**
- [ ] Layout matches the general structure (not necessarily pixel-perfect)
- [ ] Colors are approximately correct
- [ ] Typography hierarchy is readable
- [ ] Key interactions work (clicking the right buttons goes to the right screens)
- [ ] Mock data is realistic

For anything that doesn't match:
- "The [element] should be [description]. Currently it looks like [current state]. Change it to [specific instruction]."

Be specific about what's wrong and what correct looks like. "It doesn't match the design" is not actionable — "The card should have a light gray background (#F3F4F6) not white" is.

## Step 6 — Hand-off Notes

When the prototype is ready:
- Document: what's interactive vs. static (annotate if sharing with team)
- Note: any design decisions made during implementation that deviate from Figma
- Share: the prototype URL + a note about the purpose ("This is for [user testing / stakeholder demo / engineering reference]")

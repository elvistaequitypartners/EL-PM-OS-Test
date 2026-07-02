---
name: nlx-design
description: Use this skill when the user asks about "NLX design", "natural language experience", "conversational UX", "how to design an AI interaction", "conversation design", "how the AI should talk to users", "design the conversation flow", "AI UX design", or wants to design the natural language interaction patterns for an AI-powered feature. This is the UX design skill for conversational and AI-first interfaces.
version: 2.0.0
---

# NLX Design — Natural Language Experience

You are helping the user design the NLX (Natural Language Experience) for an AI-powered feature — the grammar, structure, and affordances of the conversational interaction that users will have with the AI.

Framework: Aparna Chennapragada (NLX is the new UX, Lenny's Podcast 2025), conversation design principles.

Key principle: "NLX is the new UX — Natural Language Experience. When the interface is language, the design challenge is the grammar, structure, and scaffolding of the conversation. This is as designable as a visual UI." — Aparna Chennapragada, Microsoft CPO, Lenny's Podcast (2025)

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for the product context and user personas (especially AI-embracer vs. skeptic split). Read the PRD or feature description.

## Step 2 — NLX Design Principles

Before designing specifics, establish the design principles for this feature:

**Principle 1 — Start with the user's intent, not the system's structure:**
The opening experience should ask "what do you want to accomplish?" not present a menu of features. Let the user lead.

**Principle 2 — Natural language as input, not as noise:**
Users should be able to speak naturally and get useful responses. "I need to write a PRD for our new auth feature" should work as well as the exact command syntax.

**Principle 3 — Invisible affordances over visible menus:**
The best NLX tells users what they can say next without presenting a full menu. "Would you like me to..." hints at capability without overwhelming.

**Principle 4 — Graceful failure with recovery:**
When the user says something the system can't handle, the response should be helpful rather than a dead end. "I can't do X, but I can help you with Y" keeps the conversation moving.

**Principle 5 — Progressive disclosure:**
Surface basic capabilities first. Advanced features appear as the user demonstrates readiness. Don't front-load every option.

## Step 3 — Conversation Grammar Design

Define the "grammar" of the conversation — the patterns users can follow to get results.

**Entry patterns (how users start):**
- Direct command: "Write a PRD for [feature]"
- Question: "What should I build this sprint?"
- Informal: "I need help thinking through something"
- Gossip/update: "So we just decided to [thing]..."

For each pattern: what does the ideal opening response look like?

**Response patterns (how the AI responds):**
- Clarifying question (when input is ambiguous): One question, never more than one
- Executing (when input is clear): Confirm understanding in one sentence, then execute
- Informing (when user needs education): Brief orientation, then ask permission to go deeper
- Suggesting (when proactively surfacing something): Gentle nudge with an obvious opt-out

**Completion patterns (how interactions end):**
- Deliverable complete: "Here's your [output]. Want to [next natural action]?"
- Save offer: "Shall I save this to your [memory / file]?"
- Follow-on: "Based on this, you might also want to [related action]. Want me to run that?"

## Step 4 — Natural Language Affordances

Design the specific phrases the AI uses to signal what the user can do next. These are "invisible" UI elements — they guide the user without requiring them to know commands.

Examples:
- "I can also [action] if you need it"
- "Say 'save' to add this to your memory"
- "Want me to turn this into a stakeholder update?"
- "If anything has changed since last time, just tell me"

For this feature, write 5–8 natural language affordances appropriate to the user's context.

## Step 5 — Edge Case Conversation Design

Design responses for the most common edge cases:

**User says something out of scope:**
"I'm not sure I can help with [X] in the way you're describing, but if you're trying to [underlying goal], I can [alternative]. Want to try that?"

**User asks a question mid-task:**
"Good question — [brief answer]. Should I continue with [what we were doing], or do you want to explore this further first?"

**User gives ambiguous input:**
"I want to make sure I get this right. Are you asking about [interpretation A] or [interpretation B]?"

**User wants to change course:**
"Of course — let me start fresh. What would you like to do instead?"

**User says they're not satisfied with the output:**
"I can try again with a different approach. What specifically wasn't right about [the output]?"

## Step 6 — Output

Produce:
- NLX design principles for this feature (3–5 that are specific to this use case)
- Conversation grammar (entry, response, and completion patterns)
- Natural language affordances (5–8 phrases the AI uses to guide the user)
- Edge case conversation scripts (the 5 most common edge cases)
- A sample 5-turn conversation showing the feature working well

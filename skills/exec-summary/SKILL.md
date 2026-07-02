---
name: exec-summary
description: Use this skill when the user asks to "write an exec summary", "summarize this for leadership", "write a summary for the CEO", "board update summary", "executive brief", "leadership update", "write this for C-level", or needs to communicate a complex situation, decision, or initiative status to senior leadership in a concise, structured format. Do NOT use this skill for full stakeholder updates with multiple audience versions — use stakeholder/audience-tailoring for that.
version: 2.0.0
---

# Executive Summary

You are writing an executive summary using the Pyramid Principle — the communication framework used by McKinsey and the most effective PM communicators. The key principle: lead with the conclusion, not the journey to reach it.

Framework: Pyramid Principle (Barbara Minto), SCR framework (Situation / Complication / Resolution), Lenny's 14 PM habits (clarity is the most fundamental PM skill).

Key principle from Lenny: "Great PMs take pride in clarity. They never make the listener work to find the point." — 14 Habits of Highly Effective Product Managers, Lenny Rachitsky (2021)

## Step 1 — Load Context

Read `memory/personal/${USER}.md` for: stakeholder context (who is this going to, their communication style and sensitivities), product context, and current initiative status.

## Step 2 — Identify the Point

Before writing, answer: what is the single most important thing the reader needs to know or do?

This is the "bottom line up front" — the executive summary's headline. It should be:
- A conclusion, not a status update: "We need to delay launch by 2 weeks" not "Launch preparation is ongoing"
- An action or decision request, if one is needed: "I recommend we proceed with Option B"
- A risk or signal, if nothing else: "We have early indicators that the North Star metric is moving"

If the user can't articulate the bottom line in one sentence, help them find it before writing.

## Step 3 — SCR Structure

Structure the executive summary using Situation / Complication / Resolution:

**Situation (1–2 sentences):** The context the reader needs to understand. What's the current state? Assume the reader knows the basics and skip the background. Situation = "Here's where we are."

**Complication (1–3 sentences):** What's changed, at risk, or needs a decision. This is the tension that requires the reader's attention. Complication = "But here's the problem / challenge / opportunity."

**Resolution (2–4 sentences):** What you recommend, what you've decided, or what you need from the reader. This should be specific — not "we're monitoring the situation" but "I recommend X because Y. I need Z from you by [date]."

## Step 4 — Executive Summary Format

Depending on the context, format as:
- **Slack message:** 3–5 sentences using SCR implicitly. No headers. Bottom line first.
- **Email:** Subject line = the bottom line. Body = SCR in 3 short paragraphs. Max 200 words.
- **Slide:** One headline = the insight. 3 supporting bullets. One action item.
- **Verbal briefing (script):** 90 seconds. Open with bottom line. 2–3 supporting facts. Close with what you need from them.

Ask the user which format they need if it's not obvious.

## Step 5 — Exec-Calibrated Language

Apply these rules for executive communication:
- Use numbers when you have them: "7-day retention dropped 4 points" beats "retention is declining"
- Acknowledge uncertainty explicitly: "We believe X, but won't know for certain until [date]"
- Never bury the ask: the decision or action needed should be in the first or last sentence, not the middle
- One risk, not a list: executives worry about lists of risks — they want the one thing that matters most
- No jargon from internal tools: say "the team's tracking system" not "Linear"

## Step 6 — Output

Produce:
- The executive summary in the requested format
- An alternative if the user might need both Slack and email versions
- Flagged risks: any element of the summary that might push back from this specific stakeholder (based on their sensitivities in memory)

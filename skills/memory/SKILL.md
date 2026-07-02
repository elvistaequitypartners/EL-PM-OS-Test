---
name: memory
description: Use this skill when the user asks to "update my PM Operating System memory", "save this to my profile", "remember that", "update my context", "update my product context", "save this decision", "add this to my memory", "track this risk", "mark this risk as resolved", "add a lesson learned", "save these stakeholder notes", or any explicit request to persist information to the memory profile. Also use this skill at the end of any session where a PRD was written, a roadmap decision was made, or new stakeholder context was surfaced, when the user agrees to update memory. Do NOT use this skill just because the user is mentioning their product — only use it when explicitly updating the persistent profile.
version: 2.0.0
---

# Memory Layer — Persistent PM Context

You manage the user's persistent PM memory profile. Your job is to read, write, and maintain `memory/user-profile.md` so that PM Operating System has complete, accurate context without the user needing to re-brief every session.

## Reading Memory

At session start, read `memory/user-profile.md` and extract:

1. **Product context** — name, stage, core problem, business model, current bets
2. **Stack** — which tools are connected (issue tracker, docs, comms, analytics)
3. **Working style** — PRD format preference, verbosity, preferred frameworks
4. **Stakeholders** — names, roles, communication styles, sensitivities
5. **Roadmap state** — what's in Now/Next/Later, what's been decided and why
6. **Open questions** — unresolved assumptions and risks
7. **Tracked risks** — active risks with dates flagged
8. **Lessons learned** — retrospective outcomes from past initiatives

Apply context to personalize every response. If `last_updated` is more than 7 days ago, note it and prompt for a refresh.

## Checking Staleness

After loading memory, check:
- If `last_updated` > 7 days: "Your product context hasn't been updated in [N] days. What's changed?"
- If any `open_questions` item is > 14 days old: "You flagged '[question]' [N] days ago. Is it resolved or still open?"
- If any `tracked_risks` item is > 7 days old with status "open": "You flagged '[risk]' as a risk [N] days ago. Is it still active?"
- If any `roadmap_state.now` item has a target date within 7 days: "Your roadmap shows '[item]' launching soon. Want to run /stakeholder-update?"

Surface at most 2 staleness prompts per session to avoid overwhelming the user.

## Writing Memory

When the user asks to update memory (or agrees to after a session), edit `memory/user-profile.md` with the following rules:

**Add, never replace blindly:** Before updating a field, read its current value. If existing content is still valid, preserve it and append the new information. Don't overwrite unless the user explicitly wants to replace.

**Date every new entry:** All items in `open_questions`, `tracked_risks`, `lessons_learned`, and `decided_and_why` must include the date added.

**Resolve, don't delete:** When a risk is resolved or a question is answered, update its status and add a resolution note — don't remove the entry. This preserves institutional knowledge.

**Always update `last_updated`:** Set it to today's date (ISO format) after every write.

## What to Capture Per Session Type

**After /write-prd:**
- Add to `decided_and_why`: the core decision the PRD represents (what are we building and why)
- Add to `open_questions`: any unresolved questions from the Open Questions section
- Add to `tracked_risks`: any risks identified in the Dependencies & Risks section
- Update `roadmap_state.now` or `roadmap_state.next` if this PRD is for an active initiative

**After /roadmap:**
- Overwrite `roadmap_state` with the updated Now/Next/Later
- Add to `decided_and_why` any prioritization decisions made
- Add to `tracked_risks` any pre-mortem risks that were surfaced
- Add to `open_questions` any dependencies that are unresolved

**After /stakeholder-update:**
- Update the stakeholder's `last_contact` date in the stakeholders section
- Add to `decided_and_why` any decisions that surfaced during update preparation
- Update initiative status in `roadmap_state`

**After /synthesize-research:**
- Update the relevant persona section with any new signals
- Add to `open_questions` any questions the research raised but didn't answer
- Add potential new roadmap items to `roadmap_state.later`
- Add to `lessons_learned` if the research confirmed or invalidated a past assumption

**After Gossip Mode (informal updates):**
- Parse the informal update and extract: new stakeholder context, roadmap changes, risks surfaced, decisions made
- Add extracted items to the appropriate sections
- Confirm the parsed update with the user before writing

## Gossip Mode Parsing

When the user speaks informally (voice-to-text style, or "you won't believe what just happened..."), parse and extract structured memory updates:

Look for:
- **People + opinions:** "[Name] said [X]" → potential stakeholder note
- **Blockers:** "[X] is blocked because [Y]" → tracked risk candidate
- **Decisions:** "We decided to [X]" → `decided_and_why` candidate
- **Product changes:** "We're not doing [X] anymore" → roadmap state update
- **Customer signals:** "[Customer] complained about [X]" → potential open question or persona note
- **Timeline shifts:** "[Item] is slipping to [date]" → roadmap state update

After parsing, show the user what you extracted and confirm before writing to the profile.

## Memory Schema Reference

Refer to `memory/schema.md` for the full field definitions and update rules.

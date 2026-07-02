---
description: Triage a batch of user feedback — cluster themes, score by frequency × severity × strategic fit, route top issues to roadmap or experiments
argument-hint: <paste feedback, file path, or "intercom"/"zendesk" to pull from connected tools>
allowed-tools: [Read, Write, Glob, Agent, WebSearch]
---

# /triage-feedback

You are a senior PM partner triaging user feedback. This chains: input detection → theme clustering → scoring → persona mapping → experiment recommendations → roadmap routing. The goal is to turn a pile of unstructured feedback into a ranked, actionable report.

Framework: Lenny Rachitsky (feedback methodology), frequency × severity × strategic fit scoring, Teresa Torres (opportunities not solutions).

## Input

The user has invoked this command with: `$ARGUMENTS`

Input can be:
- **Pasted feedback** directly in the message
- **File paths** to CSVs, text files, or transcripts
- **"intercom" / "zendesk" / "notion"** — pull from connected tools via MCP
- **Mixed** — any combination

If no input, ask: "Paste your feedback, provide file paths, or tell me which tool to pull from."

## Step 1 — Load Memory & Context

Read in parallel:
- `memory/user-profile.md` — product context, current OKRs, roadmap state
- `context/product/roadmap.md` (fallback: `context/product/roadmap-template.md`)
- `context/product/personas.md` (fallback: `context/product/personas-template.md`)

Context is critical: strategic fit scoring depends on knowing what's already being worked on.

### No-Context Fallback

If `memory/user-profile.md` doesn't exist or is nearly empty, feedback triage still works — just without strategic fit scoring. Ask:

1. "What product is this feedback about?" (one sentence)
2. "What are you focused on building right now?" (so strategic fit can be assessed)

Score strategic fit based on the answer. After completing, offer: "This triage surfaced a lot about your users and product. Want me to save the top pain points and persona signals to your PM Operating System memory?"

## Step 2 — Input Detection & Normalization

Detect the format and normalize:
- **Plain text / list:** Each line = one feedback entry
- **CSV / TSV:** Identify the feedback column; preserve metadata (date, severity, user tier)
- **JSON:** Extract text field; note structured fields
- **Transcript:** Split into distinct feedback points (one paragraph may contain multiple)
- **Tool pull:** Use MCP to pull recent tickets/conversations

## Step 3 — Volume-Based Processing

Count items and select approach:
- **< 50 items:** Single-pass analysis
- **50–200 items:** Two passes — cluster first, then rank
- **200+ items:** Spawn parallel sub-agents (batches of ~50), then merge

For 200+ items, use sub-agents:
```
Analyze the following [N] feedback items. For each theme found:
1. Theme name (3–5 words)
2. Frequency count
3. Severity signal (Blocking / Major friction / Minor annoyance)
4. Best representative quote
5. Affected persona (if identifiable)
Return as a structured list.
```

## Step 4 — Theme Clustering

Group feedback into recurring themes. A valid theme:
- Has at least 2 separate sources mentioning the same underlying issue
- Is distinct from other themes (not a subset)
- Is framed as a user struggle, NOT a feature request

Reframe any "I wish it had X" as "Users struggle to [do Y], which X would solve."

For each theme, capture:
- Theme name (3–5 words)
- Frequency count and percentage of total
- Severity signal: Blocking / Major friction / Minor annoyance
- 1–2 representative quotes (strongest voice-of-customer)
- Affected persona(s)

## Step 5 — Impact Scoring

Score each theme:

| Theme | Frequency (0–5) | Severity (0–3) | Strategic Fit (0–2) | Impact Score (/10) |
|---|---|---|---|---|
| [Theme] | [count-based] | [blocking=3, major=2, minor=1, cosmetic=0] | [serves OKR=2, adjacent=1, misaligned=0] | [sum] |

Sort by impact score descending.

## Step 6 — Persona Signal Analysis

For each top theme:
- Which persona segment is most affected?
- Is this a power user issue or a new user issue?
- Are there signals of a segment not yet in the persona file?
- AI Embracer vs. AI Skeptic signal (if applicable to the product)

Flag any evidence that should update persona definitions.

## Step 7 — Roadmap Routing

For each top-5 theme, recommend a routing:

| Theme | Route | Rationale |
|---|---|---|
| [Theme] | **Now — add to sprint** | High score + already near a roadmap item |
| [Theme] | **Next — add to backlog** | High score but needs scoping |
| [Theme] | **Experiment first** | High score but uncertain solution |
| [Theme] | **Monitor** | Medium score, watch for trend |
| [Theme] | **Decline** | Low score or anti-persona |

For items routed to "Experiment first", recommend:
- **Hypothesis:** "If we [intervention], [user type] will [outcome]"
- **Cheapest test:** The lowest-cost way to validate
- **Metric:** What confirms the hypothesis

## Step 8 — What to Ignore (and Why)

Flag feedback that doesn't warrant action:
- Single mention with no corroborating signal
- Anti-persona request (user not in target segment)
- Contradicts a deliberate product decision (explain the decision)
- Technical impossibility within current architecture
- Vocal minority with no frequency signal

Being explicit about what to ignore is as important as what to act on.

## Step 9 — Feedback Report Output

Produce:

1. **Executive summary:** Top 3 pain points in one paragraph
2. **Theme table:** All themes ranked by impact score with quotes
3. **Persona heat map:** Which personas are most affected
4. **Roadmap routing:** Where each theme should go
5. **Experiment recommendations:** For uncertain themes
6. **Sentiment overview:** Rough split (satisfied / neutral / frustrated)
7. **What to ignore:** Explicitly declined items with rationale
8. **Trend alert:** Any theme that's new or growing compared to previous triages

## Step 10 — Save & Update Memory

Offer to:
- Save to `outputs/feedback-triage-[date].md`
- Update `memory/user-profile.md` with:
  - New pain points discovered (→ potential roadmap items)
  - Open questions from feedback (→ `open_questions`)
  - Persona updates (→ note in memory)

---

## Quality Bar

A good feedback triage from this command:
- Reframes all feature requests as underlying struggles
- Has every theme scored on the 10-point scale
- Has explicit roadmap routing for top 5 themes
- Has a "what to ignore" section (never ignores silently)
- Includes persona mapping for each theme
- Ends with: *"Are we hearing what users are saying, or what we want to hear? Which theme surprised us most?"*

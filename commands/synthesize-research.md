---
description: Synthesize user research into OST opportunity areas — ingests interview transcripts, survey data, or Notion docs; extracts themes, persona signals, and evidence map
argument-hint: <paste transcripts / path to files / "notion" to pull from Notion>
allowed-tools: [Read, Write, Glob, Agent, mcp__notion__API-post-search, mcp__notion__API-retrieve-a-page]
---

# /synthesize-research

You are a senior PM partner and user researcher. Transform raw research into structured opportunities using Teresa Torres' Opportunity Solution Tree framework. Never skip from themes to solutions — always go through the opportunity layer.

Framework defaults: Teresa Torres (OST + Continuous Discovery), Bob Moesta (switch interview methodology), Hilary Gridley (AI-embracer vs. skeptic segmentation).

## Input

The user has invoked this command with: `$ARGUMENTS`

Input can be:
- **Pasted transcripts or notes** in the message
- **File paths** to transcript or note files
- **"notion"** — pull research notes from connected Notion workspace
- **Mixed** — both pasted and file-based

If no input is provided, ask: "Paste your research notes, provide file paths, or say 'notion' to pull from your connected Notion workspace."

## Step 1 — Load Memory & Context

Read in parallel:
- `memory/personal/${USER}.md` — product context, personas, current bets, open questions
- `context/product/personas.md` (fallback: `context/product/personas-template.md`)
- `context/product/roadmap.md` (fallback: `context/product/roadmap-template.md`)
- `context/templates/research-synthesis-template.md` — output template

Note: existing open questions from memory that this research might answer.

### No-Context Fallback

If `memory/personal/${USER}.md` doesn't exist or is nearly empty, do NOT stop. Research synthesis is one of the best entry points — the research itself provides context. Instead, ask:

1. "What product is this research for?" (one sentence)
2. "Who are your target users?" (one sentence)

Proceed with the synthesis. The themes and opportunities you extract will naturally build product context. After completing, offer: "This research gave me a lot of context about your product and users. Want me to save it to your PM Operating System memory?"

## Step 2 — Pull Research Input

If `$ARGUMENTS` is "notion" or includes "notion":
- Use Notion MCP to search for recent meeting notes, interview notes, or research pages
- Pull pages tagged with "research", "interview", "user call", or "discovery"
- Confirm what was found with the user before proceeding

If files are provided, read them.

If content is pasted directly, use it as-is.

## Step 3 — Assess Volume and Split Work

Count the number of distinct research items (interviews, survey responses, support tickets):
- **Under 20 items:** Analyze in a single pass
- **20–100 items:** Cluster first, then rank themes
- **100+ items:** Use parallel sub-agents

For 100+ items, split into batches of ~25 and launch sub-agents:
```
You are a research analyst. Analyze the following [N] research items.
For each item, identify: the user struggle or unmet need expressed, the emotional tone (frustrated / neutral / satisfied), and a representative quote.
Return: a list of (theme, count, severity signal, best quote) tuples.
```
Merge and de-duplicate sub-agent outputs before proceeding.

## Step 4 — Theme Extraction

Group research into recurring themes. A theme is valid if:
- At least 2 separate sources mention the same underlying issue
- The issue is distinct (not a subset of another theme)

For each theme, capture:
- Theme name (3–5 words)
- Frequency count and percentage
- Severity signal (blocking / major friction / minor annoyance)
- 1–2 representative quotes
- Affected persona(s)

## Step 5 — OST Opportunity Mapping (Teresa Torres)

Map each theme to the Opportunity Solution Tree:

**Desired outcome:** What user or business outcome does the research point toward?

For each theme, frame it as an opportunity:
- **Opportunity statement:** "Users struggle to [action] when [context] because [root cause]"
- **OST level:** Is this a top-level opportunity, or a sub-opportunity under a larger struggle?
- **Evidence strength:** How many sources? How severe?

Build the OST hierarchy:
```
Desired outcome: [User outcome]
├── Opportunity 1: [Struggle statement]
│   ├── Sub-opportunity 1a: [More specific struggle]
│   └── Sub-opportunity 1b: [More specific struggle]
├── Opportunity 2: [Struggle statement]
└── Opportunity 3: [Struggle statement]
```

Flag: any "opportunity" that is actually a solution in disguise (e.g., "users want dark mode" is a solution — the opportunity is "users can't use the product comfortably in low-light environments").

## Step 6 — Persona Signal Analysis

For each theme, identify which persona segment it belongs to:
- Is this an AI Embracer signal (excited, self-directed) or AI Skeptic signal (cautious, wants proof)?
- Does this come from your primary or secondary persona?
- Are there signals of a new segment not yet in the persona file?

Flag any evidence that should update the persona file.

## Step 7 — Evidence Mapping

For the top 3 opportunities, build an evidence map:

| Claim | Evidence | Source Count | Strength |
|---|---|---|---|
| [The opportunity claim] | [Quotes + behavioral observations] | [N sources] | [Strong/Medium/Weak] |

Distinguish: **attitudinal evidence** (what users say) vs. **behavioral evidence** (what users do). Behavioral evidence is stronger. Flag where you only have attitudinal evidence and suggest behavioral validation.

## Step 8 — Open Questions Raised

What did this research NOT answer that we need to know before building?
- What assumption is still unvalidated?
- Which opportunity needs more evidence before we invest?
- What follow-up study would give the most signal?

## Step 9 — Recommend Experiments

For the top 2–3 opportunities, recommend one experiment each:
- **Hypothesis:** "If we [intervention], [user type] will [outcome]"
- **Method:** [Prototype test / Wizard of Oz / Concierge / Fake door / Survey / Other]
- **Metric:** [What would confirm the hypothesis?]
- **Minimum bar:** [What result would justify building?]

## Step 10 — Output and Save

Fill in `context/templates/research-synthesis-template.md` with all findings.

Offer to:
- Save to `outputs/research-[study-name]-[date].md`
- Update `memory/personal/${USER}.md` with:
  - New opportunities (→ potential roadmap items in `roadmap_state`)
  - Open questions raised (→ `open_questions`)
  - Persona updates (→ update memory to note persona changes)
  - Lessons learned (→ `lessons_learned` if this research confirmed or invalidated a past bet)

---

## Quality Bar

A good research synthesis from this command:
- Distinguishes opportunities from solutions (never lets a solution masquerade as an opportunity)
- Has an OST hierarchy showing how sub-opportunities relate
- Distinguishes attitudinal from behavioral evidence
- Has AI-embracer vs. skeptic signal analysis
- Surfaces at least one thing the research did NOT answer
- Ends with: *"What is the riskiest assumption remaining? What would we need to learn to make confident bets on these opportunities?"*

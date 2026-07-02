# The AI-Native PM Operating System

### Plugin for Claude Code, Claude Cowork, Claude Desktop, and Claude.AI Web || Product Faculty

Stop working like a 2022 PM. Start operating like an AI-native one — solo *or* as a team.

PM Operating System is your AI Product Manager and an AI operating system for your product work. As of v3.0, it's team-aware: multiple PMs can share product context, roadmap state, and decisions through git — without last-writer-wins overwrites, without giving up personal notes.

- **65+** embedded PM skills across 12 domains
- **19** command-based workflows (end-to-end execution, not prompts)
- **8** specialized sub-agents (discovery, strategy, GTM, metrics, etc.)
- **Three-layer memory** — personal (private) / team (shared, PR-reviewed) / org (2-approval) — with immutable ADRs for durable decisions
- **GitOps governance** — schemas, CODEOWNERS, CI validation, staleness reconciler, prompt-injection scanner
- **Tracker sync** — hourly Linear/Jira → YAML for live roadmap state

Every command pulls your full context, connects to your tools, and executes like a real operator.

It's time to become a 100x Product Manager — and a 100x product *team*.

Built by Product Faculty: We run [#1 AI PM Certification](https://maven.com/product-faculty/ai-product-management-certification?promoCode=git) — trusted by 3,000+ PMs (1,000+ reviews) learning how to build and operate AI-native products.

---

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [What's Inside](#whats-inside)
  - [19 Slash Commands](#19-slash-commands)
  - [65 PM Skills Across 12 Domains](#65-pm-skills-across-12-domains)
  - [8 Specialized Sub-Agents](#8-specialized-sub-agents)
  - [Three-Layer Memory Model](#three-layer-memory-model)
  - [Live Tool Connectors (MCP)](#live-tool-connectors-mcp)
  - [Gossip Mode](#gossip-mode)
- [Team Mode](#team-mode)
  - [Layered memory in one picture](#layered-memory-in-one-picture)
  - [Promoting personal memory to team scope](#promoting-personal-memory-to-team-scope)
  - [Architecture Decision Records (ADRs)](#architecture-decision-records-adrs)
  - [GitOps governance](#gitops-governance)
  - [Tracker integration](#tracker-integration)
- [Platform Guide](#platform-guide)
- [MCP Setup (Claude Code)](#mcp-setup-claude-code)
- [Connector Setup (Claude Cowork)](#connector-setup-claude-cowork)
- [Project Structure](#project-structure)
- [Frameworks Embedded](#frameworks-embedded)
- [Customization](#customization)
- [FAQ](#faq)
- [License](#license)

---

## Install

### Claude Code (CLI)

```bash
claude plugin install .
```

Or install from a Git URL:

```bash
claude plugin install https://github.com/yourorg/pm-os
```

### Claude Cowork (Desktop)

1. Open Claude Desktop and switch to the **Cowork** tab
2. Click **Customize** in the left sidebar
3. Click **Browse plugins** or upload the plugin folder directly
4. PM Operating System appears in your plugin list — click **Install**

### First Run

On first run, PM Operating System launches the onboarding wizard automatically. It asks 10 questions about your product, stack, stakeholders, and working style — then writes your **personal** memory profile at `memory/personal/<your-username>.md` and offers to promote team-relevant answers (roadmap, stakeholders, personas) into shared team memory via PR.

Takes about 5 minutes, and you never have to re-brief Claude again.

Trigger manually with:

```
/onboarding
```

Or just say: *"I want to set up PM Operating System"*

---

## Quick Start

Once installed and onboarded:

| What you want to do | Command |
|---|---|
| Set up your personal profile (first time) | `/onboarding` |
| Start your day with a briefing | `/brief-me` |
| Write a PRD from a feature idea | `/write-prd smart notifications for enterprise users` |
| Review your team roadmap | `/roadmap` |
| Promote a personal note into team memory | `/promote-memory <what to promote>` |
| Capture a durable decision as an ADR | `/adr <decision title>` |
| Send a stakeholder update | `/stakeholder-update` |
| Run a strategy review | `/strategy-review` |
| Triage user feedback | `/triage-feedback` |

Every command pulls your layered memory context (org → team → personal → recent ADRs), loads relevant files, and connects to your live tools (Linear, Jira, Slack, Notion) if configured. No re-briefing, no context-setting — just go.

---

## What's Inside

### 19 Slash Commands

Commands are chained workflows that wire multiple skills together into end-to-end operations.

| Command | What it does |
|---|---|
| `/onboarding` | First-run setup wizard — 10 questions about your product, stack, stakeholders, and working style. Writes your personal profile and offers team-scope promotions |
| `/brief-me` | Your morning briefing — loads memory, pulls live state from all connected tools, surfaces risks and open ADRs, recommends where to start |
| `/write-prd` | JTBD analysis, OST framing, full PRD from template, prototype-ready spec, GTM positioning section |
| `/roadmap` | OKR alignment, Now/Next/Later structuring, dependency mapping, 3 stakeholder views (exec/eng/customer) |
| `/stakeholder-update` | Pull tracker + Slack context, produce audience-tailored updates (exec: Pyramid Principle, eng: context-first, customer: narrative) |
| `/synthesize-research` | Ingest interviews/transcripts/Notion docs, extract themes, persona signals, opportunity areas, evidence map |
| `/discover` | Full discovery cycle: problem framing, JTBD forces, assumption mapping, TAM/SAM/SOM, OST, experiment plan |
| `/strategy-review` | Score product strategy across 5 dimensions (25-point scale), competitive positioning, strategic gaps |
| `/plan-sprint` | Pull backlog from Linear/Jira, prioritize by outcome alignment, generate sprint plan with capacity check |
| `/triage-feedback` | Score feedback themes by frequency + severity + strategic fit (10-point scale), surface top patterns |
| `/setup-metrics` | Define North Star metric, supporting metrics, AARRR funnel, dashboard structure |
| `/plan-launch` | Launch checklist, GTM timeline, messaging hierarchy, risk mitigation, rollback criteria |
| `/competitive-intel` | Competitor analysis, battlecard generation, positioning gaps, differentiation opportunities |
| `/retro` | Compare shipped outcomes vs. original PRD predictions, assumption audit, lessons learned |
| `/set-okrs` | Structure OKRs from strategy context, validate measurability, align to North Star |
| `/design-ai-feature` | AI-specific: validate AI necessity, model tier selection, prompt architecture, eval framework, cost model, NLX UX |
| `/weekly-digest` | Pull week's activity from all connected tools, compile digest with wins, blockers, and next-week focus |
| **`/promote-memory`** | **New in v3.0** — escalate a fact from your personal profile into shared team memory via PR |
| **`/adr`** | **New in v3.0** — capture a durable product decision as an Architecture Decision Record, immutable once merged |

### 65 PM Skills Across 12 Domains

Skills are the atomic units of PM knowledge. Each skill lives in `skills/[name]/SKILL.md`, fires automatically when relevant, and can also be invoked directly. Every skill loads your layered memory context and routes writes to the right scope (personal / team via PR / org / ADR).

| Domain | Skills | Key Frameworks |
|---|---|---|
| **System** | Memory layer, Onboarding wizard, Gossip mode | Tal Raviv (onboarding pattern) |
| **Discovery** | Problem framing, Assumption mapping, JTBD analysis, OST, Continuous interview synthesis, Opportunity sizing, Switch interview | Teresa Torres (OST, CD), Bob Moesta (JTBD) |
| **Strategy** | Vision setting, North Star, OKR structuring, Competitive positioning, Beachhead mapping, Pre-mortem, Product work levels, 7 Powers, Strategy stack | Marty Cagan, Hamilton Helmer, Shreyas Doshi |
| **Execution** | PRD authoring, User story decomposition, Epic breakdown, Sprint prioritization, Prototype-ready spec | Pyramid Principle, Lenny's PRD guide |
| **Stakeholder Comms** | Exec summary, Launch announcement, Eng brief, Weekly digest, Risk escalation, Audience tailoring | Minto SCR, Pyramid Principle |
| **Market & Users** | Persona development, Journey mapping, TAM/SAM/SOM sizing, Competitor battlecards, Feedback triage, Attitudinal segmentation | April Dunford (positioning) |
| **Metrics & Data** | Cohort analysis, A/B test design, Funnel analysis, North Star selection, Dashboard structuring, SQL generation | North Star framework, AARRR, Lenny's guide |
| **AI Evals** | Error analysis, Eval suite design, LLM-as-judge, Human eval design, Regression testing, Improvement flywheel | Hamel Husain, Shreya Shankar |
| **Go-to-Market** | Launch planning, ICP definition, Messaging hierarchy, Growth loops, Pricing review, AI feature monetization, 5-component positioning | April Dunford (Obviously Awesome) |
| **Prototyping** | Vibe-coding from PRD, Prototype prompt, NLX design, Figma-to-prototype, Happy path scoping | Aparna Chennapragada (NLX), Colin Matthews |
| **Career Arc** | Solo PM to CPO, Altitude-horizon, Technical PM, Founding PM, Becoming Senior PM | Jackie Bavaro |

### 8 Specialized Sub-Agents

Sub-agents are isolated workers that handle complex, multi-step PM tasks. When a command or conversation requires deep work — discovery research, strategy analysis, document production — Claude automatically delegates to the right sub-agent. Each agent has relevant skills preloaded as domain knowledge and runs in focused isolation.

| Agent | What it handles | Preloaded Skills |
|---|---|---|
| **Discovery Researcher** | Problem framing, JTBD forces analysis, opportunity sizing, assumption mapping, interview synthesis | 7 discovery skills |
| **Strategy Analyst** | Vision setting, competitive positioning, 7 Powers analysis, OKR structuring, pre-mortems | 9 strategy skills |
| **Document Writer** | PRD authoring, user story decomposition, epic breakdown, prototype-ready specs | 5 execution skills |
| **Stakeholder Communicator** | Exec summaries, eng briefs, launch announcements, risk escalations, weekly digests | 6 stakeholder skills |
| **Market Researcher** | Persona development, journey mapping, TAM sizing, competitor battlecards, feedback triage | 6 market & users skills |
| **Metrics Analyst** | North Star selection, funnel analysis, A/B test design, cohort analysis, dashboard structuring | 6 metrics skills |
| **GTM Planner** | Launch planning, ICP definition, messaging hierarchy, positioning, pricing review | 7 GTM skills |
| **AI Evaluator** | Error analysis, eval suite design, LLM-as-judge pipelines, regression testing | 6 AI eval skills |

### Three-Layer Memory Model

PM Operating System v3.0 replaces the single `memory/user-profile.md` with a **layered memory hierarchy** modeled on Claude Code's own precedence rules and Letta/Mem0's scoped-memory patterns. Every session loads all three layers automatically.

| Layer | Path | Trust | Who writes |
|---|---|---|---|
| **Personal** | `memory/personal/<user>.md` | Trusted (self-written) | Direct edit — gitignored |
| **Team** | `memory/team/<team>/{roadmap,risks,personas,stakeholders}.yaml` + `digests/*.md` | Untrusted (multi-writer) | PR via `/promote-memory` |
| **Org** | `memory/org/*.md` | Untrusted | Direct PR, 2 approvals required |
| **Decisions** | `memory/decisions/adr-NNNN-*.md` | Immutable once merged | PR via `/adr` |

At session start, PM Operating System loads `org → team → personal → recent decisions` in precedence order (personal wins on conflict, never leaks upward). See the [Team Mode](#team-mode) section for the full picture.

### Live Tool Connectors (MCP)

Connect once, and every command pulls live data from your actual stack:

| Tool | What PM Operating System reads | What PM Operating System writes |
|---|---|---|
| **Linear** | Issues, roadmap state, sprint backlog, blockers | Tickets, status updates. Also feeds hourly `tracker-sync` into team roadmap YAML |
| **Jira** | Board, backlog, sprint state, blockers | Issues, status updates. Also feeds hourly `tracker-sync` |
| **Notion** | Spec pages, knowledge base, meeting notes | Spec drafts, research docs, PRD pushes |
| **Slack** | Channel context, thread sentiment, decisions, @mentions | Stakeholder updates |
| **GitHub** | Issue backlog, PR velocity, engineering output | — |

All connectors are optional. PM Operating System works fully without them — it just can't pull live data from your tools. Commands gracefully skip any connector that isn't configured.

### Gossip Mode

Speak informally — voice-to-text, stream-of-consciousness, "you won't believe what happened in standup" — and PM Operating System parses it into structured memory updates. It extracts stakeholder signals, roadmap changes, risks, decisions, and team dynamics, then routes each to the right scope (personal by default; offers `/promote-memory` for team-relevant items). Designed to complete in under 60 seconds.

---

## Team Mode

v3.0 makes PM Operating System usable by multiple PMs sharing the same repo. The design is documented in full in [`memory/decisions/adr-0001-adopt-team-shared-memory.md`](./memory/decisions/adr-0001-adopt-team-shared-memory.md) and the design proposal (`PMOS_Readme.md` — team-shared design doc). Highlights below.

### Layered memory in one picture

```
memory/
├── org/                            # company-wide, 2 approvals to merge
│   └── mission.md
├── team/
│   └── <team-name>/                # PR-reviewed by any team PM
│       ├── roadmap.yaml            # ← schema-validated
│       ├── risks.yaml
│       ├── personas.yaml
│       ├── stakeholders.yaml
│       └── digests/                # append-only weekly narrative
├── personal/                       # gitignored per-PM notes
│   └── <user>.md
├── decisions/                      # ADRs, immutable once merged
│   └── adr-NNNN-<slug>.md
└── schemas/                        # JSON Schema draft-07 for every YAML
```

**Load precedence at session start:** `org → team → personal → 10 most recent ADRs`. Personal wins on conflict but never leaks upward.

### Promoting personal memory to team scope

Nothing moves from personal to team silently. When you want to share:

```
/promote-memory the CTO's new caching preference
```

Claude reads your personal notes, identifies the fact, routes it to the right team YAML file (`stakeholders.yaml`, `risks.yaml`, `roadmap.yaml`, etc.), validates the shape against the schema, opens a branch, and creates a PR labeled `memory-promotion`. Your teammates review, request changes if needed, and merge — that's when it becomes team truth.

### Architecture Decision Records (ADRs)

Durable cross-team decisions get their own record:

```
/adr adopt streaming-first ingestion for v2
```

Creates `memory/decisions/adr-NNNN-<slug>.md` in `proposed` status with the ADR template (Context, Decision, Consequences, Alternatives). Merges to `accepted`. If reversed later, a new ADR sets `supersedes: [ADR-XXXX]` — ADRs are never edited, only superseded.

### GitOps governance

Everything in `memory/team/**` and `memory/org/**` is treated as [content-as-code](https://github.com/open-gitops/documents/blob/main/PRINCIPLES.md):

- **Declarative** — the YAML files *are* the roadmap
- **Versioned & immutable** — `git blame` shows who changed which risk, when
- **Pulled automatically** — the SessionStart hook at `.claude/hooks/session-start.sh` runs `git pull --rebase` on every session
- **Continuously reconciled** — CI runs on every PR:
  - **`validate.yml`** — JSON Schema validation, markdown lint, prompt-injection scanner
  - **`staleness.yml`** — weekly cron, opens issues for files without a `last_updated` refresh in 30 days
  - **`tracker-sync.yml`** — hourly Linear/Jira → YAML sync (PM-owned fields never overwritten)

`.github/CODEOWNERS` routes review by path:

- `memory/personal/*` → author only
- `memory/team/**` → `@vista-pm-guild` (any team PM)
- `memory/org/**` → `@head-of-product @product-ops` (two approvals)
- `memory/decisions/**` → `@head-of-product`

### Tracker integration

`memory/team/<team>/roadmap.yaml` links initiatives to Linear projects or Jira epics via `linear_project_id` / `jira_epic_key`. An hourly workflow (`tracker-sync.yml`) pulls `tracker_status`, `target_date`, and `owner` from the tracker and opens a PR on any drift. PM-owned fields (`title`, `strategic_bet`, `adr_refs`) are never touched by the bot — the split is by field, not by document.

For volatile data (velocity, this-sprint blockers), the session-start MCP query fetches it live instead of caching to disk.

---

## Platform Guide

PM Operating System runs on every Claude surface. Here's what to know for each.

### Claude Code (CLI)

This is the full-power experience. Everything works out of the box:

- All 19 slash commands via `/command-name`
- All 65 skills fire automatically based on context
- 8 specialized sub-agents for complex multi-step workflows
- MCP connectors via `.mcp.json` (Linear, Jira, Notion, Slack, GitHub)
- Sub-agent parallelism for commands like `/brief-me` and `/roadmap`
- File I/O for reading context, writing outputs, and updating memory
- `CLAUDE.md` loads automatically as global instructions
- SessionStart hook (`.claude/hooks/session-start.sh`) reconciles team memory on every session

**Requirements:** Claude Code CLI installed, Node.js (for MCP servers via npx), git (for team-memory GitOps flow)

### Claude Cowork (Desktop)

Cowork provides the same skills and commands through a visual interface with autonomous task execution:

- All skills and slash commands work identically
- Connectors are set up through the **Customize > Connectors** UI (not `.mcp.json`)
- Sub-agents run in parallel with visual progress — often faster than Claude Code
- File-based memory works natively (Cowork reads/writes your local files)
- `CLAUDE.md` loads as project instructions

**Key differences from Claude Code:**
- Connector setup is via UI, not `.mcp.json` — see [Connector Setup](#connector-setup-claude-cowork)
- No terminal required — everything happens in the desktop app
- Tasks can be scheduled to run on a recurring basis
- SessionStart hook not supported natively — pull team memory manually or via a scheduled task

**Requirements:** Claude Desktop app with Cowork enabled (Pro or Max subscription, macOS)

---

## MCP Setup (Claude Code)

The `.mcp.json` file in the project root configures five MCP servers. Copy `.env.example` to `.env` and fill in the credentials for the connectors you use:

```bash
cp .env.example .env
# edit .env with your tokens
```

Contents of `.env.example`:

```bash
# Linear
LINEAR_API_KEY=lin_api_...

# Jira
JIRA_URL=https://yourorg.atlassian.net
JIRA_EMAIL=you@company.com
JIRA_API_TOKEN=...

# Notion
NOTION_API_KEY=secret_...

# Slack
SLACK_BOT_TOKEN=xoxb-...
SLACK_TEAM_ID=T...

# GitHub
GITHUB_TOKEN=ghp_...

# Optional: override team resolved from .pm-os.yaml
# PM_TEAM=platform
```

`.env` is gitignored — never commit real credentials. `.env.example` is the committed template, safe to share.

Only configure the tools you use. Unconfigured connectors are silently skipped.

---

## Connector Setup (Claude Cowork)

In Cowork, connectors are managed through the UI instead of `.mcp.json`:

1. Open **Customize** in the Cowork sidebar
2. Go to **Connectors**
3. Search for and connect the tools you use: **Linear**, **Jira**, **Notion**, **Slack**, **GitHub**
4. Authenticate through each connector's OAuth flow

Once connected, PM Operating System commands automatically pull live data from your tools — no environment variables or config files needed.

---

## Project Structure

```
pm-os/
├── .claude-plugin/
│   ├── plugin.json                # Plugin manifest (name, version, metadata)
│   └── marketplace.json           # Marketplace entry
├── .claude/
│   ├── hooks/
│   │   └── session-start.sh       # SessionStart: git pull --rebase + $CURRENT_TEAM
│   └── settings.json              # Hook wiring + permission allowlist
├── .github/
│   ├── CODEOWNERS                 # Route review by memory scope
│   └── workflows/
│       ├── validate.yml           # JSON Schema + markdown lint + injection scanner
│       ├── staleness.yml          # Weekly staleness reconciler
│       └── tracker-sync.yml       # Hourly Linear/Jira → YAML sync
├── .mcp.json                      # MCP server config (Claude Code only)
├── .env.example                   # Per-user secret template (copy to .env)
├── .pm-os.yaml                    # Team / members / trackers config
├── .pre-commit-config.yaml        # Schema + markdown lint (local)
├── CLAUDE.md                      # Global instructions loaded every session
│
├── commands/                      # 19 slash commands (chained workflows)
│   ├── onboarding.md
│   ├── brief-me.md
│   ├── write-prd.md
│   ├── roadmap.md
│   ├── stakeholder-update.md
│   ├── synthesize-research.md
│   ├── discover.md
│   ├── strategy-review.md
│   ├── plan-sprint.md
│   ├── triage-feedback.md
│   ├── setup-metrics.md
│   ├── plan-launch.md
│   ├── competitive-intel.md
│   ├── retro.md
│   ├── set-okrs.md
│   ├── design-ai-feature.md
│   ├── weekly-digest.md
│   ├── promote-memory.md          # v3.0
│   └── adr.md                     # v3.0
│
├── agents/                        # 8 specialized sub-agents
│   ├── discovery-researcher.md
│   ├── strategy-analyst.md
│   ├── document-writer.md
│   ├── stakeholder-communicator.md
│   ├── market-researcher.md
│   ├── metrics-analyst.md
│   ├── gtm-planner.md
│   └── ai-evaluator.md
│
├── skills/                        # 65 skills — skills/[name]/SKILL.md
│   ├── memory/SKILL.md            # v3.0 — three-scope routing
│   └── ... (64 more)
│
├── memory/                        # v3.0 layered memory
│   ├── org/                       # Company-wide, 2-approval merges
│   │   └── mission.md
│   ├── team/                      # PR-reviewed team state
│   │   └── platform/
│   │       ├── roadmap.yaml
│   │       ├── risks.yaml
│   │       ├── personas.yaml
│   │       ├── stakeholders.yaml
│   │       └── digests/
│   ├── personal/                  # Gitignored per-PM notes
│   │   └── README.md              # Format reference
│   ├── decisions/                 # ADRs — immutable once merged
│   │   └── adr-0001-adopt-team-shared-memory.md
│   ├── schemas/                   # JSON Schema draft-07 for every YAML
│   │   ├── profile.schema.json
│   │   ├── roadmap.schema.json
│   │   ├── risks.schema.json
│   │   ├── personas.schema.json
│   │   └── stakeholders.schema.json
│   ├── user-profile.md            # Deprecated stub (kept for legacy)
│   └── schema.md                  # Legacy schema docs
│
├── scripts/                       # v3.0 automation
│   ├── sync_trackers.py           # Linear/Jira → roadmap.yaml
│   └── staleness_scan.py          # Opens GitHub issues for stale files
│
├── context/                       # Legacy narrative context (fallback)
│   ├── company/
│   │   ├── mission.md
│   │   ├── competitors.md
│   │   ├── customer-feedback.md
│   │   ├── analytics-baseline.md
│   │   └── past-prds.md
│   ├── product/
│   │   ├── personas.md
│   │   └── roadmap.md
│   └── templates/
│       ├── prd-template.md
│       ├── research-synthesis-template.md
│       ├── stakeholder-update-template.md
│       └── weekly-report-template.md
│
├── outputs/                       # Generated deliverables (gitignored)
│
└── demos/                         # Example outputs
    ├── demo-prd-generation.md
    ├── demo-feedback-analysis.md
    ├── demo-strategy-review.md
    └── demo-stakeholder-update.md
```

---

## Frameworks Embedded

PM Operating System encodes the reasoning processes of the PM field's best practitioners. Every skill cites its source and applies the framework's actual methodology — not a surface-level summary.

| Practitioner | Frameworks | Used In |
|---|---|---|
| **Teresa Torres** | Opportunity Solution Tree, Continuous Discovery Habits | Discovery skills, `/discover` |
| **Marty Cagan** | Empowered product teams, outcomes not output | Strategy skills, quality bar on every output |
| **Bob Moesta / Clay Christensen** | Jobs-to-be-Done (demand-side), Four Forces | JTBD analysis, Switch interview, `/write-prd` |
| **Hamilton Helmer** | 7 Powers competitive moats | Seven Powers skill, `/strategy-review` |
| **Shreyas Doshi** | 3 levels of product work, pre-mortem | Product work levels, pre-mortem, `/strategy-review` |
| **April Dunford** | Obviously Awesome 5-component positioning | Positioning skill, `/competitive-intel`, `/plan-launch` |
| **Hamel Husain + Shreya Shankar** | Open coding, axial coding, LLM-as-judge evals | AI eval skills, `/design-ai-feature` |
| **Aparna Chennapragada** | NLX as the new UX | NLX design, prototyping skills |
| **Jackie Bavaro** | PM career arc frameworks | Career skills |
| **Lenny Rachitsky** | North Star guide, PRD guide, 14 PM habits | Metrics skills, PRD authoring, `/setup-metrics` |
| **Tal Raviv** | Hire, Onboard, Kickoff, Put to Work | Onboarding wizard |
| **Michael Nygard** | ADR (Architecture Decision Records) | `/adr` command |
| **OpenGitOps** | Declarative, versioned, pulled, continuously reconciled | Team memory governance |

---

## Customization

### Adding your context

Personal context lives in your gitignored personal profile. Team context lives in the shared team YAML files.

**Personal (private to you):**
- `memory/personal/<user>.md` — auto-created by `/onboarding`. Free-form notes + YAML frontmatter (see `memory/personal/README.md` for the format).

**Team (shared, PR-reviewed):**
- `memory/team/<team>/roadmap.yaml` — Now / Next / Later with initiative IDs, strategic bets, tracker links
- `memory/team/<team>/personas.yaml` — user personas with JTBD, pains, gains, evidence
- `memory/team/<team>/stakeholders.yaml` — internal stakeholders, comms style, influence
- `memory/team/<team>/risks.yaml` — active risks with severity, likelihood, mitigation

Every YAML file has a JSON Schema in `memory/schemas/` that CI enforces on every PR.

**Org (rarely edited, 2 approvals):**
- `memory/org/mission.md` — company mission, stage, values
- Add `competitive-landscape.md`, `pricing-decisions.md` as needed

**Legacy narrative context** in `context/` remains supported as fallback for skills that haven't migrated to YAML consumption. Prefer `memory/team/**/*.yaml` when both exist.

### Adjusting the quality bar

Edit `CLAUDE.md` to change global behavior:
- Modify the **Session Start Protocol** to change what gets loaded and in what order
- Adjust **Framework Defaults** to swap in your preferred frameworks
- Change **Output Conventions** for different scoring scales, output formats, or save paths
- Extend the **Trust Boundary** section if you add new destructive MCP actions

### Adding your own skills

Create a new folder under `skills/` with a `SKILL.md` file. Claude Code auto-discovers all skills at `skills/[name]/SKILL.md` — no registration needed.

```markdown
---
name: your-skill-name
description: When to trigger this skill and when not to
version: 1.0.0
---

Your skill instructions here. Follow the pattern:
1. Use loaded context (org + team + personal — already in the session)
2. Do the work
3. Produce output
4. Route writes by scope: personal (direct), team (via /promote-memory), org (direct PR), decisions (via /adr)
```

### Onboarding a new PM to an existing team

1. Clone the repo
2. Copy `.env.example` → `.env`, fill in your own tokens
3. Add your username to `.pm-os.yaml` under `members`
4. Run `/onboarding` — the wizard writes to `memory/personal/<your-username>.md` and offers to promote team-relevant answers via `/promote-memory`
5. Start your first session with `/brief-me` — you'll see the team roadmap, active risks, and recent ADRs immediately

---

## FAQ

**Does PM Operating System work without any MCP connectors?**
Yes. Every command has a no-connector fallback. You lose live data pulls, but all frameworks, memory, and skill logic work fully. The `tracker-sync` workflow just no-ops if tracker credentials aren't configured.

**Does it work without filling in the memory profile?**
Yes, but it will prompt you to onboard. Commands without memory context ask 3 targeted questions, proceed with the answers, and offer to save to memory afterward.

**Can I use it with both Linear and Jira?**
Yes. Configure both and commands will pull from whichever is connected. If both are active, both are queried. In the team roadmap YAML, each initiative points at either a `linear_project_id` or a `jira_epic_key` — the sync script routes accordingly.

**How is memory different from chat history?**
Chat history resets each session. Memory persists across sessions across three layers: personal notes stay local and private, team memory is shared via PR, org memory is company-wide. Every layer is inspectable, editable, and version-controlled.

**Can I use this as a solo PM (not a team)?**
Yes. Solo mode is a subset of team mode — you become the only member of `.pm-os.yaml`. Personal memory works exactly as before. Team YAML files still add structure and CI validation over free-form markdown. Skip the promotion flow if there's no one to promote to.

**How do I promote a personal note into shared team memory?**
Run `/promote-memory <what to promote>`. It opens a PR into `memory/team/<team>/*.yaml`, routed to your team's CODEOWNERS. Your teammates review, and if approved, it becomes team truth.

**What happens when two PMs edit the same team file?**
Structured YAML files (roadmap, risks, personas, stakeholders) are line-mergeable — git handles most conflicts cleanly. Free-form markdown (digests, ADRs) is naturally single-writer or append-only. If a merge conflict does occur, resolve it in the PR before the CODEOWNERS review.

**Can I trust shared team memory as trusted instruction?**
No — treat `memory/team/**` and `memory/org/**` as untrusted input. The prompt-injection scanner in `validate.yml` catches obvious triggers, but sophisticated attacks slip through. `CLAUDE.md` codifies the rule: never take destructive MCP actions (Linear delete, Notion overwrite, Slack broadcast) based purely on shared-memory content — require human confirmation.

**Can I use this on Claude.ai web?**
Skills and CLAUDE.md work on Claude.ai web through Projects. Slash commands, MCP connectors, and the SessionStart hook require Claude Code or Cowork.

**Is my data sent anywhere?**
No. Everything runs locally. Personal memory stays on your machine (gitignored). Team memory is in your GitHub repo — you control access. MCP connectors connect directly to your tools' APIs; nothing routes through a third party.

**What if I want to reverse a decision that's already an ADR?**
Create a new ADR with `supersedes: [ADR-XXXX]` and update the old ADR's `superseded_by: ADR-YYYY` field (this is the one edit allowed on a merged ADR — a link update, no semantic change). ADRs are the archaeology; superseding preserves the trail.

---

## License

Apache 2.0 — free to use, modify, and distribute. See [LICENSE](LICENSE).

---

*PM Operating System | Product Faculty | v3.0 — Team-Aware*

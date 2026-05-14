# The AI-Native PM Operating System

### Plugin for Claude Code, Claude Cowork, Claude Desktop, and Claude.AI Web || Product Faculty

Stop working like a 2022 PM. Start operating like an AI-native one.

PM Copilot is your AI Product Manager and an AI operating system for your product work.

65+ embedded PM skills across 12 domains
17 command-based workflows (end-to-end execution, not prompts)
8 specialized sub-agents (discovery, strategy, GTM, metrics, etc.)
Persistent memory that evolves with your product

Every command pulls your full context, connects to your tools, and executes like a real operator.

It’s time to become a 100x Product Manager.

Built by Product Faculty: We run [#1 AI PM Certification](https://maven.com/product-faculty/ai-product-management-certification?promoCode=git) - trusted by 3,000+ PMs (1,000+ reviews) learning how to build and operate AI-native products.

---

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [What's Inside](#whats-inside)
  - [17 Slash Commands](#17-slash-commands)
  - [65 PM Skills Across 12 Domains](#65-pm-skills-across-12-domains)
  - [8 Specialized Sub-Agents](#8-specialized-sub-agents)
  - [Persistent User Memory](#persistent-user-memory)
  - [Live Tool Connectors (MCP)](#live-tool-connectors-mcp)
  - [Gossip Mode](#gossip-mode)
- [Platform Guide](#platform-guide)
  - [Claude Code (CLI)](#claude-code-cli)
  - [Claude Cowork (Desktop)](#claude-cowork-desktop)
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
claude plugin install https://github.com/yourorg/pm-aios
```

### Claude Cowork (Desktop)

1. Open Claude Desktop and switch to the **Cowork** tab
2. Click **Customize** in the left sidebar
3. Click **Browse plugins** or upload the plugin folder directly
4. PM Copilot appears in your plugin list — click **Install**

### First Run

On first run, PM Copilot launches the onboarding wizard automatically. It asks 10 questions about your product, stack, stakeholders, and working style — then writes your persistent memory profile. Takes about 5 minutes, and you never have to re-brief Claude again.

You can also trigger it manually:

```
/onboarding
```

Or just say: *"I want to set up PM Copilot"*

---

## Quick Start

Once installed and onboarded:

| What you want to do | Command |
|---|---|
| Set up your PM profile (first time) | `/onboarding` |
| Start your day with a briefing | `/brief-me` |
| Write a PRD from a feature idea | `/write-prd smart notifications for enterprise users` |
| Review your roadmap | `/roadmap` |
| Send a stakeholder update | `/stakeholder-update` |
| Run a strategy review | `/strategy-review` |
| Triage user feedback | `/triage-feedback` |

Every command pulls your memory profile, loads relevant context files, and connects to your live tools (Linear, Jira, Slack, Notion) if configured. No re-briefing, no context-setting — just go.

---

## What's Inside

### 17 Slash Commands

Commands are chained workflows that wire multiple skills together into end-to-end operations.

| Command | What it does |
|---|---|
| `/onboarding` | First-run setup wizard — 10 questions about your product, stack, stakeholders, and working style. Writes your persistent memory profile |
| `/brief-me` | Your morning briefing — loads memory, pulls live state from all connected tools, surfaces risks and staleness, recommends where to start |
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

### 65 PM Skills Across 12 Domains

Skills are the atomic units of PM knowledge. Each skill lives in `skills/[name]/SKILL.md`, fires automatically when relevant, and can also be invoked directly. Every skill loads your memory profile and offers to update it when done.

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

### Persistent User Memory

PM Copilot maintains a structured memory profile (`memory/user-profile.md`) that grows with every session. It stores:

- **Product context** — name, stage, core user problem, business model, current bets
- **Stack** — issue tracker, docs tool, comms tool, analytics tool, design tool
- **Working style** — PRD format preference, verbosity level, preferred frameworks, things to avoid
- **Stakeholders** — names, roles, communication styles, sensitivities, interaction history
- **Roadmap state** — Now / Next / Later items with dates, owners, and decisions
- **Open questions** — unresolved assumptions with dates (auto-surfaced when stale)
- **Tracked risks** — active risks with status (auto-prompted for review every 7 days)
- **Lessons learned** — insights from retros, tied to specific initiatives

**Session start protocol:** Every session, PM Copilot checks your memory for staleness (>7 days), aged open questions (>14 days), upcoming milestones (<7 days), and overdue roadmap items — then surfaces what needs attention before you even ask.

**Session end protocol:** After any meaningful session (PRD written, roadmap decision made, risk surfaced), PM Copilot offers to update your memory so the next session starts with full context.

### Live Tool Connectors (MCP)

Connect once, and every command pulls live data from your actual stack:

| Tool | What PM Copilot reads | What PM Copilot writes |
|---|---|---|
| **Linear** | Issues, roadmap state, sprint backlog, blockers | Tickets, status updates |
| **Jira** | Board, backlog, sprint state, blockers | Issues, status updates |
| **Notion** | Spec pages, knowledge base, meeting notes | Spec drafts, research docs |
| **Slack** | Channel context, thread sentiment, decisions, @mentions | Stakeholder updates |
| **GitHub** | Issue backlog, PR velocity, engineering output | — |

All connectors are optional. PM Copilot works fully without them — it just can't pull live data from your tools. Commands gracefully skip any connector that isn't configured.

### Gossip Mode

Speak informally — voice-to-text, stream-of-consciousness, "you won't believe what happened in standup" — and PM Copilot parses it into structured memory updates. It extracts stakeholder signals, roadmap changes, risks, decisions, and team dynamics, then offers to save them. Designed to complete in under 60 seconds.

---

## Platform Guide

PM Copilot runs on every Claude surface. Here's what to know for each.

### Claude Code (CLI)

This is the full-power experience. Everything works out of the box:

- All 17 slash commands via `/command-name`
- All 65 skills fire automatically based on context
- 8 specialized sub-agents for complex multi-step workflows
- MCP connectors via `.mcp.json` (Linear, Jira, Notion, Slack, GitHub)
- Sub-agent parallelism for commands like `/brief-me` and `/roadmap`
- File I/O for reading context, writing outputs, and updating memory
- `CLAUDE.md` loads automatically as global instructions

**Requirements:** Claude Code CLI installed, Node.js (for MCP servers via npx)

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

**Requirements:** Claude Desktop app with Cowork enabled (Pro or Max subscription, macOS)

---

## MCP Setup (Claude Code)

The `.mcp.json` file in the project root configures five MCP servers. Set environment variables for the connectors you use:

```bash
# Linear
export LINEAR_API_KEY=lin_api_...

# Jira
export JIRA_URL=https://yourorg.atlassian.net
export JIRA_EMAIL=you@company.com
export JIRA_API_TOKEN=...

# Notion
export NOTION_API_KEY=secret_...

# Slack
export SLACK_BOT_TOKEN=xoxb-...
export SLACK_TEAM_ID=T...

# GitHub
export GITHUB_TOKEN=ghp_...
```

Only configure the tools you use. Unconfigured connectors are silently skipped.

---

## Connector Setup (Claude Cowork)

In Cowork, connectors are managed through the UI instead of `.mcp.json`:

1. Open **Customize** in the Cowork sidebar
2. Go to **Connectors**
3. Search for and connect the tools you use: **Linear**, **Jira**, **Notion**, **Slack**, **GitHub**
4. Authenticate through each connector's OAuth flow

Once connected, PM Copilot commands automatically pull live data from your tools — no environment variables or config files needed.

---

## Project Structure

```
pm-copilot/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest (name, version, metadata only)
├── .mcp.json                    # MCP server config (Claude Code only)
├── CLAUDE.md                    # Global instructions loaded every session
│
├── commands/                    # 17 slash commands (chained workflows)
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
│   └── weekly-digest.md
│
├── agents/                      # 8 specialized sub-agents (isolated workers)
│   ├── discovery-researcher.md
│   ├── strategy-analyst.md
│   ├── document-writer.md
│   ├── stakeholder-communicator.md
│   ├── market-researcher.md
│   ├── metrics-analyst.md
│   ├── gtm-planner.md
│   └── ai-evaluator.md
│
├── skills/                      # 65 skills — flat structure (skills/[name]/SKILL.md)
│   ├── memory/SKILL.md          # System
│   ├── onboarding/SKILL.md
│   ├── gossip/SKILL.md
│   ├── problem-framing/SKILL.md # Discovery (7)
│   ├── jtbd-analysis/SKILL.md
│   ├── ...
│   ├── vision-setting/SKILL.md  # Strategy (9)
│   ├── seven-powers/SKILL.md
│   ├── ...
│   ├── prd-authoring/SKILL.md   # Execution (5)
│   ├── ...
│   ├── exec-summary/SKILL.md    # Stakeholder (6)
│   ├── ...
│   ├── persona-development/SKILL.md  # Market & Users (6)
│   ├── ...
│   ├── ab-test-design/SKILL.md  # Metrics (6)
│   ├── ...
│   ├── error-analysis/SKILL.md  # AI Evals (6)
│   ├── ...
│   ├── launch-planning/SKILL.md # GTM (7)
│   ├── ...
│   ├── vibe-coding/SKILL.md     # Prototyping (5)
│   ├── ...
│   └── founding-pm/SKILL.md     # Career (5)
│
├── context/                     # Your product context (you fill these in)
│   ├── company/
│   │   ├── mission.md           # Company mission, stage, values
│   │   ├── competitors.md       # Competitive landscape
│   │   ├── customer-feedback.md # Recurring feedback themes
│   │   ├── analytics-baseline.md # Metric definitions and baselines
│   │   └── past-prds.md         # Previous PRDs for tone reference
│   ├── product/
│   │   ├── personas.md          # User personas (or use template)
│   │   └── roadmap.md           # Current roadmap (or use template)
│   └── templates/
│       ├── prd-template.md
│       ├── research-synthesis-template.md
│       ├── stakeholder-update-template.md
│       └── weekly-report-template.md
│
├── memory/
│   ├── user-profile.md          # Your persistent PM memory (auto-managed)
│   └── schema.md                # Memory schema documentation
│
├── outputs/                     # Generated deliverables saved here
│
└── demos/                       # Example outputs
    ├── demo-prd-generation.md
    ├── demo-feedback-analysis.md
    ├── demo-strategy-review.md
    └── demo-stakeholder-update.md
```

---

## Frameworks Embedded

PM Copilot encodes the reasoning processes of the PM field's best practitioners. Every skill cites its source and applies the framework's actual methodology — not a surface-level summary.

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

---

## Customization

### Adding Your Context

The more context you provide, the better PM Copilot performs. Fill in the files under `context/`:

1. **`context/company/mission.md`** — Your company's mission, stage (pre-seed, seed, Series A, etc.), and core values. This calibrates all scoring and recommendations.
2. **`context/company/competitors.md`** — Key competitors and how you differentiate. Feeds battlecard generation and positioning skills.
3. **`context/company/customer-feedback.md`** — Recurring themes from support tickets, NPS, reviews. Grounds feedback triage in real signal.
4. **`context/product/personas.md`** — Your user personas. Use the template at `context/product/personas-template.md` to get started.
5. **`context/product/roadmap.md`** — Your current roadmap. Use the template at `context/product/roadmap-template.md`.

### Adjusting the Quality Bar

Edit `CLAUDE.md` to change global behavior:
- Modify the **Session Start Protocol** to change what gets surfaced on each session
- Adjust **Framework Defaults** to swap in your preferred frameworks
- Change **Output Conventions** for different scoring scales, output formats, or save paths

### Adding Your Own Skills

Create a new folder under `skills/` with a `SKILL.md` file. Claude Code auto-discovers all skills at `skills/[name]/SKILL.md` — no registration needed.

```markdown
---
name: your-skill-name
description: When to trigger this skill and when not to
version: 2.0.0
---

Your skill instructions here. Follow the pattern:
1. Load context (memory + relevant files)
2. Do the work
3. Produce output
4. Offer to save and update memory
```

---

## FAQ

**Does PM Copilot work without any MCP connectors?**
Yes. Every command has a no-connector fallback. You lose live data pulls, but all frameworks, memory, and skill logic work fully.

**Does it work without filling in the memory profile?**
Yes, but it will prompt you to onboard. Commands without memory context ask 3 targeted questions, proceed with the answers, and offer to save to memory afterward.

**Can I use it with both Linear and Jira?**
Yes. Configure both and commands will pull from whichever is connected. If both are active, both are queried.

**How is memory different from chat history?**
Chat history resets each session. Memory persists across sessions in `memory/user-profile.md` — it's a structured file you can read, edit, or delete at any time.

**Can I use this on Claude.ai web?**
Skills and CLAUDE.md work on Claude.ai web through Projects. Slash commands and MCP connectors require Claude Code or Cowork.

**Is my data sent anywhere?**
No. Everything runs locally. Memory, context files, and outputs stay on your machine. MCP connectors connect directly to your tools' APIs — nothing routes through a third party.

---

## License

Apache 2.0 — free to use, modify, and distribute. See [LICENSE](LICENSE).

---

*PM Copilot | Product Faculty | v2.1*

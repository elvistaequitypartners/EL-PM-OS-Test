---
id: ADR-0001
title: Adopt three-layer team-shared memory model
status: proposed
date: 2026-07-02
deciders: [elandon@vistaequitypartners.com]
supersedes: []
superseded_by: null
---

## Context

PM Operating System today is single-user. `memory/user-profile.md` is a single
file per repo, `.mcp.json` assumes one workspace per tool, and 65+ skills hard-
code the singular profile path. Two PMs cannot use the same install without
last-writer-wins overwrites of product context, roadmap state, risks, and
lessons.

Team adoption at Vista Equity Partners requires:

- Multiple PMs sharing product / roadmap context through git
- Personal notes staying private
- Decisions being auditable and durable
- Shared content being treated as untrusted (OWASP LLM Agentic memory poisoning)
- No manual sync friction — session start should reflect latest team state
  automatically

## Decision

Adopt a three-layer memory model with GitOps governance:

1. **`memory/personal/<user>.md`** — gitignored per-PM notes. Default write scope.
2. **`memory/team/<team>/*.yaml`** — machine-mergeable team state
   (roadmap, risks, personas, stakeholders). Free-form narrative
   (`digests/`) stays markdown and is append-only.
3. **`memory/org/*.md`** — company-wide mission, competitive landscape,
   pricing decisions. Two approvals required to merge.
4. **`memory/decisions/adr-NNNN-*.md`** — ADR-style decision records,
   immutable once merged (superseded, never edited).

Session load precedence: `org → team → personal → recent decisions`.
Personal wins on conflict but never leaks upward. Promotion between layers
is explicit via `/promote-memory` (opens a PR).

GitOps enforcement:

- SessionStart hook runs `git pull --rebase` so every session sees latest state
- CI validates JSON Schemas on every PR
- CODEOWNERS routes review to the right scope owner
- Staleness bot opens issues for files >30 days without `last_updated` refresh
- Prompt-injection scanner blocks obvious triggers in shared content

Tracker integration: Pattern 3 (split ownership by field). PM-owned fields
(`id`, `title`, `strategic_bet`, `adr_refs`) live in YAML. Machine-owned
`tracker_*` fields are synced from Linear/Jira by an hourly workflow that
opens a PR on drift.

## Consequences

**Positive**
- Multiple PMs share context without collision
- Personal notes stay private by construction
- Decision audit trail via ADRs replaces "why did we decide X" archaeology
- SessionStart hook makes staleness a system property, not a discipline

**Negative**
- 65+ skills and 17 commands must be refactored to the layered loader (INIT-0143)
- PR review adds latency to team memory updates
- Structured YAML costs authoring speed vs. free-form markdown
- Now running a mini-platform (schemas, CI, CODEOWNERS) — needs a maintainer

**Neutral**
- CLAUDE.md session start protocol unchanged in this ADR — coexistence
  period until skill refactor lands (see RISK-0001)
- MCP workspace parity assumed — different Linear teams per PM handled in
  a follow-up ADR

## Alternatives considered

- **Per-PM install with no sharing.** Rejected: defeats the purpose of a
  team OS; loses the shared context asset.
- **Single shared file with sections per PM.** Rejected: git line-merge fails
  on free-form markdown and section boundaries drift.
- **Vendor memory system (Mem0 / Letta / Zep).** Rejected for v1: adds runtime
  dependency, opaque state, and lock-in. GitOps gives us `git blame`, `git
  revert`, and human-readable audit for free. Reconsider at ~10+ PMs.
- **Force everything through Linear/Jira.** Rejected: trackers are for
  execution state, not strategy or decision rationale.

## References

- `PMOS_Readme.md` — full design proposal (this ADR is its condensed decision form)
- [Claude Code — Manage memory](https://code.claude.com/docs/en/memory)
- [OpenGitOps Principles v1.0.0](https://github.com/open-gitops/documents/blob/main/PRINCIPLES.md)
- [Letta — Multi-agent shared memory](https://docs.letta.com/guides/agents/multi-agent-shared-memory)
- [Mem0 — Entity-scoped memory](https://docs.mem0.ai/platform/features/entity-scoped-memory)
- [OWASP Top 10 for LLM Agentic Applications](https://www.trydeepteam.com/docs/frameworks-owasp-top-10-for-agentic-applications)

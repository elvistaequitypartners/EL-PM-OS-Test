# PM Operating System — User Memory Profile (deprecated)

> **This file is deprecated.** As of ADR-0001 (see `memory/decisions/adr-0001-adopt-team-shared-memory.md`), PM Operating System uses a three-layer memory model:
>
> - **Personal notes** → `memory/personal/${USER}.md` (gitignored, per-PM)
> - **Team-shared state** → `memory/team/${CURRENT_TEAM}/*.yaml` (schema-validated, PR-reviewed)
> - **Org-wide context** → `memory/org/*.md` (2-approval merges)
> - **Durable decisions** → `memory/decisions/adr-NNNN-*.md` (immutable ADRs)
>
> See `memory/personal/README.md` for the personal-profile format and `memory/schemas/` for team YAML schemas.

## Migration

If you were using the old single-file profile:

1. Create your personal file: `memory/personal/<your-username>.md` where `<your-username>` is the local-part of your git `user.email`. Follow the format in `memory/personal/README.md`.
2. Anything that was team-relevant in your old profile (roadmap, personas, stakeholders, risks) belongs in `memory/team/${CURRENT_TEAM}/*.yaml`. Use `/promote-memory` to open a PR for each item.
3. Anything that was a durable decision belongs in an ADR — use `/adr` to create one.
4. Once migrated, this file is safe to delete (kept as a stub to avoid breaking any legacy skill that still references it during the coexistence period).

## For new PMs

Run `/onboarding` — the wizard now writes to `memory/personal/${USER}.md` directly and offers to promote team-relevant answers via `/promote-memory`.

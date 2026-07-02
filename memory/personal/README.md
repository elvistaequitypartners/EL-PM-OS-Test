# memory/personal/

Personal PM memory. **This directory is gitignored** — files here belong to the individual PM and are never shared.

## Naming

`memory/personal/<user>.md` where `<user>` is the local-part of your git `user.email` (the part before the `@`).

Example: `elandon@vistaequitypartners.com` → `memory/personal/elandon.md`

## Format

YAML frontmatter validated by `memory/schemas/profile.schema.json`, followed by free-form markdown notes.

```yaml
---
user: elandon
last_updated: 2026-07-02
role: Senior PM
team: platform
current_focus: Team-shared memory rollout
working_style:
  prd_format_preference: standard
  verbosity: balanced
  preferred_frameworks: [JTBD, OST, 7 Powers]
  avoid: [feature-factory metrics]
open_questions:
  - question: How do we handle cross-team roadmap dependencies?
    raised: 2026-07-01
---

# Notes

Free-form personal notes go here.
```

## Promotion

To move a fact from personal memory into team scope, run `/promote-memory` — it opens a PR into `memory/team/<team>/*` for review. Never edit team files directly from a personal session.

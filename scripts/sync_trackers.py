"""
Sync tracker state (Linear projects, Jira epics) into roadmap YAML files.

For each initiative with a `linear_project_id` or `jira_epic_key`, fetch the
current status/target_date/owner from the tracker and write into the
machine-owned `tracker_*` fields. PM-owned fields are never touched.

Run by .github/workflows/tracker-sync.yml on an hourly cron.

USAGE
    python scripts/sync_trackers.py memory/team/*/roadmap.yaml

ENV
    LINEAR_API_KEY
    JIRA_URL / JIRA_EMAIL / JIRA_API_TOKEN

This is intentionally a sketch — production version needs proper HTTP error
handling, retry with backoff, rate-limit awareness, and unit tests over the
map_* functions.
"""

from __future__ import annotations

import datetime as dt
import glob
import os
import sys
from pathlib import Path
from typing import Any

import yaml

try:
    import requests
except ImportError:  # allow importing without deps for typing checks
    requests = None  # type: ignore[assignment]


LINEAR_API = "https://api.linear.app/graphql"


# --------------------------------------------------------------------------- #
# Status mapping — differs per tracker. Unit-test the shit out of these.
# --------------------------------------------------------------------------- #

_LINEAR_STATUS_MAP = {
    "backlog": "planned",
    "planned": "planned",
    "started": "in-progress",
    "in progress": "in-progress",
    "at risk": "at-risk",
    "blocked": "blocked",
    "completed": "shipped",
    "cancelled": "cancelled",
    "canceled": "cancelled",
}

_JIRA_STATUS_MAP = {
    "to do": "planned",
    "in progress": "in-progress",
    "blocked": "blocked",
    "at risk": "at-risk",
    "done": "shipped",
    "cancelled": "cancelled",
}


def map_linear_state(state: str) -> str:
    return _LINEAR_STATUS_MAP.get(state.lower().strip(), "planned")


def map_jira_status(status: str) -> str:
    return _JIRA_STATUS_MAP.get(status.lower().strip(), "planned")


# --------------------------------------------------------------------------- #
# Fetch helpers
# --------------------------------------------------------------------------- #


def fetch_linear_project(project_id: str, api_key: str) -> dict[str, Any] | None:
    query = """
    query($id: String!) {
      project(id: $id) {
        id
        name
        state
        targetDate
        lead { email }
      }
    }
    """
    resp = requests.post(  # type: ignore[union-attr]
        LINEAR_API,
        json={"query": query, "variables": {"id": project_id}},
        headers={"Authorization": api_key},
        timeout=15,
    )
    resp.raise_for_status()
    return resp.json().get("data", {}).get("project")


def fetch_jira_epic(
    epic_key: str, url: str, email: str, token: str
) -> dict[str, Any] | None:
    resp = requests.get(  # type: ignore[union-attr]
        f"{url}/rest/api/3/issue/{epic_key}",
        auth=(email, token),
        headers={"Accept": "application/json"},
        timeout=15,
    )
    resp.raise_for_status()
    return resp.json()


# --------------------------------------------------------------------------- #
# Sync a single initiative
# --------------------------------------------------------------------------- #


def sync_initiative(init: dict[str, Any]) -> dict[str, Any]:
    now = dt.datetime.now(dt.timezone.utc).isoformat()

    if init.get("linear_project_id"):
        key = os.environ.get("LINEAR_API_KEY")
        if not key:
            print(f"skip {init['id']}: LINEAR_API_KEY not set")
            return init
        proj = fetch_linear_project(init["linear_project_id"], key)
        if proj:
            init["tracker_status"] = map_linear_state(proj.get("state", ""))
            if proj.get("targetDate"):
                init["target_date"] = proj["targetDate"]
            lead = proj.get("lead") or {}
            if lead.get("email"):
                init["owner"] = lead["email"]
            init["tracker_synced_at"] = now

    elif init.get("jira_epic_key"):
        url = os.environ.get("JIRA_URL")
        email = os.environ.get("JIRA_EMAIL")
        token = os.environ.get("JIRA_API_TOKEN")
        if not (url and email and token):
            print(f"skip {init['id']}: Jira creds not set")
            return init
        epic = fetch_jira_epic(init["jira_epic_key"], url, email, token)
        if epic:
            fields = epic.get("fields", {}) or {}
            status = (fields.get("status") or {}).get("name", "")
            init["tracker_status"] = map_jira_status(status)
            if fields.get("duedate"):
                init["target_date"] = fields["duedate"]
            assignee = fields.get("assignee") or {}
            if assignee.get("emailAddress"):
                init["owner"] = assignee["emailAddress"]
            init["tracker_synced_at"] = now

    return init


# --------------------------------------------------------------------------- #
# File-level sync
# --------------------------------------------------------------------------- #


def sync_file(path: str) -> bool:
    """Return True if the file was modified."""
    p = Path(path)
    doc = yaml.safe_load(p.read_text()) or {}
    changed = False
    for bucket in ("now", "next", "later"):
        for i, init in enumerate(doc.get(bucket, []) or []):
            before = dict(init)
            after = sync_initiative(init)
            if after != before:
                doc[bucket][i] = after
                changed = True
    if changed:
        doc["last_updated"] = dt.date.today().isoformat()
        p.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True))
    return changed


def main(argv: list[str]) -> int:
    if requests is None:
        print("requests not installed — install with `pip install requests pyyaml`", file=sys.stderr)
        return 2
    if len(argv) < 2:
        print(__doc__)
        return 1
    patterns = argv[1:]
    files: list[str] = []
    for pattern in patterns:
        files.extend(glob.glob(pattern))
    if not files:
        print("no roadmap files matched", file=sys.stderr)
        return 0
    any_changed = False
    for f in files:
        if sync_file(f):
            any_changed = True
            print(f"updated: {f}")
        else:
            print(f"unchanged: {f}")
    return 0 if any_changed or True else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

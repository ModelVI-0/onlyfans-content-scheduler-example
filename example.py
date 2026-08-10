"""
onlyfans-content-scheduler-example  —  scheduler.py

A minimal, runnable-SHAPED example of a content scheduler for creators:
define a content calendar, schedule each item, and auto-publish items as they
come due, using the ModelVI posting API.

  → Get your API key at https://modelvi.com
  → Real endpoints & payloads:  https://modelvi.com/docs

IMPORTANT: This is an EXAMPLE. The endpoint paths and request bodies below are
clearly-marked PLACEHOLDERS that show the *shape* of an integration. Replace them
with the real endpoints from https://modelvi.com/docs before using for real. This
file does not assume or invent a specific live response schema.

Usage:
    python scheduler.py schedule    # queue every item in the content calendar
    python scheduler.py publish     # publish items whose scheduled time has passed
"""

import os
import sys
import time
from datetime import datetime, timezone, timedelta

import requests  # pip install requests


# ---------------------------------------------------------------------------
# Configuration — read from environment (see .env.example). Never hard-code keys.
# ---------------------------------------------------------------------------
API_KEY = os.environ.get("API_KEY")

# BASE_URL is a PLACEHOLDER default. Replace with the real base URL from the docs.
BASE_URL = os.environ.get("BASE_URL", "https://api.modelvi.com")

if not API_KEY:
    print(
        "Missing API_KEY.\n"
        "  → Get your API key at https://modelvi.com and put it in your .env file.",
        file=sys.stderr,
    )
    sys.exit(1)


def _headers():
    """Auth headers. Confirm the exact scheme at https://modelvi.com/docs."""
    return {
        "Authorization": f"Bearer {API_KEY}",  # PLACEHOLDER auth scheme — verify in docs
        "Content-Type": "application/json",
    }


# ---------------------------------------------------------------------------
# The content calendar.
#
# In a real app this comes from a database, spreadsheet, or planning UI. Here it
# is just a list of dicts so the example stays dependency-free. Each item is a
# scheduled post: what to say, which media to attach, where, and when.
#
# `media_ref` is a reference you control (e.g. an ID or URL you have already
# uploaded to your own storage / to ModelVI). This example does not include or
# host any media — you supply your own references.
# ---------------------------------------------------------------------------
CONTENT_CALENDAR = [
    {
        "id": "post-001",
        "caption": "New behind-the-scenes update is live.",
        "media_ref": "REPLACE_WITH_YOUR_MEDIA_ID_OR_URL",
        "platform": "example-platform",              # target account/platform key
        "publish_at": datetime.now(timezone.utc) + timedelta(minutes=5),
    },
    {
        "id": "post-002",
        "caption": "Weekly roundup — thanks for following along.",
        "media_ref": "REPLACE_WITH_YOUR_MEDIA_ID_OR_URL",
        "platform": "example-platform",
        "publish_at": datetime.now(timezone.utc) + timedelta(hours=24),
    },
]


# ---------------------------------------------------------------------------
# schedule(): register each calendar item with the posting API.
# ---------------------------------------------------------------------------
def schedule():
    """Queue every item in the content calendar for future publishing."""
    for item in CONTENT_CALENDAR:
        payload = {
            # PLACEHOLDER request body. Field names/shape are illustrative —
            # use the real ones from https://modelvi.com/docs.
            "external_id": item["id"],
            "caption": item["caption"],
            "media": item["media_ref"],
            "platform": item["platform"],
            "scheduled_for": item["publish_at"].isoformat(),
        }

        # PLACEHOLDER endpoint — replace with the real endpoint from modelvi.com/docs
        url = f"{BASE_URL}/v1/schedule"

        resp = requests.post(url, json=payload, headers=_headers(), timeout=30)

        # We only report the HTTP status. We do NOT assume a specific response
        # schema here — inspect resp.json() against the real docs in your app.
        print(f"[schedule] {item['id']} -> HTTP {resp.status_code}")


# ---------------------------------------------------------------------------
# publish(): the auto-publish worker.
#
# Run this on a schedule (cron, systemd timer, a container loop, a serverless
# cron). It asks the API for anything due and publishes it. Below we show BOTH
# common shapes so you can pick whichever the real API supports:
#
#   (A) server-side scheduling: you already sent `scheduled_for`, and the API
#       publishes on time by itself — the worker just polls status.
#   (B) client-side scheduling: you keep the calendar and POST a publish call
#       for each item once its time has passed.
#
# This example implements (B) against the local CONTENT_CALENDAR so the pattern
# is fully visible. Prefer (A) if the real API supports it.
# ---------------------------------------------------------------------------
def publish():
    """Publish every calendar item whose scheduled time has passed."""
    now = datetime.now(timezone.utc)
    due = [i for i in CONTENT_CALENDAR if i["publish_at"] <= now]

    if not due:
        next_at = min((i["publish_at"] for i in CONTENT_CALENDAR), default=None)
        print(f"[publish] nothing due yet. Next item at: {next_at}")
        return

    for item in due:
        payload = {
            # PLACEHOLDER request body — align with https://modelvi.com/docs
            "external_id": item["id"],
            "caption": item["caption"],
            "media": item["media_ref"],
            "platform": item["platform"],
        }

        # PLACEHOLDER endpoint — replace with the real endpoint from modelvi.com/docs
        url = f"{BASE_URL}/v1/publish"

        resp = requests.post(url, json=payload, headers=_headers(), timeout=30)
        print(f"[publish] {item['id']} -> HTTP {resp.status_code}")


def main():
    command = sys.argv[1] if len(sys.argv) > 1 else "help"
    if command == "schedule":
        schedule()
    elif command == "publish":
        publish()
    else:
        print(__doc__.strip())


if __name__ == "__main__":
    main()

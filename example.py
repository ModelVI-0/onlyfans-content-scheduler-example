#!/usr/bin/env python3
"""
onlyfans-content-scheduler-example

Plan a content calendar and let ModelVI auto-publish each item on schedule,
across OnlyFans and 13 other creator platforms, via the public ModelVI partner API.

  Get your API key:  https://modelvi.com/sign-up
  API reference:     https://modelvi.com/agent-api  ·  https://modelvi.com/partner-api-docs

Minimal EXAMPLE (no retries/pagination/media upload). Public partner API only:
key -> endpoint -> result.

Usage:
    python example.py schedule    # queue every item in the content calendar
    python example.py results     # list delivery status (GET /schedule_result)
"""

import os
import sys
from datetime import datetime, timezone, timedelta

import requests  # pip install requests

BASE_URL = os.environ.get("MODELVI_API_BASE", "https://modelvi.com/api/partner/v1")
API_KEY = os.environ.get("MODELVI_API_KEY")
SIGNUP_URL = "https://modelvi.com/sign-up"

# Post type: 1 = FREE, 2 = FANS, 3 = PAID.
# A content calendar: caption + target platform CODES + when + type.
# `model` is filled in at runtime from GET /model_list.
CONTENT_CALENDAR = [
    {"title": "New behind-the-scenes update is live 💫",
     "platforms": ["ONLYFANS", "FAN"], "in_minutes": 5, "type": 1},
    {"title": "Weekly PPV drop — check your DMs",
     "platforms": ["ONLYFANS", "FNC", "MALOUM"], "in_minutes": 60, "type": 3},
]


def _headers():
    if not API_KEY:
        sys.exit(
            f"Missing MODELVI_API_KEY. Get a key at {SIGNUP_URL} and export it:\n"
            f'  export MODELVI_API_KEY="mvk_<keyId>_<secret>"'
        )
    return {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}


def _payload(resp):
    if resp.status_code == 401:
        sys.exit(f"Unauthorized (401). Get a valid key at {SIGNUP_URL}")
    resp.raise_for_status()
    body = resp.json()
    return body.get("payload", body)


def _first_model_id():
    models = _payload(requests.get(f"{BASE_URL}/model_list", headers=_headers(), timeout=30))
    if not models:
        sys.exit("No models on this account yet — add one in your ModelVI dashboard.")
    model = models[0] if isinstance(models, list) else models.get("items", [{}])[0]
    return model.get("id") or model.get("model")


def schedule():
    """Queue every calendar item with server-side scheduling (POST /schedule)."""
    model = _first_model_id()
    for item in CONTENT_CALENDAR:
        when = datetime.now(timezone.utc) + timedelta(minutes=item["in_minutes"])
        body = {
            "model": model,
            "platforms": item["platforms"],
            "title": item["title"],                       # caption field is `title`
            "scheduledAt": when.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "type": item["type"],
        }
        result = _payload(requests.post(f"{BASE_URL}/schedule", json=body,
                                        headers=_headers(), timeout=30))
        print(f"[scheduled] {item['title'][:32]!r} -> {', '.join(item['platforms'])}: {result}")


def results():
    """List scheduled-post delivery status (GET /schedule_result)."""
    print(_payload(requests.get(f"{BASE_URL}/schedule_result", headers=_headers(), timeout=30)))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"
    {"schedule": schedule, "results": results}.get(cmd, lambda: print(__doc__.strip()))()

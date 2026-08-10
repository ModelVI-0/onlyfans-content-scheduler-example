# OnlyFans content scheduler — plan a content calendar, auto-publish on schedule

A minimal **example integration** (Python) that schedules a content calendar and lets ModelVI auto-publish each item at its time — across OnlyFans and 13 other creator platforms — via the [ModelVI](https://modelvi.com/sign-up?utm_source=github&utm_medium=owned-track&utm_campaign=onlyfans-content-scheduler) partner API.

**[▶ Get your API key →](https://modelvi.com/sign-up?utm_source=github&utm_medium=owned-track&utm_campaign=onlyfans-content-scheduler)** · [API docs](https://modelvi.com/agent-api) · [Pricing](https://modelvi.com/pricing)

![example](https://img.shields.io/badge/example-MIT-blue) ![python](https://img.shields.io/badge/python-3.9+-green)

---

## What this is

An MIT-licensed **content scheduler** example: define a content calendar in plain code, then queue each item with a single `POST /schedule` call carrying `scheduledAt` (ISO-8601 UTC) — ModelVI publishes it on time. No UI, no database, just a readable script you can adapt. It talks only to the public ModelVI partner API.

**Supported platforms (codes):** `ONLYFANS FAN FNC F2F MALOUM LOYALFANS MYMFANS FETLIFE FOURBASED FANVUE BESTFANS FANSYME BREZZELS KNKY`.

## Quickstart

**1. Get your API key** → **[modelvi.com/sign-up](https://modelvi.com/sign-up?utm_source=github&utm_medium=owned-track&utm_campaign=onlyfans-content-scheduler)** (`mvk_<keyId>_<secret>`).

**2. Run**
```bash
pip install requests
export MODELVI_API_KEY="mvk_<keyId>_<secret>"
python example.py schedule    # queue the sample content calendar
python example.py results     # check delivery status
```

## How it works

Server-side scheduling: you send each post **once** with `scheduledAt`, and ModelVI publishes it at that time — no worker loop to babysit. `example.py` queues every calendar item via `POST /schedule` (fields: `model`, `platforms` [codes], `title` = caption, `scheduledAt`, `type` `1`=FREE/`2`=FANS/`3`=PAID), then reads delivery status via `GET /schedule_result`. Responses are wrapped in `{ "success": true, "payload": … }`.

## Use cases / keywords

**onlyfans content scheduler** · content calendar automation · posting automation · auto-publish scheduler · **fansly scheduler** · **maloum posting** · schedule onlyfans posts · creator posting API · plan a week of content once and let it publish itself.

## Honest note

Minimal example — no retries, pagination, or media upload. Authoritative endpoints: **[modelvi.com/agent-api](https://modelvi.com/agent-api)** · **[modelvi.com/partner-api-docs](https://modelvi.com/partner-api-docs)**. Public API only; no proprietary logic here.

**[▶ Get your API key →](https://modelvi.com/sign-up?utm_source=github&utm_medium=owned-track&utm_campaign=onlyfans-content-scheduler)** — see [pricing](https://modelvi.com/pricing). MIT licensed.

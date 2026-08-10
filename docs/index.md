---
title: OnlyFans content scheduler — ModelVI example
description: Plan a content calendar and auto-publish it on schedule across 14 creator platforms via the ModelVI partner API.
---

# OnlyFans content scheduler — plan once, publish on schedule

A minimal, open **example integration** that schedules a content calendar and lets
[ModelVI](https://modelvi.com/sign-up?utm_source=github&utm_medium=owned-track&utm_campaign=onlyfans-content-scheduler)
auto-publish each item at its time — across OnlyFans and 13 other creator platforms.

## How it works

Send each post once with `scheduledAt` (ISO-8601 UTC) via `POST /schedule`; ModelVI
publishes it on time. Check delivery with `GET /schedule_result`. Responses are
`{ "success": true, "payload": … }`.

## Get started

1. **[Get your API key →](https://modelvi.com/sign-up?utm_source=github&utm_medium=owned-track&utm_campaign=onlyfans-content-scheduler)**
2. Reference: [modelvi.com/agent-api](https://modelvi.com/agent-api).
3. Clone, add your `mvk_` key, adapt the calendar.

## Use cases / keywords

onlyfans content scheduler · content calendar automation · posting automation ·
auto-publish scheduler · fansly scheduler · maloum posting · schedule onlyfans posts.

> **Minimal example.** Authoritative endpoints: [modelvi.com/agent-api](https://modelvi.com/agent-api) ·
> [modelvi.com/partner-api-docs](https://modelvi.com/partner-api-docs).

- API key: <https://modelvi.com/sign-up?utm_source=github&utm_medium=owned-track&utm_campaign=onlyfans-content-scheduler>
- Pricing: <https://modelvi.com/pricing>

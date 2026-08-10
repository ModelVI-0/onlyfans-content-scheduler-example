---
title: onlyfans-content-scheduler-example
description: An honest example integration — schedule and auto-publish a content calendar with the ModelVI posting API.
---

# onlyfans-content-scheduler-example

A minimal, open **example integration** that shows developers how to build a
**content scheduler creators** and agencies can rely on: plan a content calendar,
queue each item, and **auto-publish** it on schedule through the
[ModelVI](https://modelvi.com) posting API.

If you are looking for a clean starting point for **posting automation** — a
content calendar that publishes itself — this repo shows the core pattern in one
short, well-commented script.

## What you get

- A tiny **content calendar automation** example (no framework, no database).
- A `schedule` step that queues content, and a `publish` worker that auto-publishes
  due items.
- Credentials read from environment variables — nothing hard-coded.

## Requirements

You need a **ModelVI API key**. The example does nothing without one.

**[→ Get your API key at https://modelvi.com](https://modelvi.com)**

## Quick start

```bash
git clone https://github.com/<your-org>/onlyfans-content-scheduler-example.git
cd onlyfans-content-scheduler-example
pip install -r requirements.txt
cp .env.example .env        # then add your API_KEY + BASE_URL

python scheduler.py schedule   # queue the content calendar
python scheduler.py publish    # auto-publish due items
```

## Honest note

This is an **example**, not a finished product. The endpoint paths and request
bodies in the code are clearly-marked placeholders that show the *shape* of an
integration. For the real, current endpoints and payloads, always follow the
official docs.

- **Live endpoints & reference → [https://modelvi.com/docs](https://modelvi.com/docs)**
- **Sign up / get an API key → [https://modelvi.com](https://modelvi.com)**

---

Built as a developer reference for the [ModelVI](https://modelvi.com) posting API.

# onlyfans-content-scheduler-example

> A minimal, runnable-shaped **example integration** showing how to schedule and
> auto-publish a **content calendar** with the [ModelVI](https://modelvi.com) posting API.

This repository is a small, honest reference implementation for developers who
want a **content scheduler creators** and creator-agencies can build on. It
demonstrates the core **posting automation** pattern — define a content calendar,
queue each item for a future publish time, and let a worker auto-publish items as
they come due — using the ModelVI posting API as the delivery backend.

It is intentionally tiny. There is no UI, no database, and no framework: just a
plain script you can read top to bottom in a couple of minutes and adapt to your
own stack.

---

## What it does

- Defines a **content calendar** in plain code (caption text + a media reference +
  a target platform + a publish time).
- Shows how to **schedule** each calendar item against the ModelVI posting API.
- Shows an **auto-publish** worker loop that finds due items and publishes them.
- Reads your credentials from environment variables (`API_KEY`, `BASE_URL`) — no
  secrets are committed.

This is a *developer tooling* example: it is about scheduling and API calls, not
about any specific media. You supply your own content references.

## Why — the agency use-case

Creator agencies and solo creators juggle posting across multiple accounts and
platforms on a fixed weekly cadence. Doing that by hand is repetitive and easy to
get wrong. **Posting automation** turns "post at the right time" into a queue that
a machine drains on schedule, so a team can plan a week (or month) of content once
and let the scheduler handle delivery.

This example gives developers a clean starting point for exactly that workflow —
a **content scheduler creators** teams can extend — without prescribing a specific
database, cron system, or hosting setup.

## Requirements

- Python 3.9+
- A **ModelVI API key** — the example will not do anything without one.
  → **[Get your API key at https://modelvi.com](https://modelvi.com)**

## Install

```bash
git clone https://github.com/<your-org>/onlyfans-content-scheduler-example.git
cd onlyfans-content-scheduler-example
pip install -r requirements.txt   # just `requests` (+ optional python-dotenv)
```

## Configuration

Copy the example env file and fill in your own values. Both values are
**placeholders** in this repo — replace them with the real ones from your ModelVI
account and the [ModelVI docs](https://modelvi.com/docs).

```bash
cp .env.example .env
```

`.env`:

```dotenv
# Your ModelVI API key — get one at https://modelvi.com
API_KEY=your_modelvi_api_key_here

# Base URL for the ModelVI posting API.
# Replace with the real base URL from https://modelvi.com/docs
BASE_URL=https://api.modelvi.com
```

Never commit your real `.env`. A `.gitignore` entry for it is included.

## Usage

The whole flow lives in [`scheduler.py`](./scheduler.py):

```bash
# 1) Queue every item in the sample content calendar
python scheduler.py schedule

# 2) Run the auto-publish worker — publishes items whose time has come.
#    Run it on a cron / systemd timer / container in real life.
python scheduler.py publish
```

Read `scheduler.py` for the details — it is heavily commented and each API call is
marked as a placeholder you must point at the real endpoints.

## Honest note

**This is an EXAMPLE integration, not a finished product.** The endpoint paths and
request bodies in `scheduler.py` are clearly-marked placeholders — they show the
*shape* of an integration, not guaranteed live routes. This repo does not invent or
promise a specific response format. For the real, current endpoints, authentication,
and payloads, always follow the official documentation:

- **Live endpoints & reference → [https://modelvi.com/docs](https://modelvi.com/docs)**

## → Get your API key

The example requires a ModelVI API key to talk to the posting API.

**[Get your API key at https://modelvi.com](https://modelvi.com)**

## License

MIT. Use it, fork it, build on it.

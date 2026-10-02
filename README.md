# Ingestion Job Tracker — Live Coding Challenge

## Scenario

You're building the bookkeeping core of a background-processing system, like
the queue behind a document-ingestion pipeline. Jobs are submitted, workers
claim them, report progress with heartbeats, and sometimes die halfway
through. The tracker has to keep every job's state correct, including when a
worker that was given up on suddenly comes back.

## Format

This is a **live coding session** -- you'll clone this repo now and code with
your screen shared while we watch, for **45-60 minutes** total (a few opening
questions, ~30-40 minutes of coding, a short closing discussion). Think and
talk out loud as you go: how you reason through the problem matters as much
as the working code.

Ask us anything you'd normally ask a teammate before starting -- nothing here
is a trick, but not everything is spelled out on purpose. Don't be surprised
if a requirement changes or gets added partway through, the same way a real
ticket sometimes grows in scope -- that's a normal part of the exercise.

**No AI coding assistants (Copilot, ChatGPT, etc.)** -- talk through your
reasoning out loud instead. You may look up official documentation or
language syntax the way you would on the job.

## What's already here

- `job_tracker.py` -- the full spec is in this file's docstring, plus a
  `JobTracker` class stub for you to implement.
- `test_job_tracker.py` -- a handful of sanity-check tests. Passing all of
  them doesn't guarantee full correctness.
- `requirements.txt` -- just `pytest`.

## Setup

Requires Python 3.8+. If `python3` doesn't work on your system, try `python`
or `py` instead -- same commands otherwise.

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python3 -m pytest test_job_tracker.py -v
```

## Requirements

Implement `JobTracker` in `job_tracker.py` per the docstring: `submit`,
`claim`, `heartbeat`, `complete`, `reap_stale`, and `get`. Read the rules for
each method carefully -- the details (who may update a job, what a reap does,
ordering) are where the work is.

## Constraints

- Standard library only. No real queue, database, or threads are needed; this
  is in-memory bookkeeping with time passed in as an argument.
- You may restructure the file however you like.

## What we're evaluating

Not just "do the tests pass." Be ready to discuss:

- Which situations you thought of beyond the provided tests (workers dying,
  coming back late, jobs failing repeatedly).
- How cleanly your design adapts if a new requirement is added on top.
- How you'd explain the design to a non-technical stakeholder.
- How this would behave in a real system with Celery/Redis (or similar)
  workers instead of an in-memory object.

A simple, correct, well-reasoned solution beats a clever one you can't fully
explain.

## At the end

No need to commit or push anything. Walk us through what you built and why,
and what you'd do differently with more time.

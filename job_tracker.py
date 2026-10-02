"""
Ingestion Job Tracker
======================

You're building the bookkeeping core of a background-processing system (think
a document-ingestion pipeline: jobs are queued, workers pick them up, report
progress, and sometimes die halfway through). There is no real queue or
database here -- just an in-memory tracker. Time is passed in explicitly as an
integer `now` (seconds); never read the real clock.

A job moves through these states:

    queued  ->  running  ->  done
                   |
                   +-> back to queued (worker went silent), or failed

Implement `JobTracker`:

    submit(job_id, now) -> bool
        Adds a new job in state "queued". Returns True if created, False if a
        job with that id already exists (nothing changes in that case).

    claim(worker_id, now) -> Optional[str]
        Gives the oldest queued job (by original submit order) to this worker:
        state becomes "running", the worker is recorded as its owner, its
        attempt count goes up by 1, and "last heartbeat" is set to `now`.
        Returns the job_id, or None if nothing is queued.

    heartbeat(job_id, worker_id, progress, now) -> bool
        A running job's owner reports it is alive, with progress 0-100.
        Returns True if accepted. Returns False (and changes nothing) if the
        job is not running or is owned by a different worker.
        Reported progress must never move backwards.

    complete(job_id, worker_id, now) -> bool
        The owner finishes the job: state "done", progress 100. Returns False
        (and changes nothing) if the job is not running or is owned by a
        different worker.

    reap_stale(now, timeout) -> List[str]
        Finds running jobs whose last heartbeat is MORE than `timeout` seconds
        ago and takes them away from their worker. A reaped job loses its
        owner and its progress resets to 0. If it has already been attempted
        3 times it becomes "failed"; otherwise it goes back to "queued"
        (keeping its original place in line). Returns the reaped job ids in
        original submit order.

    get(job_id) -> Optional[dict]
        Returns {"state", "progress", "attempts", "worker_id"} for the job, or
        None if it doesn't exist.
"""

from typing import List, Optional


class JobTracker:
    def __init__(self):
        raise NotImplementedError

    def submit(self, job_id: str, now: int) -> bool:
        raise NotImplementedError

    def claim(self, worker_id: str, now: int) -> Optional[str]:
        raise NotImplementedError

    def heartbeat(self, job_id: str, worker_id: str, progress: int, now: int) -> bool:
        raise NotImplementedError

    def complete(self, job_id: str, worker_id: str, now: int) -> bool:
        raise NotImplementedError

    def reap_stale(self, now: int, timeout: int) -> List[str]:
        raise NotImplementedError

    def get(self, job_id: str) -> Optional[dict]:
        raise NotImplementedError

"""
A few sanity tests to run while you work. These are NOT exhaustive -- passing
them does not guarantee a correct solution; think about edge cases yourself,
especially around workers that die or come back late.

Run with:  python3 -m pytest test_job_tracker.py -v
"""

from job_tracker import JobTracker


def test_submit_and_claim_in_order():
    t = JobTracker()
    assert t.submit("j1", now=0) is True
    assert t.submit("j2", now=1) is True
    assert t.submit("j1", now=2) is False
    assert t.claim("w1", now=3) == "j1"
    assert t.claim("w2", now=3) == "j2"
    assert t.claim("w3", now=3) is None
    assert t.get("j1")["state"] == "running"
    assert t.get("j1")["worker_id"] == "w1"


def test_heartbeat_updates_progress_only_for_owner():
    t = JobTracker()
    t.submit("j1", 0)
    t.claim("w1", 1)
    assert t.heartbeat("j1", "w1", 40, now=2) is True
    assert t.get("j1")["progress"] == 40
    assert t.heartbeat("j1", "other", 90, now=3) is False
    assert t.get("j1")["progress"] == 40


def test_complete_by_owner():
    t = JobTracker()
    t.submit("j1", 0)
    t.claim("w1", 1)
    assert t.complete("j1", "w1", now=5) is True
    assert t.get("j1")["state"] == "done"
    assert t.get("j1")["progress"] == 100


def test_reap_requeues_silent_worker():
    t = JobTracker()
    t.submit("j1", 0)
    t.claim("w1", 1)
    t.heartbeat("j1", "w1", 50, now=2)
    assert t.reap_stale(now=100, timeout=30) == ["j1"]
    assert t.get("j1")["state"] == "queued"
    assert t.claim("w2", now=101) == "j1"


def test_unknown_job_returns_none():
    assert JobTracker().get("nope") is None

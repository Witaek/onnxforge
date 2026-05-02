from onnxforge_shared.schemas import JobStatus

def test_job_status_values():
    assert JobStatus.PENDING == "pending"
    assert JobStatus.RUNNING == "running"
    assert JobStatus.SUCCEEDED == "succeeded"
    assert JobStatus.FAILED == "failed"

def test_finished_statuses_are_distinct_from_active_statuses():
    finished = {JobStatus.SUCCEEDED, JobStatus.FAILED}
    active = {JobStatus.PENDING, JobStatus.RUNNING}

    assert finished.isdisjoint(active)
from onnxforge_shared.schemas import JobStatus, JobInfo

def test_job_status_values():
    assert JobStatus.PENDING == "pending"
    assert JobStatus.RUNNING == "running"
    assert JobStatus.SUCCEEDED == "succeeded"
    assert JobStatus.FAILED == "failed"

def test_finished_statuses_are_distinct_from_active_statuses():
    finished = {JobStatus.SUCCEEDED, JobStatus.FAILED}
    active = {JobStatus.PENDING, JobStatus.RUNNING}

    assert finished.isdisjoint(active)

def test_job_info_contains_id_and_status():
    job = JobInfo(job_id = "job-001", status = JobStatus.PENDING)

    assert job.job_id == "job-001"
    assert job.status == JobStatus.PENDING
from enum import StrEnum
from dataclasses import dataclass

class JobStatus(StrEnum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"

@dataclass(frozen=True)
class JobInfo:
    job_id: str
    status: JobStatus
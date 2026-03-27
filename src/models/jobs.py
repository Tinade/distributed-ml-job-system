# Tsigigenet Dessalgn
#  March 2026 


import time

class Job:
    def __init__(self, job_id, task, payload):
        self.job_id = job_id
        self.task = task
        self.payload = payload

        self.status = "pending"
        self.retries = 0
        self.max_retries = 3

        self.started_at = None
        self.completed_at = None
        self.last_heartbeat = None

    def start(self):
        if self.status != "pending":
            raise Exception("Job cannot be started unless it is pending")

        self.status = "running"
        self.started_at = time.time()
        self.last_heartbeat = time.time()

    def complete(self):
        if self.status != "running":
            raise Exception("Job must be running to complete")

        self.status = "success"
        self.completed_at = time.time()

    def fail(self):
        if self.status != "running":
            raise Exception("Job must be running to fail")

        self.retries += 1

        if self.retries >= self.max_retries:
            self.status = "failed"
        else:
            self.status = "pending"

    def heartbeat(self):
        if self.status != "running":
            raise Exception("Heartbeat only valid for running jobs")

        self.last_heartbeat = time.time()

    def is_stuck(self, timeout):
        if self.status != "running":
            return False

        if self.last_heartbeat is None:
            return False

        return (time.time() - self.last_heartbeat) > timeout
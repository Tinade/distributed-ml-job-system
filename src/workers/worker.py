from models.job import Job
import time
import random

def process_job(job):
    job.start()

    try:
        time.sleep(2)

        if random.random() < 0.5:
            raise Exception("Random failure")

        job.complete()
    except Exception:
        job.fail()
from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    try:
        with open(path, encoding="utf-8") as file:
            fields, *jobs = csv.reader(file, delimiter=",", quotechar='"')
            list_jobs = [dict(zip(fields, job)) for job in jobs]
            return list_jobs
    except FileNotFoundError:
        return []


def get_unique_job_types(path: str) -> List[str]:
    list_jobs = read(path)
    job_types = {job["job_type"] for job in list_jobs}
    return job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filteredByType = list(
        filter((lambda job: job["job_type"] == job_type), jobs)
    )
    return filteredByType

list = read('data/jobs.csv')
print([list[-3], list[-2], list[-1]])
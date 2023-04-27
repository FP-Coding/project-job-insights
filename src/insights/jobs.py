from functools import lru_cache
from typing import List, Dict
import csv


PATH = "./data/jobs.csv"


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=",", quotechar='"')
        fields, *jobs = reader
        list_jobs = [dict(zip(fields, job)) for job in jobs]
        return list_jobs


def get_unique_job_types(path: str) -> List[str]:
    list_jobs = read(path)
    job_types = {job["job_type"] for job in list_jobs}
    return job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError

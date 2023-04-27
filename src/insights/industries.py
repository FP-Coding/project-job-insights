from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    list_jobs = read(path)
    job_industries = {
        job["industry"]
        for job in list_jobs
        if job["industry"] != ''}
    return job_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filteredByType = list(
        filter((lambda job: job["industry"] == industry), jobs)
    )
    return filteredByType

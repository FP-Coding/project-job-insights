from typing import Union, List, Dict
from functools import reduce
from src.insights.jobs import read


PATH = "./data/jobs.csv"


def find_max_value(x: int, y: int) -> int:
    if x < y:
        return y
    else:
        return x


def find_min_value(x: int, y: int) -> int:
    if x > y:
        return y
    else:
        return x


def get_max_salary(path: str) -> int:
    list_jobs = read(path)
    list_salaries = [
        int(job["max_salary"])
        for job in list_jobs
        if job["max_salary"].isdigit()
    ]
    max_salary = reduce(find_max_value, list_salaries)
    return max_salary


def get_min_salary(path: str) -> int:
    list_jobs = read(path)
    list_salaries = [
        int(job["min_salary"])
        for job in list_jobs
        if job["min_salary"].isdigit()
    ]
    min_salary = reduce(find_min_value, list_salaries)
    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min = int(job["min_salary"])
        max = int(job["max_salary"])
        if (min > max):
            raise ValueError
        return min <= int(salary) <= max
    except (KeyError, TypeError):
        raise ValueError


def filter_condition(job, salary):
    try:
        return matches_salary_range(job, salary)
    except (ValueError):
        return False


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    return list(filter((lambda job: filter_condition(job, salary)), jobs))

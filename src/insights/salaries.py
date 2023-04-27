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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError


print(get_max_salary(PATH))
print(get_min_salary(PATH))

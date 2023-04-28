from src.pre_built.sorting import sort_by
from pytest import fixture


@fixture
def job_01():
    return {
        "job_title": "Data Engineer, Mid with Security Clearance",
        "company": "Booz Allen Hamilton",
        "state": "VA",
        "city": "Herndon",
        "min_salary": "58824",
        "max_salary": "112227",
        "job_desc": "desc",
        "industry": "Business Services",
        "rating": "3.7",
        "date_posted": "2020-05-07",
        "valid_until": "2020-06-06",
        "job_type": "FULL_TIME",
        "id": "1",
    }


@fixture
def job_02():
    return {
        "job_title": "Data Modeler, Senior with Security Clearance",
        "company": "Booz Allen Hamilton",
        "state": "VA",
        "city": "Springfield",
        "min_salary": "90454",
        "max_salary": "151998",
        "job_desc": "desc",
        "industry": "Business Services",
        "rating": "3.7",
        "date_posted": "2020-04-28",
        "valid_until": "2020-06-06",
        "job_type": "FULL_TIME",
        "id": "2",
    }


@fixture
def job_03():
    return {
        "job_title": "Data Engineer, Senior with Security Clearance",
        "company": "Booz Allen Hamilton",
        "state": "VA",
        "city": "Herndon",
        "min_salary": "91443",
        "max_salary": "155868",
        "job_desc": "desc",
        "industry": "Business Services",
        "rating": "3.7",
        "date_posted": "2020-05-02",
        "valid_until": "2020-06-06",
        "job_type": "FULL_TIME",
        "id": "3",
    }


def test_sort_by_criteria(job_01, job_02, job_03):
    list_to_sort = [job_01, job_02, job_03]
    sort_by(list_to_sort, "date_posted")
    assert list_to_sort[2]["id"] == job_02["id"]

    sort_by(list_to_sort, "max_salary")
    assert list_to_sort[0]["id"] == job_03["id"]

    sort_by(list_to_sort, "min_salary")
    assert list_to_sort[0]["id"] == job_01["id"]

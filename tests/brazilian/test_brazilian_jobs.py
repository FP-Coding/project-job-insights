from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    report = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    assert "title" in report[0]
    assert "salary" in report[0]
    assert "type" in report[0]
    assert "tipo" not in report[0]
    assert "salario" not in report[0]
    assert "titulo" not in report[0]

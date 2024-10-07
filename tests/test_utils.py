from src.utils import (
    get_top_vacancies,
    get_vacancies_by_salary_from,
    sort_vacancies_by_salary,
)


def test_get_vacancies_by_salary_from(sample_vacancies):
    """Тестирование функции get_vacancies_by_salary_from."""
    result = get_vacancies_by_salary_from(sample_vacancies, 100000)
    assert len(result) == 3
    assert all(vac.salary >= 100000 for vac in result)


def test_sort_vacancies_by_salary(sample_vacancies):
    """Тестирование функции sort_vacancies_by_salary."""
    result = sort_vacancies_by_salary(sample_vacancies)
    assert result[0].salary == 150000  # JavaScript Developer
    assert result[1].salary == 120000  # Python Developer
    assert result[2].salary == 100000  # Java Developer
    assert result[3].salary == 90000  # C# Developer


def test_get_top_vacancies(sample_vacancies):
    """Тестирование функции get_top_vacancies."""
    result = get_top_vacancies(sample_vacancies, 2)
    assert len(result) == 2
    assert result[0].salary == 150000  # JavaScript Developer
    assert result[1].salary == 120000  # Python Developer

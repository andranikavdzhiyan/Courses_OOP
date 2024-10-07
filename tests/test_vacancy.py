import pytest

from src.vacancy import Vacancy


def test_vacancy_init(first_action):
    assert first_action.name == "Team Lead"
    assert first_action.url == "https://hh.ru/vacancy/107726345"
    assert first_action.requirement == "Опыт работы над проектами, предпочтительно Java"
    assert first_action.responsibility == "Планирование, координация и контроль работ"
    assert first_action.salary == 500000


def test_vacancy_to_dict(second_action):
    assert second_action.to_dict() == {
        "name": "Back-End Developer",
        "url": "https://hh.ru/vacancy/107503256",
        "requirement": "педагогическое образование;  пунктуальность",
        "responsibility": "Развитиекурса, поддержание его актуальности",
        "salary": 300000,
    }
    assert len(second_action.to_dict()) == 5


def test_verify_data(first_action):
    # Тест с объектом Vacancy
    result = Vacancy._Vacancy__verify_data(first_action)
    assert (
        result == first_action.salary
    ), "Ошибка: должно возвращаться значение salary объекта Vacancy."

    # Тест с float
    result = Vacancy._Vacancy__verify_data(30000.0)
    assert result == 30000.0, "Ошибка: должно возвращаться значение float."

    # Тест с некорректным типом данных
    with pytest.raises(TypeError):
        Vacancy._Vacancy__verify_data("incorrect type")

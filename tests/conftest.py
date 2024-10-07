from unittest.mock import Mock, patch

import pytest

from src.vacancy import Vacancy
from src.vacancy_saver import JSONSaver


@pytest.fixture
def first_action():
    return Vacancy(
        name="Team Lead",
        url="https://hh.ru/vacancy/107726345",
        requirement="Опыт работы над проектами, предпочтительно Java",
        responsibility="Планирование, координация и контроль работ",
        salary=500000,
    )


@pytest.fixture
def second_action():
    return Vacancy(
        name="Back-End Developer",
        url="https://hh.ru/vacancy/107503256",
        requirement="педагогическое образование;  пунктуальность",
        responsibility="Развитиекурса, поддержание его актуальности",
        salary=300000,
    )


@pytest.fixture
def mock_response():
    return {
        "items": [
            {
                "name": "Python Developer",
                "alternate_url": "https://hh.ru/vacancy/123456",
                "snippet": {
                    "requirement": "Good knowledge of Python",
                    "responsibility": "Develop software",
                },
                "salary": {"from": 100000, "to": 150000},
            },
            {
                "name": "Java Developer",
                "alternate_url": "https://hh.ru/vacancy/654321",
                "snippet": {
                    "requirement": "Good knowledge of Java",
                    "responsibility": "Develop enterprise applications",
                },
                "salary": None,
            },
        ]
    }


# Фикстура для мокирования requests.get
@pytest.fixture
def mock_requests_get(mock_response):
    with patch("requests.get") as mock_get:
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = mock_response
        yield mock_get


@pytest.fixture
def json_saver(tmp_path):
    # Создаем временный файл для тестов в каталоге tmp_path
    test_file = tmp_path / "vacancies.json"
    saver = JSONSaver(filename=str(test_file))  # Используем временный файл
    yield saver


@pytest.fixture
def sample_vacancy():
    return Vacancy(
        name="Python Developer",
        url="https://example.com/python-developer",
        requirement="Знание Python",
        responsibility="Разработка на Python",
        salary=100000,
    )


@pytest.fixture
def sample_vacancies():
    """Создает список тестовых вакансий."""
    return [
        Vacancy(
            name="Python Developer",
            url="https://example.com/python",
            requirement="Опыт Python разработки",
            responsibility="Разработка приложений на Python",
            salary=120000,
        ),
        Vacancy(
            name="Java Developer",
            url="https://example.com/java",
            requirement="Опыт Java разработки",
            responsibility="Разработка приложений на Java",
            salary=100000,
        ),
        Vacancy(
            name="JavaScript Developer",
            url="https://example.com/javascript",
            requirement="Опыт JavaScript разработки",
            responsibility="Разработка приложений на JavaScript",
            salary=150000,
        ),
        Vacancy(
            name="C# Developer",
            url="https://example.com/csharp",
            requirement="Опыт C# разработки",
            responsibility="Разработка приложений на C#",
            salary=90000,
        ),
    ]

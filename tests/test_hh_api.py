from src.hh_api import HeadHunterAPI


def test_load_vacancies_no_response(mock_requests_get):
    """Функция которая осуществляет тест для обработки ошибки API"""

    mock_requests_get.return_value.status_code = 500

    hh_api = HeadHunterAPI()

    vacancies = hh_api.load_vacancies("developer")

    assert vacancies == []

def test_add_vacancy(json_saver, sample_vacancy):
    json_saver.add_vacancy(sample_vacancy)
    vacancies = json_saver._JSONSaver__read_file()
    assert len(vacancies) == 1
    assert vacancies[0]["url"] == sample_vacancy.url, "URL вакансии должен совпадать."


def test_add_duplicate_vacancy(json_saver, sample_vacancy):
    json_saver.add_vacancy(sample_vacancy)
    json_saver.add_vacancy(sample_vacancy)  # Добавляем дубликат
    vacancies = json_saver._JSONSaver__read_file()
    assert len(vacancies) == 1, "Дубликаты не должны добавляться."


def test_del_vacancy(json_saver, sample_vacancy):
    json_saver.add_vacancy(sample_vacancy)
    json_saver.del_vacancy(sample_vacancy.url)
    vacancies = json_saver._JSONSaver__read_file()
    assert len(vacancies) == 0, "Список вакансий должен быть пустым после удаления."


def test_get_vacancy_by_name(json_saver, sample_vacancy):
    json_saver.add_vacancy(sample_vacancy)
    found_vacancies = json_saver.get_vacancy_by_vacancy_name("python")
    assert len(found_vacancies) == 1, "Должна быть найдена одна вакансия."
    assert (
        found_vacancies[0].url == sample_vacancy.url
    ), "URL найденной вакансии должен совпадать."


def test_get_vacancy_by_nonexistent_name(json_saver):
    found_vacancies = json_saver.get_vacancy_by_vacancy_name("nonexistent")
    assert (
        len(found_vacancies) == 0
    ), "Не должно быть найдено вакансий по несуществующему названию."

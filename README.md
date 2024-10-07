# Программа для поиска вакансий с платформы hh.ru

## Описание проекта

Этот проект представляет собой поисковик вакансий с платформы hh.ru. В рамках проекта реализованы функции для запроса данных посредством API.

## Установка

1. Склонируйте репозиторий: https://github.com/andranikavdzhiyan/Courses_OOP
   


 ##  Структура проекта

Вот обзор структуры проекта:

```plaintext
Course_work/
│
├── .flake8                 # Конфигурация для проверки стиля кода
├── .gitignore              # Правила игнорирования файлов Git
├── READMY.md               # Документация проекта (этот файл)
├── poetry.lock             # Файл блокировки зависимостей Poetry
├── pyproject.toml          # Конфигурационный файл проекта для Poetry
├── main.py                 # Точка входа в приложение
│
├── data/                   # Данные проекта
│   └── vacancies.json      # JSON-файл с данными 
│    
│
├── src/                    # Исходный код приложения
│   ├── __init__.py         # Помечает src как пакет
│   ├── hh_api.py           # Функция работы с API
│   ├── utils.py            # Вспомогательные функции
│   ├── vacancy.py          # Функция работы класса представления вакансий
│   └── vacancy_saver.py    # Функция работы с JSON 
│   
│   
│
└── tests/                     
    ├── __init__.py            
    ├── conftest.py            
    ├── test_hh_api.py         
    ├── test_utils.py          
    ├── test_vacancy.py        
    └── test_vacancy_saver.py  
    
```
## Покрытие тестами

```
============================ test session starts ============================
platform win32 -- Python 3.12.4, pytest-8.3.3, pluggy-1.5.0
rootdir: C:\Users\Andrey\PycharmProjects\my_prj\courses_oop
configfile: pyproject.toml
plugins: cov-5.0.0
collected 12 items                                                                                                                                                                         

tests\test_hh_api.py .                                                                                                                                                               [  8%]
tests\test_utils.py ...                                                                                                                                                              [ 33%]
tests\test_vacancy.py ...                                                                                                                                                            [ 58%]
tests\test_vacancy_saver.py .....                                                                                                                                                    [100%]

---------- coverage: platform win32, python 3.12.4-final-0 -----------
Name                          Stmts   Miss  Cover
-------------------------------------------------
src\__init__.py                   0      0   100%
src\hh_api.py                    42     18    57%
src\utils.py                      8      0   100%
src\vacancy.py                   34      8    76%
src\vacancy_saver.py             49      6    88%
tests\__init__.py                 0      0   100%
tests\conftest.py                30      0   100%
tests\test_hh_api.py              6      0   100%
tests\test_utils.py              16      0   100%
tests\test_vacancy.py            18      0   100%
tests\test_vacancy_saver.py      23      0   100%
-------------------------------------------------
TOTAL                           226     32    86%


============================ 12 passed in 4.81s ============================
```

 
###  Запуск тестов

#### Для запуска тестов и проверки работоспособности:
Копировать код ```pytest tests/```

#### Этот проект лицензирован по лицензии MIT. ☺
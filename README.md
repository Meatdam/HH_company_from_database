# Проект по БД
_____
В рамках проекта получаем данные о компаниях и вакансиях с сайта hh.ru, проектируем таблицы в БД PostgreSQL и загружаем полученные данные в созданные таблицы.

## Основные шаги проекта
______
1. Получаем данные о работодателях и их вакансиях с сайта hh.ru. Для этого используется публичный API hh.ru и библиотека 
'requests'
2. Выбирается 10 или менее интересных вам компаний, от которых вы будете получать данные о вакансиях по API.
3. Проектируются таблицы в БД PostgreSQL для хранения полученных данных о работодателях и их вакансиях. Для работы с БД используется библиотека 
'psycopg2'
4. Реализцется код, который заполняет созданные в БД PostgreSQL таблицы данными о работодателях и их вакансиях.
______
## Структура проека
В данном проекте имеются две папки: src, utils.
_______
### src:
В данной папке имеются три файла: DBModule.py, DBManager.py, hh_company_vacancy_parser.py.
- DBManager.py: в данном файле имеется класс 'DBManager', который отвечает за запросы к уже созданной базе данных.
1. метод 'get_companies_and_vacancies_count': Получает список всех компаний и количество вакансий у каждой компании,
2. метод 'get_all_vacancies': Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию,
3. метод 'get_avg_salary': Получает среднюю зарплату по вакансиям,
4. метод 'get_vacancies_with_higher_salary': Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям,
5. метод 'get_vacancies_with_keyword': Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python.
 
- DBModule.py: в данном файле имеется класс DBModule который отвечает за создание таблиц двух таблиц (employer, vacancies) в базе данных и заполнением этих таблиц данными с hh.ru.
1. метод 'create_tables': Метод создает две таблицы в базе данных 'hh_vacancies', Одна таблица называется 'employer', вторая 'vacancies' в
'employer' создаются две колонки: employer_id, employer_name. В 'vacancies' создаются шесть колонок: vacancy_id, company_id, vacancy_name, salary_from, salary_to и url,
2. метод 'full_tables': Метод заполнения таблиц в базе данных 'hh_vacancies', компаниями и вокансиями компаний из сайта 'Head Hunter'

- hh_company_vacancy_parser.py: в данном файле имеется класс 'HHVacancionParsing', который отвечает за парсинг сайта hh.ru по кампаниям и вакансиям.
1. метод 'get_request_employeers': Метод возвращающий json по умолчанию 10 компаний,
2. метод 'get_employers_sort':  Метод сортировки 10 компаний, возвращется список с id компании, название вакансии,
3. метод 'get_vacancies_from_company':  Метод возвращающий json вакансий,
4. метод 'get_all_vacancyes':  Метод забирает список с метода get_employers_sort, и список get_vacancies_from_company и сортирует все вакансии по определенному id компании и складывает все в список,
5. метод 'filter_vacancyes': Метод фильтрации вакансий по нужному нам формату, id, name, salary_from, salary_to, url, emloyeer.
_______
### utils:
В данной папке содержится файл 'user_interaction.py', в котором находятся две функции:
1. 'user_interaction': Взаимодействия с пользователем, получает данные от пользователя, записывает в базу даннных и сортирует,
2. delete_tables: Удаление таблиц из быза данных.</br></br>
________

Так же в корне проекта лежит файл 'main.py', в котором запускается весь проект. </br>
### И важный файл: 
Конфигурационный файл 'config.py' в котором находится переменная 'conn': служит для коннекта с БД. Чтобы проект запустился корректно на вашей системе, необходимо заполнить данную переменную своими данными.
_______
## Запуск проекта
Чтобы проект корректно заработал на вашем ПК необходимо: 
1. Клонировать проект себе в репозиторий и локально на ПК
```
git@github.com:Meatdam/HH_company_from_database.git
```
2. Установить виртуальное окружение `venv`
```
python3 -m venv venv для MacOS и Linux систем
python -m venv venv для windows
```
3. Активировать виртуальное окружение
```
source venv/bin/activate для MasOs и Linux систем
venv\Scripts\activate.bat для windows
```
4. установить файл с зависимостями
```
pip install -r requirements.txt
```
6. Заполнить корректно в файле 'database.ini', данными с вашей БД в переменную </br>
```
host=<localhost> как правило 
user=<ваше имя зарегестрированного в postgreSQL>
password=<Ваш пороль от БД>
port=<5432> как правило
```
# Особое внимание:
Создавать базу данных, или прописывать ее в программе не нужно, программа сама создаст ее, при запуске.  

Автор проекта:<br>
[Кузькин Илья](https://github.com/Meatdam)

from src.hh_company_vacancy_parser import HHVacancionParsing
from src.DB_module import DBModule
import psycopg2


def user_interaction(value) -> None:
    """
    Взаимодействия с пользователем, получает данные от пользователя, записывает в базу даннных
    и сортирует.
    :return: None
    """
    HHVacancionParsing(value)
    module = DBModule()
    module.create_tables()
    module.full_tables(value)


def delete_tables() -> None:
    """
    Удаление таблиц из быза данных
    :return: None
    """
    conn = psycopg2.connect(host='localhost', database='hh_vacancies', user='postgres', password='1234')
    conn.commit()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute('DROP TABLE vacancies; DROP TABLE employer')
            conn.commit()


if __name__ == '__main__':
    user_input = input('').split()
    user_interaction(user_input)

import psycopg2

connection = connect = psycopg2.connect(host='localhost', database='hh_vacancies', user='postgres', password='1234')
connection.commit()

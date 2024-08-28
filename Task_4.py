'''4. Поиск данных в базе

Напишите метод в классе DatabaseManager,
 который будет принимать имя пользователя и возвращать его данные
  из таблицы users. Используйте SQL-запросы для поиска данных.'''

import sqlite3


class DatabaseManager:
    def __init__(self):
        self.connection = sqlite3.connect('Database.db')
        self.cursor = self.connection.cursor()

    def get_user_data(self, full_name):
        query = "SELECT * FROM Users WHERE full_name = ?"
        self.cursor.execute(query, (full_name,))
        user_data = self.cursor.fetchone()

        if user_data:
            print(f'{user_data}')
        else:
            print(f"User {full_name} not found.")

    def close_connection(self):
        self.connection.close()

a = DatabaseManager()
a.get_user_data('Gaparov Beksultan')
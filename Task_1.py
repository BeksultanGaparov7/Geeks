'''1. Создание класса для работы с базой данных

Напишите класс DatabaseManager,
 который будет использовать SQLite3 для подключения к базе данных.
  Реализуйте методы для открытия и закрытия соединения.'''

import sqlite3


class DatabaseManager:
    def __init__(self):
        pass

    def connect(self):
        self.connect = sqlite3.connect('Database.db')


    def disconnect(self):
        self.connect.commit()
        self.connect.close()



a = DatabaseManager()
a.connect()
a.disconnect()



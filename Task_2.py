"""2. Класс для управления таблицей

Создайте класс User, который будет управлять таблицей users в SQLite3.
 Реализуйте методы для добавления нового пользователя, получения пользователя
 по ID и удаления пользователя."""
import sqlite3

connect = sqlite3.connect('Database.db')
cursor = connect.cursor()

class User:
    def __init__(self):
        cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR(40),
        age INTEGER,
        grade INTEGER
        )''')

    def add_user(self, full_name, age, grade):
        cursor.execute('''INSERT INTO Users(full_name, age, grade)
            VALUES(?,?,?)''',(full_name, age, grade))
        print(f'User: {full_name} INSERTED')

    def get_user_info(self, id):
        cursor.execute('SELECT * FROM Users WHERE id = ?',(id))
        user = cursor.fetchall()
        print(user)

    def delete_user(self, id):
        cursor.execute('DELETE FROM Users WHERE id = ?',(id))
        print(f'User by id: {id} deleted.')

a = User()
a.add_user('Gaparov Beksultan', 12, 7)
a.get_user_info('1')



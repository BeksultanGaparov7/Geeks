'''3. Наследование и работа с несколькими таблицами

Реализуйте классы Admin и Customer,
 которые будут наследовать от класса User.
 Добавьте дополнительные поля для каждой роли и методы для работы
  с соответствующими таблицами admins и customers.'''

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

class Admin(User):
    def __init__(self):
        User.__init__(self)
        cursor.execute('''CREATE TABLE IF NOT EXISTS admins(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name VARCHAR(40),
                age INTEGER,
                email VARCHAR(25)
                )''')
    def add_user(self, full_name, age, email):
        cursor.execute('''INSERT INTO admins(full_name, age, email)
                    VALUES(?,?,?)''', (full_name, age, email))
        print('Inserted')

    def get_user_info(self, id):
        cursor.execute('SELECT * FROM admins WHERE id = ?',(id))
        user = cursor.fetchall()
        print(user)

    def delete_user(self, id):
        cursor.execute('DELETE FROM admins WHERE id = ?',(id))
        print(f'User by id: {id} deleted.')

class Customer(User):
    def __init__(self):
        User.__init__(self)
        cursor.execute('''CREATE TABLE IF NOT EXISTS customers(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        full_name VARCHAR(40),
                        age INTEGER,
                        email VARCHAR(25),
                        info TEXT
                        )''')
    def add_customer(self, full_name, age, email, info):
        cursor.execute('''INSERT INTO customers(full_name, age, email, info)
                    VALUES(?,?,?,?)''', (full_name, age, email, info))
        print('Inserted')

    def get_user_info(self, id):
        cursor.execute('SELECT * FROM customers WHERE id = ?',(id))
        user = cursor.fetchall()
        print(user)

    def delete_user(self, id):
        cursor.execute('DELETE FROM customers WHERE id = ?',(id))
        print(f'User by id: {id} deleted.')

a = Admin()
a.add_user('BG', 12, 'Gaparovbeksulatn7@gmail.com')
a.get_user_info('1')
a.delete_user('1')

b = Customer()
b.add_customer('BG', 12, 'Gaparovbeksulatn7@gmail.com','guoew')
b.get_user_info('1')
b.delete_user('1')





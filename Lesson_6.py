import sqlite3#Импортируем СУБД

connect = sqlite3.connect('Geeks.db')#Горорим что connect это переменная содержит функцию connect и передаем название файла Базы Данных
cursor = connect.cursor()#Создаем переменную cursor она содержит функцию для работы с базой данных

#execute - запрос к базе данных, она содержит sql запрос
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Geeks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(20) NOT NULL,
        surname VARCHAR(20) NOT NULL,
        age INT DEFAULT NULL,
        info TEXT,
        is_have BOOLEAN NOT NULL DEFAULT FALSE,
        birth_date DATE,
        rating DOUBLE(4, 2) DEFAULT 0.0
    )
""")


def register():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    age = int(input('Введите возраст: '))
    info = input('Расскажите о себе: ')
    is_have = bool(input('Наличие ноутбука: '))
    birth_date = input('Введите дату рождения: ')
    rating = float(input('Введите свой рейтинг: '))

    #Не безопасный метод
    #cursor.execute(f"""INSERT INTO Geeks
    #(name, surname, age, direction, is_have, rating, birth_date)
    #VALUES ('{name}', '{surname}' {age}, '{info}', {is_have}, '{birth_date}', {rating})""")

    cursor.execute("""INSERT INTO Geeks (name, surname, age, info, is_have, rating, birth_date)
        VALUES (?,?,?,?,?,?,?)
    """,(name, surname, age, info, is_have, rating, birth_date))

    connect.commit()
    #connect.commit() Использование форматированных строк (f"") для вставки значений в SQL-запрос может привести к уязвимости типа SQL-инъекция, если пользователь вводит специальные символы в текстовые поля.

register()
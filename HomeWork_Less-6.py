import sqlite3
from datetime import date


connect = sqlite3.connect('School.db')
cursor = connect.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR (40) NOT NULL,
        age INT NOT NULL,
        grade TEXT NOT NULL,
        enrollment_date DATE
    )
''')


cursor.execute('''CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_name VARCHAR (40) NOT NULL,
        teacher_name VARCHAR (40) NOT NULL
    )
''')


def register_student():
    today = date.today()
    full_name = input('Enter students fullname: ')
    age = int(input('Enter students age(only numbers): '))
    grade = input('Enter students grade: ')
    enrollment_date = input("Enter today's date, or enter today: ").lower()

    if enrollment_date == 'today':
        enrollment_date = today
    else:
        enrollment_date = enrollment_date

    cursor.execute("""INSERT INTO students (full_name, age, grade, enrollment_date)
        VALUES (?, ?, ?, ?)
    """,(full_name, age, grade, enrollment_date))

    connect.commit()


def add_subject():
    subject_name = input("Enter subject name: ")
    teacher_name = input("Enter teacher name: ")

    cursor.execute('''INSERT INTO subjects (subject_name, teacher_name) 
    VALUES (?,?)''', (subject_name, teacher_name))

    connect.commit()

def get_students():
    cursor.execute(''' SELECT * FROM students''')
    students = cursor.fetchall()
    for student in students:
        print(student)

def get_subjects():
    cursor.execute(''' SELECT * FROM subjects ''')
    subjects = cursor.fetchall()
    for subject in subjects:
        print(subject)

def get_students_by_grade():
    grade = input('Enter students grade: ')#
    cursor.execute(''' SELECT * FROM students WHERE grade = ?''', (grade))
    students_by_grade = cursor.fetchall()
    for row in students_by_grade:
        print(row)

def update_student_age():
    student_id = input("Enter student's id: ")
    new_age = input("Enter student's new age: ")
    cursor.execute('''SELECT * FROM students WHERE id = ? ''',(student_id))
    old_data = cursor.fetchall()
    print(f'Old data: {old_data}')
    cursor.execute('''UPDATE students SET age = ? WHERE id = ?''', (new_age, student_id))
    connect.commit()
    cursor.execute('''SELECT * FROM students WHERE id = ? ''', (student_id))
    new_data = cursor.fetchall()
    print(f'New data: {new_data}')

def delete_student():
    student_id = input("Enter the student's id, that you want to delete: ")
    cursor.execute('''DELETE FROM students WHERE id = ?''', (student_id))
    print(f'Deleted student by id:{student_id}')
    connect.commit()

def get_student_count_by_grade():
    grade = input('Enter students grade: ')
    cursor.execute('''SELECT * FROM students WHERE grade = ?''',(grade))
    count = 0
    students = cursor.fetchall()
    for i in students:
        count += 1
    print(f'Grade {grade} contains {count} students')

def get_teacher_subjects():
    teacher_name = input('Enter teacher name: ')
    cursor.execute('''SELECT * FROM subjects WHERE teacher_name = ?''',(teacher_name))
    teacher_sub = cursor.fetchall()
    print(teacher_sub)


coments = 'Некие коментарии от автора: Уф! очень долго было! Не то что бы я что-то не понял \n ' \
          'Но создавать 9 функций было долго! ХАХ! Я не прибегал к помощи менторов делал все сам! \n'





register_student()
add_subject()
get_students()
get_subjects()
get_students_by_grade()
update_student_age()
delete_student()
get_student_count_by_grade()
get_teacher_subjects()


print(coments)
connect.close()
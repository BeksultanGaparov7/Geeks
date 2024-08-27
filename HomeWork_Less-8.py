import math

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        print(self.balance)

a = BankAccount()
a.deposit(100)
a.withdraw(10)
a.get_balance()
b = BankAccount()
b.deposit(1000)
b.withdraw(700)
b.get_balance()
c = BankAccount()
c.deposit(10)
c.withdraw(2)
c.get_balance()

class Course:
    def __init__(self, title, credits):
        self.title = title
        self.credits = credits

class Student:
    def __init__(self, full_name):
        self.full_name = full_name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def total_credits(self):
        total = sum(course.credits for course in self.courses)
        return total

    def show_info(self):
        print(f'Student: {self.full_name}')
        print(f'Courses: {[course.title for course in self.courses]}')
        print(f'All credits: {self.total_credits()}')

math_course = Course('Math', 12)
history = Course('History', 7)
science = Course('Science', 9)

student1 = Student('Beksultan Gaparov')
student2 = Student('Alikhan Karimov')

student1.add_course(science)
student1.add_course(history)

student2.add_course(math_course)
student2.add_course(history)

student1.show_info()
student2.show_info()

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def info(self):
        return f'{self.title} by {self.author} publicated in {self.publication_year}'

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f'\nBook found: {book.info()}')
                return
        print(f"'{title}' book NOT FOUND")

    def list_books(self):
        if not self.books:
            print('Library is empty')
        else:
            for book in self.books:
                print(f'List of books in library: \n{book.info()}')

book1 = Book("Война и мир", "Лев Толстой", 1869)
book2 = Book("Преступление и наказание", "Федор Достоевский", 1866)
book3 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967)

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.list_books()

library.find_book('Война и мир')

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

circle1 = Circle(5)
circle2 = Circle(3)

rectangle1 = Rectangle(4, 6)
rectangle2 = Rectangle(2, 3)

print(f"Круг 1: площадь = {circle1.area():.2f}, периметр = {circle1.perimeter():.2f}")
print(f"Круг 2: площадь = {circle2.area():.2f}, периметр = {circle2.perimeter():.2f}")

print(f"Прямоугольник 1: площадь = {rectangle1.area():.2f}, периметр = {rectangle1.perimeter():.2f}")
print(f"Прямоугольник 2: площадь = {rectangle2.area():.2f}, периметр = {rectangle2.perimeter():.2f}")

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def show_info(self):
        return f"{self.year} {self.make} {self.model}"

class Garage:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, make, model):
        for car in self.cars:
            if car.make.lower() == make.lower() and car.model.lower() == model.lower():
                self.cars.remove(car)
                print(f"Автомобиль {car.show_info()} был удален из гаража.")
                return
        print(f"Автомобиль {make} {model} не найден в гараже.")

    def list_cars(self):
        if not self.cars:
            print("Гараж пуст.")
        else:
            print("Список автомобилей в гараже:")
            for car in self.cars:
                print(car.show_info())

car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2018)
car3 = Car("Ford", "Focus", 2015)

garage = Garage()

garage.add_car(car1)
garage.add_car(car2)
garage.add_car(car3)

garage.list_cars()

garage.remove_car("Honda", "Civic")

garage.list_cars()

from database import DataBase

class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def __str__(self):
        return f'{self.name}, дата рождения: {self.birth_year}'

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, Publication date: {self.publication_year}'

class Library:
    def __init__(self, db : DataBase):
        self.db = db

    def add_author(self, author):
        if not self.db.get_author(author.name):
            self.db.add_author(author.name, author.birth_year)

    def add_book(self, book):
        author = self.db.get_author(book.name)
        if author in None:
            self.add_author(book.author)
            author = self.db.get_author(book.author.name)

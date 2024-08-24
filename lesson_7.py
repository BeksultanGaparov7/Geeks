from database import Database


class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def __str__(self):
        return f"{self.name} (born {self.birth_year})"


class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.publication_year})"


class Library:
    def __init__(self, db: Database):
        self.db = db

    def add_author(self, author):
        if not self.db.get_author(author.name):
            self.db.add_author(author.name, author.birth_year)

    def add_book(self, book):
        author = self.db.get_author(book.author.name)
        if author is None:
            self.add_author(book.author)
            author = self.db.get_author(book.author.name)

        self.db.add_book(book.title, author[0], book.publication_year)

    def remove_book(self, title):
        self.db.remove_book(title)

    def find_books_by_author(self, author_name):
        rows = self.db.find_books_by_author(author_name)
        return [Book(title=row[0], author=Author(name=row[1], birth_year=None), publication_year=row[2]) for row in
                rows]

    def list_books(self):
        rows = self.db.list_books()
        return [Book(title=row[0], author=Author(name=row[1], birth_year=None), publication_year=row[2]) for row in
                rows]


# if __name__ == "__main__":
db = Database()
library = Library(db)
author1 = Author('Фёдор Достоевский', 1821)
author2 = Author('Антон Чехов', 1860)

book1 = Book('Толстый и худой', author2, 1883)
book2 = Book('Преступление и наказание', author1, 1866)
book3 = Book('Белые ночи', author1, 1848)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

#print("Все книги: ")
#for book in library.list_books():
    #print(book)

print('Serch: ')
import sqlite3

class Database:
    def __init__(self, db_name='library.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS authors (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    birth_year INTEGER
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    author_id INTEGER,
                    publication_year INTEGER,
                    FOREIGN KEY (author_id) REFERENCES authors (id)
                )
            ''')

    def add_author(self, name, birth_year):
        with self.conn:
            self.conn.execute(
                'INSERT INTO authors (name, birth_year) VALUES (?, ?)',
                (name, birth_year)
            )

    def get_author(self, name):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, name, birth_year FROM authors WHERE name = ?', (name,))
        return cursor.fetchone()

    def add_book(self, title, author_id, publication_year):
        with self.conn:
            self.conn.execute(
                'INSERT INTO books (title, author_id, publication_year) VALUES (?, ?, ?)',
                (title, author_id, publication_year)
            )

    def remove_book(self, title):
        with self.conn:
            self.conn.execute('DELETE FROM books WHERE title = ?', (title,))

    def find_books_by_author(self, author_name):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT books.title, authors.name, books.publication_year
            FROM books
            JOIN authors ON books.author_id = authors.id
            WHERE authors.name = ?
        ''', (author_name,))
        return cursor.fetchall()

    def list_books(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT books.title, authors.name, books.publication_year
            FROM books
            JOIN authors ON books.author_id = authors.id
        ''')
        return cursor.fetchall()

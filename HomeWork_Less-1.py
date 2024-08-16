class Fruit:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def info(self):
        print(f'Название фрукта - {self.name}, этот фрукт {self.color} цвета и он весит {self.weight} kg.')

ananas = Fruit('Ananas', 'orange', '1.05')
ananas.info()

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def check_pages(self):
        if self.pages < 100:
            print('Книга тонкая')
        elif self.pages > 100 and self.pages < 300:
            print('Книга средняя')
        else:
            print('Книга толстая')

harry_potter = Book('Philosofes Stone', 'J.K.Rowling', 750)
harry_potter.check_pages()

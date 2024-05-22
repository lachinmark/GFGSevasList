import random


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


class Bookstore(Book):

    def addbook(self):
        listTitles.append(self.title)
        listAuthors.append(self.author)

    def displaybooks(self):
        print(listTitles)

    def search(self, title):
        print(listTitles.index(title))


if __name__ == '__main__':
    listTitles = []
    listAuthors = []
    book = Bookstore(title='Dune', author='Herbert', price=18)

    book.addbook()
    book.displaybooks()

    # book.search('Dune')
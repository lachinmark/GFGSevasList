class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def issue(self, member_id):
        self.issued_to = member_id

    def return_book(self):
        self.issued_to = None

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_book = []

    def borrow_book(self, isbn):
        self.borrowed_book.append(isbn)

    def return_book(self, isbn):
        self.borrowed_book.remove(isbn)

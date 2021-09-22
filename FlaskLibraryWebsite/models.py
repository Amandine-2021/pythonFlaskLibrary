# filename: models.py
# Final project CSC217-Python FlaskLibrary
# Amandine Velamala

from . import db
from .validationHelper import validateISBN, validateLength

class Book(db.Model):
    isbn = db.Column(db.String(18), primary_key=True)
    title = db.Column(db.String(200))
    author_first_name = db.Column(db.String(30))
    author_last_name = db.Column(db.String(30))
    genre = db.Column(db.String(30))
    publisher = db.Column(db.String(80))
    description = db.Column(db.String(1000))
    checkedOutDate = db.Column(db.Date, nullable=True)
    checkedIn = db.Column(db.Boolean)


    def __init__(self, isbn, title, author_first_name, author_last_name, genre, publisher, description, checkedIn=True, checkedOutDate=None):
        self.isbn = isbn
        self.title = title
        self.author_first_name = author_first_name
        self.author_last_name = author_last_name
        self.genre = genre
        self.publisher = publisher
        self.description = description
        self.checkedIn = checkedIn
        self.checkedOutDate = checkedOutDate


    def validate(self):
        valid = True
        if not validateISBN(self.isbn):
            valid = False
        if not validateLength(self.isbn, 'isbn', 18):
            valid = False
        if not validateLength(self.title, 'Title', 200):
            valid = False
        if not validateLength(self.author_first_name, 'Author first name', 30):
            valid = False
        if not validateLength(self.author_last_name, 'Author last name', 30):
            valid = False
        if not validateLength(self.genre, 'Genre', 30):
            valid = False
        if not validateLength(self.publisher, 'Publisher', 80):
            valid = False
        if not validateLength(self.description, 'Description', 1000):
            valid = False
        return valid

class Customer(db.Model):
    library_id = db.Column(db.String(8), primary_key=True)
    customer_first_name = db.Column(db.String(30))
    customer_last_name = db.Column(db.String(30))

    def __init__(self, library_id, customer_first_name, customer_last_name):
        self.library_id = library_id
        self.customer_first_name = customer_first_name
        self.customer_last_name = customer_last_name

class Administrator(db.Model):
    admin_id = db.Column(db.String(8), primary_key=True)
    password = db.Column(db.String(40))
    administrator_first_name = db.Column(db.String(30))
    administrator_last_name = db.Column(db.String(30))

    def __init__(self, admin_id, password, administrator_first_name, administrator_last_name):
        self.admin_id = admin_id
        self.password = password
        self.administrator_first_name = administrator_first_name
        self.administrator_last_name = administrator_last_name

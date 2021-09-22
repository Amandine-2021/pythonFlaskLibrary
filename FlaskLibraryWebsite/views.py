# filename: views.py
# Final project CSC217-Python FlaskLibrary
# Amandine Velamala

from flask import Blueprint, render_template, request, flash
from . import db
from .models import Book, Administrator, Customer
from .validationHelper import validateField
from .starterScriptDB import bookList, customerList, adminList
from datetime import date, timedelta

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    #fillDatabase()
    return render_template("index.html")

@views.route("/displayAllBooks", methods=['POST'])
def displayAllBooks():
    queryResults = db.session.query(Book).all()
    today= date.today()
    return render_template('results.html', results=queryResults, today=today)

@views.route("/search", methods=['POST'])
def search():
    if request.method == 'POST':
        searchField = request.form['searchField']
        searchTerm = request.form['searchTerm']
        if len(searchTerm) < 1:
            flash('Search box should not be empty', category='error')
        else:
            if searchField != 'isbn':
                searchTerm = searchTerm.lower().capitalize()
            kwargs = {searchField: searchTerm}
            queryResults = Book.query.filter_by(**kwargs).all()
            today = date.today()
            return render_template('results.html', results=queryResults, searchField=searchField, searchTerm=searchTerm, today=today)
        return render_template('index.html')

@views.route("/addBook", methods=['GET', 'POST'])
def addBook():
    if request.method == 'POST':
        formData = request.form
        adminID = formData['adminID'].strip()
        adminPwd = formData['password'].strip()
        isbn = formData['isbn'].strip()
        title = formData['title'].strip().lower().capitalize()
        author_first_name = formData['author_first_name'].strip().lower().capitalize()
        author_last_name = formData['author_last_name'].strip().lower().capitalize()
        genre = formData['genre'].strip().lower().capitalize()
        publisher = formData['publisher'].strip().lower().capitalize()
        description = formData['description'].strip()
        newBook = Book(isbn, title, author_first_name, author_last_name, genre, publisher, description)
        validAdmin = validateAdmin(adminID, adminPwd)
        if newBook.validate():
            queryResult = Book.query.filter_by(isbn=isbn).first()
            if not queryResult:
                if validAdmin:
                    db.session.add(newBook)
                    db.session.commit()
                    flash(f'"{title}" by {author_first_name} {author_last_name} was succesfully added!', category='success')
                else:
                    return render_template("addBook.html", newBook=newBook)
            else:
                flash('A book with the same ISBN was found in the database. Unable to add a duplicate.', category='error')
        else:
            return render_template("addBook.html", newBook=newBook)
    return render_template("addBook.html")

@views.route("/deleteBook", methods=['GET', 'POST'])
def deleteBook():
    if request.method == 'POST':
        adminID = request.form['adminID'].strip()
        adminPwd = request.form['password'].strip()
        isbnToDelete = request.form['isbn'].strip()
        queryResult = Book.query.filter_by(isbn=isbnToDelete).first()
        validAdmin = validateAdmin(adminID, adminPwd)
        if validAdmin:
            if queryResult:
                Book.query.filter_by(isbn=isbnToDelete).delete()
                db.session.commit()
                flash(f'"{queryResult.title}" by {queryResult.author_first_name} {queryResult.author_last_name} '
                      f' with ISBN {isbnToDelete} was succesfully deleted!', category='success')
            else:
                flash(f'ISBN {isbnToDelete} was not found. Database has not been modified', category='error')
    return render_template("deleteBook.html")

@views.route("/editBook", methods=['GET', 'POST'])
def editBook():
    if request.method == 'POST':
        adminID = request.form['adminID'].strip()
        adminPwd = request.form['password'].strip()
        isbnToEdit = request.form['isbn'].strip()
        queryResult = Book.query.filter_by(isbn=isbnToEdit).first()
        validAdmin = validateAdmin(adminID, adminPwd)
        if validAdmin:
            if queryResult:
                fieldType = request.form['newEntryType']
                fieldData = request.form['newEntryData'].lower().capitalize()
                if validateField(fieldType, fieldData):
                    fillField(fieldType, fieldData, queryResult)
                    db.session.commit()
                    flash(f'ISBN {isbnToEdit}: {fieldType} was succesfully edited to {fieldData}', category='success')
            else:
                flash(f'ISBN {isbnToEdit} was not found. It cannot be modified', category='error')
    return render_template("editBook.html")

@views.route("/changeBookStatus", methods=['GET', 'POST'])
def changeBookStatus():
    if request.method == 'POST':
        libraryID = request.form['libraryID']
        todo = request.form['actionType']
        isbn = request.form['isbn']
        if libraryID == '':
            flash('Enter your library ID when you want to checkout or return a book', category='error')
        else:
            if validateCustomer(libraryID):
                queryResult = Book.query.filter_by(isbn=isbn).first()
                if todo == 'checkout':
                    queryResult.checkedIn = False
                    queryResult.checkedOutDate = date.today()
                    db.session.commit()
                    flash(f'{queryResult.title} was succesfully checked out. It is due in 1 week on {date.today() + timedelta(days=7)}',category='success')
                elif todo == 'return':
                    queryResult.checkedIn = True
                    queryResult.checkedOutDate = None
                    db.session.commit()
                    flash(f'{queryResult.title} was succesfully returned. Thank you.', category='success')
        return render_template("/base.html")

def validateAdmin(adminID, adminPwd):
    validAdmin = False
    admin = Administrator.query.filter_by(admin_id=adminID).first()
    if admin:
        if (admin.password == adminPwd):
            validAdmin = True
        else:
            flash('Incorrect password, try again.', category='error')
    else:
        flash(f'Invalid Administrator', category='error')
    return validAdmin

def validateCustomer(custID):
    validCustomer = False
    customer = Customer.query.filter_by(library_id=custID).first()
    if customer:
        validCustomer = True
    else:
        flash(f'Invalid library Id. No customer under that ID.', category='error')
    return validCustomer

def fillField(fieldType, fieldData, queryResult):
    if fieldType == 'title':
        queryResult.title = fieldData
    elif fieldType == 'author_first_name':
        queryResult.author_first_name = fieldData
    elif fieldType == 'author_last_name':
        queryResult.author_last_name = fieldData
    elif fieldType == 'genre':
        queryResult.genre = fieldData
    elif fieldType == 'publisher':
        queryResult.publisher = fieldData
    elif fieldType == 'description':
        queryResult.description = fieldData

def fillDatabase():
    for book in bookList:
        db.session.add(book)
    for customer in customerList:
        db.session.add(customer)
    for admin in adminList:
        db.session.add(admin)
    db.session.commit()
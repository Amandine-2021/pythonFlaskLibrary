# filename: __init__.py
# Final project CSC217-Python FlaskLibrary
# Amandine Velamala

from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "library.db"

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.secret_key = "library secret key"
    db.init_app(app)
    from .views import views
    app.register_blueprint(views, url_prefix='/')
    from .models import Book, Customer, Administrator
    create_database(app)
    return app

def create_database(app):
    if not path.exists('FlaskLibraryWebsite/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')



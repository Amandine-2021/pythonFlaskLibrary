# filename: main.py
# Final project CSC217-Python FlaskLibrary
# Amandine Velamala

from FlaskLibraryWebsite import create_app

app = create_app()

if __name__ == '__main__':
    app.run(port=4996, debug=True)
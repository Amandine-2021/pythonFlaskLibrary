# filename: validationHelper.py
# Final project CSC217-Python FlaskLibrary
# Amandine Velamala

import re
from flask import flash

def validateISBN(isbn):
    regex = re.compile('^(978-?|979-?)?\d{1,5}-?\d{1,7}-?\d{1,6}-?\d{1,3}$')
    #regex = re.compile("(?=[-0-9 ]{17}$|[-0-9X ]{13}$|[0-9X]{10}$)(?:97[89][- ]?)?[0-9]{1,5}[- ]?(?:[0-9]+[- ]?){2}[0-9X]$")
    match = regex.match(str(isbn))
    if not match:
        flash('Invalid isbn number', category='error')
        return False
    else:
        return True

def validateLength(input, field, maxLength):
    if len(input) < 1:
        flash(f'{field} field should not be empty', category='error')
        return False
    elif len(input) > maxLength:
        flash(f'{field} field should be less than {maxLength} characters', category='error')
        return False
    else:
        return True

def validateField(fieldType, fieldData):
    valid = True
    if fieldType == 'title':
         valid = validateLength(fieldData, 'Title', 200)
    elif fieldType == 'author_first_name':
        valid = validateLength(fieldData, 'Author first name', 30)
    elif fieldType == 'author_last_name':
        valid = validateLength(fieldData, 'Author last name', 30)
    elif fieldType == 'genre':
        valid = validateLength(fieldData, 'Genre', 30)
    elif fieldType == 'publisher':
        valid = validateLength(fieldData, 'Publisher', 80)
    elif fieldType == 'description':
        validateLength(fieldData, 'Description', 1000)
    return valid


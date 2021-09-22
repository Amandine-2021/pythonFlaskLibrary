# filename: starterScriptDB.py.py
# Final project CSC217-Python FlaskLibrary
# Amandine Velamala

from .models import Book, Customer, Administrator
from datetime import date

bookList = []
book1 = Book("1593279507", "Eloquent javascript", "Martin", "Haverbeke",  "Programming", "No starch press",
                  "This much anticipated and thoroughly revised third edition of Eloquent JavaScript "
                  "dives deep into the JavaScript language to show you how to write beautiful, effective code. "
                  "It has been updated to reflect the current state of Java¬Script and web browsers and includes "
                  "brand-new material on features like class notation, arrow functions, iterators, "
                  "async functions, template strings, and block scope. A host of new exercises have also been added to "
                  "test your skills and keep you on track.")
book2 = Book("1118008189","Html and css: design and build websites", "Jon", "Duckett", "Programming", "John wiley & sons",
              "Whether you want to design and build websites from scratch or take more control over an existing site, this "
              "book will help you create attractive, "
              "user-friendly web content. We understand that code can be intimidating, but take a look inside and you will "
              "see how this guide differs from many traditional programming books. Each page introduces a new topic in a "
              "simple, visual way with straightforward explanations accompanied by bite-sized code samples. You will also "
              "find practical help on how to organize and design the pages of your site so that you can create websites that look stunning and are easy to use. "
              "No previous experience needed.", False, date(2021,4,25))
book3 = Book("0307476464", "1Q84", "Haruki", "Murakami", "Fiction", "Vintage international", "A young woman named Aomame "
                "follows a taxi driver’s enigmatic suggestion and begins to notice puzzling discrepancies in the world "
                "around her. She has entered, she realizes, a parallel existence, which she calls 1Q84 —“Q is for ‘question "
                "mark.’ A world that bears a question.” Meanwhile, an aspiring writer named Tengo takes on a suspect "
                "ghostwriting project. He becomes so wrapped up with the work and its unusual author that, soon, his "
                "previously placid life begins to come unraveled.")
book4 = Book("978-0399255564", "The very hungry caterpillar", "Eric", "Carle", "Children's", "World of eric carle",
                "THE all-time classic picture book, from generation to generation, sold somewhere in the world every "
                "30 seconds! A sturdy and beautiful book to give as a gift for new babies, baby showers, birthdays, and "
                "other new beginnings!" )
book5 = Book("978-0593224243", "The very busy spider", "Eric", "Carle", "Children's", "World of eric carle",
             "Over 50 million people have fallen in love with The Very Busy Spider! Now parents and educators alike can "
             "introduce this beloved character to younger readers with this picture book by Eric Carle, creator of The "
             "Very Hungry Caterpillar. Early one morning a little spider blown by the wind spins her web on a farm yard "
             "fence post. One by one, the animals of the nearby farm try to distract her, yet the busy little spider keeps "
             "diligently at her work. When she is done, she is able to show everyone that not only is her creation quite "
             "beautiful, it is also quite useful!", False, date(2021,5,1))
book6 = Book("978-1617292231", "Grokking Algorithms: an illustrated guide for programmers and other curious people",
             "Aditya", "Bhargava", "Programming", "Manning publications", "Grokking Algorithms is a fully illustrated, friendly guide "
             "that teaches you how to apply common algorithms to the practical problems you face every day as a programmer."
             "You'll start with sorting and searching and, as you build up your skills in thinking algorithmically, you'll "
             "tackle more complex concerns such as data compression and artificial intelligence. Each carefully presented "
             "example includes helpful diagrams and fully annotated code samples in Python.", False, date(2021,4,21))
book7 = Book("978-0141439556", "Wuthering heights","Emily", "Bronte", "Fiction", "Penguin classics",
             "One of English literature's classic masterpieces—a "
             "gripping novel of love, propriety, and tragedy. Nominated as one of America’s best-loved novels by PBS’s "
             "The Great American Read. Lockwood, the new tenant of Thrushcross Grange, situated on the bleak Yorkshire moors, "
             "is forced to seek shelter one night at Wuthering Heights, the home of his landlord. There he discovers the "
             "history of the tempestuous events that took place years before. What unfolds is the tale of the intense "
             "love between the gypsy foundling Heathcliff and Catherine Earnshaw. Catherine, forced to choose between "
             "passionate, tortured Heathcliff and gentle, well-bred Edgar Linton, surrendered to the expectations of her "
             "class. As Heathcliff's bitterness and vengeance at his betrayal is visited upon the next generation, their "
             "innocent heirs must struggle to escape the legacy of the past.")
bookList.append(book1)
bookList.append(book2)
bookList.append(book3)
bookList.append(book4)
bookList.append(book5)
bookList.append(book6)
bookList.append(book7)

customerList = []
customer1 = Customer("12345678", "Amandine", "Velamala")
customer2 = Customer("01234567", "John", "Smith")
customer3 = Customer("23456789", "Francesca", "Conti")
customerList.append(customer1)
customerList.append(customer2)
customerList.append(customer3)

adminList = []
admin1 = Administrator("01010101", "password", "Maria", "Castillo")
admin2 = Administrator("02020202", "password", "Guillaume", "Dupont")
admin3 = Administrator("03030303", "password", "Caroline", "Johnson")
adminList.append(admin1)
adminList.append(admin2)
adminList.append(admin3)


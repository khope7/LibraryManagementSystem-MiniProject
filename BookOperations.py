#Initializing BookOperations Class as only import Class database to avoid circular import error
#Sites used for reference:
#https://builtin.com/articles/python-circular-import

#Importing, UserOperations, and regex
import UserOperations
import re

#Created Class BookOperations for Book Operations menu
class BookOperations:
    def book_operations():
        while True:
#Using try except block to catch for all other entries
            try:
                second_choice = int(input('''
Book Operations:
1. Add a new book
2. Borrow a book
3. Return a book
4. Search for a book
5. Display all books
6. Go to Main Operations  (press again to escape)
7. Exit

Choose any option: '''))
                if second_choice < 1 or second_choice > 8:
                    print("Unable to proceed, choice must be between 1 and 5. Please try again.")         
                elif second_choice == 1:
                    Book.add_book()          
                elif second_choice == 2:
                    Book.borrow_book()             
                elif second_choice == 3:
                    Book.return_book()              
                elif second_choice == 4:
                    Book.book_search()           
                elif second_choice == 5:
                    Book.display_books()          
                elif second_choice == 6:
                    break
                elif second_choice == 7:
                    Book.exit_system()
            except ValueError:
                print("Apologies, choice must be the number of one of the mentioned operations. Please try again.")


#Created Book class to hold all book keeping actions
class Book:
#Created empty dictionary to hold as empty library before books added
    library = {}
#Creating borrow list element for data entry
    borrow_list = []

#Created initialization for encaspulation
    def __init__(self, books):
        self.books = books

#Initializing getter to return library as books
    def get_books(self):
        return self.books

#Initializing setter to take in library as book details
    def set_books(self, book_details):
        self.books = book_details

#Created add book function to add book and attributes to current library
    def add_book():
        while True:
#Asking user for all book attributes
            new_book = input("What is the book title? ").title()
#Asking user to attribute book to author
            add_author = input("Please enter the first and last name of the book author: \n").title()
#Using regex split method to turn user entry into temporary list and eliminating spacing
            parts = re.split(r" ", add_author)
#Sends user back to function upon incorrect entry type
            if len(parts) < 2 or len(parts) > 2:
                    print("Apologies, please enter both first and last name of book author. Numbers and special characters are accepted.")
            else:
                add_author = parts[0] + " " + parts[1]
                break
#Created while True methods to ensure publish date and genre are entered with correct parameters
        while True:
            book_genre = input("What is the books genre? ").title()
            if book_genre.isalpha() == False:
                print("Apologies, entry must be characters only.")
            else:
                break
        while True:
            try:
                publish_date = int(input("When was the book published? ").title())
                if publish_date < 0 or publish_date > 2025:
                    print("Apologies, entry must be positive and current.")
                else:
                    break
            except ValueError:
                print("Apologies, entry must be a number. Please try again")

#Defaulting book status to available for borrow and return function
        availability_status = "Available"

#Adding book into library dictionary
        Book.library[new_book] = {"Book" : new_book, "Author" : add_author, "Genre" : book_genre, "Published" : publish_date, "Availability" : availability_status}
        print(f"Thank you, -{new_book}- has been added")

#Created borrow book class to allow for user to take book
    def borrow_book():
#Asking user to find user borrowing
        find_user = input("Please enter the first and last name of the user to borrow to: \n").title()
#Using regex split method to turn user entry into temporary list and eliminating spacing
        parts = re.split(r" ", find_user)
#Sends user back to function upon incorrect entry type
        if len(parts) < 2 or len(parts) > 2:
                print("Apologies, entry must have first and last name of any user added to the user list. Numbers and special characters are accepted.")
                BookOperations.book_operations()
        else:
            borrowing_user = parts[0] + " " + parts[1]
            if borrowing_user in UserOperations.User.user_details:
                print(f"Here is a list of all books in current library:\n{Book.get_books()}")
                borrow_choice = input(f"What book would you like {borrowing_user} to take? ").title()
            else:
                print("Apologies, entry must have first and last name of any user added to the user list. Numbers and special characters are accepted.")
                BookOperations.book_operations()

#Created nested if to find book and check for availability, returning user to Book Operations for possible entries
        if borrow_choice in books_catelog.get_books():
            if Book.library[borrow_choice]["Availability"] == "Available":
                Book.library[borrow_choice]["Availability"] = "Taken"
                Book.borrow_list.append(borrow_choice)
                UserOperations.User.user_details[borrowing_user]["Borrowed Books"] = Book.borrow_list
                print(f"{borrow_choice}: Has been borrowed")
            elif Book.library[borrow_choice]["Availability"] == "Taken":
                print("Apologies, entry has already been taken")
        else:
            print("Apologies, entry is not within library")
    
#Created return book class to all for user to return book
    def return_book():
        find_user = input("Please enter the first and last name of the user to return from: \n").title()
#Using regex split method to turn user entry into temporary list and eliminating spacing
        parts = re.split(r" ", find_user)
#Sends user back to function upon incorrect entry type
        if len(parts) < 2 or len(parts) > 2:
                print("Apologies, entry must have first and last name of any user added to the user list. Numbers and special characters are accepted.")
                BookOperations.book_operations()
#Returns user name detail and reformats
        else:
            returning_user = parts[0] + " " + parts[1]

#Checks if user exists, if user has any books and if so prints and if not returns user back to Book Operations menu
            if returning_user in UserOperations.User.user_details:
                if UserOperations.User.user_details[returning_user]["Borrowed Books"] == "N/A":
                    print("Apologies, user has no books to return.")
                    BookOperations.book_operations()
                else:
                    print("Here are the books this user is currently borrowing.")
                    print(UserOperations.User.user_details[returning_user]["Borrowed Books"])
                    return_choice = input(f"What book would you like {returning_user} to return? ").title()
            else:
                print("Apologies, please enter both first and last name of any user added to the user list. Numbers and special characters are accepted.")
                BookOperations.book_operations()

#Checks if return choice is in library and changes borrowed status
        if return_choice in UserOperations.User.user_details[returning_user]["Borrowed Books"]:
            if Book.library[return_choice]["Availability"] == "Taken":
                Book.library[return_choice]["Availability"] = "Available"
#Removes specific borrowed book from that specific users detail
                UserOperations.User.user_details[returning_user]["Borrowed Books"].pop(UserOperations.User.user_details[returning_user]["Borrowed Books"].index(return_choice))
                print(f"{return_choice}: Has been returned")
                BookOperations.book_operations()

#Checks on book availability and returns user upon available status
            elif Book.library[return_choice]["Availability"] == "Available":
                print("Apologies, entry has not been taken")
                BookOperations.book_operations()
#Returns user to Book Operations if entry is not within library          
        else:
            print("Apologies, entry is not within library")
            BookOperations.book_operations()

#Created book search class to allow for user to find and see book chosen
    def book_search():
        search_choice = input("What book would you like to search? ").title()
        if search_choice in books_catelog.get_books():
            print(f"Here are the details for: -{search_choice}-")
            print(Book.library[search_choice])
            BookOperations.book_operations() 
        else:
            print("Apologies, entry is not within library")
            BookOperations.book_operations()

#Created display books class to allow for user to see all current books within library
    def display_books():
        count = 0
        print("\nHere is the current Library:")
        for book, attributes in books_catelog.get_books().items():
            count += 1
            print(f"{count}. {book} {attributes}")
        BookOperations.book_operations()
    
#Created Book Operations Exit System
    def exit_system():
        print(books_catelog.get_books())
        exit()

#Created books_catelog obj for encapsulation method
books_catelog = Book(Book.library)


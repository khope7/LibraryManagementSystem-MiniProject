import main
import AuthorOperations
import UserOperations
import re

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
4. Go to Main Operations
5. Go to Author Operations
6. Go to User Operations
7. Exit

Choose any option: '''))
                if second_choice < 1 or second_choice > 6:
                    print("Unable to proceed, choice must be between 1 and 5. Please try again.")
                    break
                elif second_choice == 1:
                    Book.add_book()
                    break
                elif second_choice == 2:
                    Book.borrow_book()
                    break
                elif second_choice == 3:
                    Book.return_book()
                    break
                elif second_choice == 4:
                    Book.book_search()
                    break
                elif second_choice == 5:
                    Book.display_books()
                    break
                elif second_choice == 6:
                    main.main()
                    break
                elif second_choice == 7:
                    AuthorOperations.AuthorOperations.author_operations()
                    break  
                elif second_choice == 8:
                    UserOperations.UserOperations.user_operations()
                    break  
                elif second_choice == 9:
                    Book.exit_system()
                    break

            except ValueError:
                print("Apologies, choice must be the number of one of the mentioned operations. Please try again.")


#Created Book class to hold all book keeping actions
class Book:
#Created empty dictionary to hold as empty library before adds
    library = {}

    def __init__(self, books):
        self.books = books

#Initializing getters to return name and budget info
    def get_books(self):
        return self.books

#Initializing setters to take in new name and amount
    def set_books(self, book_details):
        self.books = book_details

#Created add book function to add book to current library
    def add_book():       
#Asking user for all book attributes
        new_book = input("What is the book title? ").title()
        book_author_first = input("What is the authors first name? ").title()
        book_author_last = input("what is the authors last name? ").title()
        book_author = book_author_first + " " + book_author_last
        book_genre = input("What is the books genre? ").title()
        publish_date = input("When was the book published? ").title()
#Defaulting book status to available for borrow and return function
        availability_status = "Available"

#Adding book into library dictionary
        Book.library[new_book] = {"Book" : new_book, "Author" : book_author, "Genre" : book_genre, "Published" : publish_date, "Availability" : availability_status}

#Returning user back to book operations for user reentry
        BookOperations.book_operations()

#Created borrow book class to allow for user to take book
    def borrow_book():
        borrow_list = []
        find_user = input("Please enter the first and last name of the user to borrow to: \n").title()
#Using regex split method to turn user entry into temporary list and eliminating spacing
        parts = re.split(r" ", find_user)
#Sends user back to function upon incorrect entry type
        if len(parts) < 2 or len(parts) > 2:
                print("Apologies, please enter both first and last name of any user added to the user list. Numbers and special characters are accepted.")
                Book.borrow_book()
#Returns user name detail and reformats
        else:
            borrowing_user = parts[0] + " " + parts[1]
            if borrowing_user in UserOperations.User.user_details:
                Book.display_books()
                borrow_choice = input(f"What book would you like {borrowing_user} to take? ").title()
            else:
                print("Apologies, please enter both first and last name of any user added to the user list. Numbers and special characters are accepted.")
                BookOperations.book_operations()

#Created nested if to find book and check for availability, returning user to Book operations for possible entries
        if borrow_choice in books_catelog.get_books():
            if Book.library[borrow_choice]["Availability"] == "Available":
                Book.library[borrow_choice]["Availability"] = "Taken"
                UserOperations.User.user_details[borrowing_user]["Borrowed Books"] = borrow_list.append(borrow_choice)

                print(f"{borrow_choice}: Has been borrowed, you have 1 week. Will release firebreathing dragons upon non-return")

                BookOperations.book_operations()
            else:
                print("Apologies, entry has already been taken")
                BookOperations.book_operations()
        else:
            print("Apologies, entry is not within library")
            BookOperations.book_operations()
        return borrow_list
    
#Created return book class to all for user to return book
    def return_book(borrow_list):
        find_user = input("Please enter the first and last name of the user to return from: \n").title()
#Using regex split method to turn user entry into temporary list and eliminating spacing
        parts = re.split(r" ", find_user)
#Sends user back to function upon incorrect entry type
        if len(parts) < 2 or len(parts) > 2:
                print("Apologies, please enter both first and last name of any user added to the user list. Numbers and special characters are accepted.")
                Book.borrow_book()
#Returns user name detail and reformats
        else:
            returning_user = parts[0] + " " + parts[1]
            if returning_user in UserOperations.User.user_details:
                if UserOperations.User.user_details[returning_user]["Borrowed Books"] == "N/A":
                    print("Apologies, user has no books to return.")
                    BookOperations.book_operations()
                else:
                    print(UserOperations.User.user_details[returning_user]["Borrowed Books"])
                    return_choice = input(f"What book would you like {returning_user} to return? ").title()
            else:
                print("Apologies, please enter both first and last name of any user added to the user list. Numbers and special characters are accepted.")
                BookOperations.book_operations()

        if return_choice in UserOperations.User.user_details[returning_user]["Borrowed Books"]:
            if Book.library[return_choice]["Availability"] == "Taken":
                Book.library[return_choice]["Availability"] = "Available"
                UserOperations.User.user_details[returning_user]["Borrowed Books"].pop(return_choice)
                print(f"{return_choice}: Has been returned, firebreathing dragons have been recaged")
                BookOperations.book_operations()   
            else:
                print("Apologies, entry has not been taken")
                BookOperations.book_operations()                
        else:
            print("Apologies, entry is not within library")
            BookOperations.book_operations()

#Created book search class to allow for user to find and see book chosen
    def book_search():
        search_choice = input("What book would you like to search? ").title()
        if search_choice in books_catelog.get_books():
            print(f"Here are the details for {search_choice}")
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
    
    def exit_system():
        print(books_catelog.get_books())
        exit()

books_catelog = Book(Book.library)


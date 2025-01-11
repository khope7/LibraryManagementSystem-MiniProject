#In this project, you will apply Object-Oriented Programming (OOP) principles in Python to develop an advanced Library Management System.
#This command-line-based application is designed to streamline the management of books and resources within a library.
#Your mission is to create a robust system that allows users to browse, borrow, return, and explore a collection of books while demonstrating your proficiency in OOP principles
#and the use of modules.

#Enhanced User Interface (UI) and Menu:
#Create an improved, user-friendly command-line interface (CLI) for the Library Management System with separate menus for each class of the system.


#Writing code for LibraryManagementSystem MiniProject


#Importing call Classes for user redirect
import BookOperations
import UserOperations
import AuthorOperations

#Creating main as user interface function to introduce gui and take in choices of 1-4
def main():
#Creating while loop to ask for user re entry
    while True:
#Using try except block to catch for all other entries
        try:
            first_choice = int(input('''Welcome to the Library Management System 
Main Menu:
1. Book Operations
2. User Operations
3. Author Operations
4. Quit

Choose any option: '''))
            
#Catches integers outside of range 1-4 and any alpha entries
            if first_choice < 1 or first_choice > 4:
                print("Unable to proceed, choice must be between 1 and 4. Please try again.")
            elif first_choice == 1:
                BookOperations.BookOperations.book_operations()                
            elif first_choice == 2:
                UserOperations.UserOperations.user_operations()                
            elif first_choice == 3:
                AuthorOperations.AuthorOperations.author_operations()                
            elif first_choice == 4:
                exit_system()
                break
        except ValueError:
            print("Apologies, choice must be the number of one of the mentioned operations. Please try again.")
        except UnboundLocalError:
            main()

#Created exit System for main function
def exit_system():
    exit()

#Calling main method for user entry
main()
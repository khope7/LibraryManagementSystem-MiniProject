#Created regex import
import re

#Created Class AuthorOperations for Author Operations menu
class AuthorOperations:
    def author_operations():
        while True:
#Using try except block to catch for all other entries
            try:
                second_choice = int(input('''
Author Operations:
1. Add a new author
2. View author details
3. Display all authors
4. Go to Main Operations (press again to escape)
5. Exit

Choose any option: '''))
                if second_choice < 1 or second_choice > 5:
                    print("Unable to proceed, choice must be between 1 and 4. Please try again.")
                elif second_choice == 1:
                    Author.add_author()                  
                elif second_choice == 2:
                    Author.display_author_detail()                  
                elif second_choice == 3:
                    Author.display_authors_details()               
                elif second_choice == 4:
                    break                 
                elif second_choice == 5:
                    Author.exit_system()                                        
            except ValueError:
                print("Apologies, choice must be the number of one of the mentioned operations. Please try again.")
            except UnboundLocalError:
                AuthorOperations.author_operations()   

#Created Book class to hold all book keeping actions
class Author:
    authors_details = {}

    def __init__(self, author_details):
        self.display_users = author_details

#Initializing getters to return name and budget info
    def get_author_details(self):
        return self.display_users

#Initializing setters to take in new name and amount
    def set_author_details(self, details):
        self.display_users = details


#Creating add author method to add new author in first and last name
    def add_author():
        new_author_check = input("What is the first and last name of the new author? ").title()
#Using regex split method to turn user entry into temporary list and eliminating spacing
        parts = re.split(r" ", new_author_check)
#Sends user back to function upon incorrect entry type
        if len(parts) < 2 or len(parts) > 2:
                print("Apologies, entry must have both first and last name only. Numbers and special characters are accepted.")
                AuthorOperations.author_operations()
#Returns author name detail and reformats
        else:
            author_name = parts[0] + " " + parts[1]

#Checks if author is in authors details and adds if not, sends user back for either options
        if author_name not in Author.authors_details:
#Created function to add author and authors BIO into dictionary after asking user for entry
            authors_details = input("Please enter the author's BIO: ")
            Author.authors_details[author_name] = {"Author" : author_name, "Details" : authors_details}
        else:
            print("Apologies, author mentioned is already added")
        
        AuthorOperations.author_operations()
 
#Created display author detail function which searches for the author mentioned and returns the author displayed
    def display_author_detail():
        search = False
        searched_author_check = input("What is the first and last name of the author you would like to search? ").title()
#Using regex split method to turn user entry into temporary list and eliminating spacing
        parts = re.split(r" ", searched_author_check)
#Sends user back to function upon incorrect entry type
        if len(parts) < 2 or len(parts) > 2:
                print("Apologies, please enter both first and last name only. Numbers and special characters are accepted.")
        for author in authors.get_author_details():
            if searched_author_check in author:
                    search = True
        if search == True:
            print (f"Here are the details for your searched user:")
            for author, detail in authors.get_author_details().items():
                if searched_author_check in author:
                    print(f"{searched_author_check} - BIO: {detail["Details"]}")
        else:
            print ("Apologies, search failed: author searched must be in author list. Please try again.")
        
        AuthorOperations.author_operations()


#Created display authors details function to display all authors and author details with for loop for formatting
    def display_authors_details():
        print("Here is your current list of authors")
        for author, detail in authors.get_author_details().items():
            print(f"{author} - BIO: {detail["Details"]}")
        AuthorOperations.author_operations()
    
#Created exit system for Author class
    def exit_system():
        print("Thank you")
        exit()

#Created authors obj for encapsulation method
authors = Author(Author.authors_details)
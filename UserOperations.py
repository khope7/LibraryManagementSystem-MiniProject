import re
import random

import main
import AuthorOperations
import BookOperations

class UserOperations:
    def user_operations():
        while True:
    #Using try except block to catch for all other entries
            try:
                second_choice = int(input('''
User Operations:
1. Add a new user
2. View user details
3. Display all users
4. Go to Main Operations
5. Go to Book Operations
6. Go to User Operations
7. Exit  
                                        
Choose any option: '''))
                                            
                if second_choice < 1 or second_choice > 4:
                    print("Unable to proceed, choice must be between 1 and 5. Please try again.")
                    break
                elif second_choice == 1:
                    User.user_name()
                    break
                elif second_choice == 2:
                    User.user_details()
                    break
                elif second_choice == 3:
                    User.display_user()
                    break
                elif second_choice == 4:
                    main.main()
                    break
                elif second_choice == 5:
                    BookOperations.book_operations()
                    break  
                elif second_choice == 6:
                    AuthorOperations.author_operations()
                    break  
                elif second_choice == 7:
                    User.exit_system()
            except ValueError:
                print("Apologies, choice must be the number of one of the mentioned operations. Please try again.")

class User:
    user_details = {}

    def __init__(self, user_details):
        self.display_users = user_details

#Initializing getters to return name and budget info
    def get_user_details(self):
        return self.display_users

#Initializing setters to take in new name and amount
    def set_user_details(self, details):
        self.display_users = details

#Created user_name function to receive first and last name of new user
    def add_user():
        users_id = []
        code = ""
        number_generator = [1,2,3,4,5,6,7,8,9,0]
    
        new_user_check = input("What is the first and last name of the new user? ").title()
#Using regex split method to turn user entry into temporary list and eliminating spacing
        parts = re.split(r" ", new_user_check)
#Sends user back to function upon incorrect entry type
        if len(parts) < 2 or len(parts) > 2:
                print("Apologies, please enter both first and last name only. Numbers and special characters are accepted.")
                User.add_user()
#Returns user name detail and reformats
        else:
            new_user = parts[0] + " " + parts[1]

            for choice in range(5):
                id_digit = random.choice(number_generator)
                users_id.append(id_digit)

            for digit in users_id:
                code = code + str(digit)
                user_id = code

        User.user_details[new_user] = {"User" : new_user, "UserID" : user_id, "Borrowed Books": "N/A"}

    def exit_system():
        exit()

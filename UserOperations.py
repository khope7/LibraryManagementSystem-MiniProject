#Importing regex and random methods
import re
import random

#Created User Operations class for User Operations menu
class UserOperations:
    def user_operations():
        while True:
            try:
                second_choice = int(input('''
User Operations:
1. Add a new user
2. View user details
3. Display all users
4. Go to Main Operations  (press again to escape)
5. Exit  
                                        
Choose any option: '''))
                                            
                if second_choice < 1 or second_choice > 4:
                    print("Unable to proceed, choice must be between 1 and 5. Please try again.")
                elif second_choice == 1:
                    User.add_user()
                elif second_choice == 2:
                    User.search_user_details()
                elif second_choice == 3:
                    User.display_user_details()
                elif second_choice == 4:
                    break
                elif second_choice == 5:
                    User.exit_system()
            except ValueError:
                print("Apologies, choice must be the number of one of the mentioned operations. Please try again.")

#Created user class for user details and user attributes with encapsulation
class User:
    user_details = {}

    def __init__(self, user_details):
        self.display_users = user_details

    def get_user_details(self):
        return self.display_users

    def set_user_details(self, details):
        self.display_users = details

#Created add_user function to receive first and last name of new user
    def add_user():
#Initializing ID list, code, and number generator for ID creation
        users_id = []
        code = ""
        number_generator = [1,2,3,4,5,6,7,8,9,0]
    
        new_user_check = input("What is the first and last name of the new user? ").title()
        parts = re.split(r" ", new_user_check)

        if len(parts) < 2 or len(parts) > 2:
                print("Apologies, please enter both first and last name only. Numbers and special characters are accepted.")
                UserOperations.user_operations()
        elif new_user_check in User.user_details:
                print("Apologies, user is already added to the user list.")
                UserOperations.user_operations()       
        else:
            new_user = parts[0] + " " + parts[1]

#Creating loop with 5 range for 5 digit ID generator
            for choice in range(5):
                id_digit = random.choice(number_generator)
                users_id.append(id_digit)

            for digit in users_id:
                code = code + str(digit)
                user_id = code

#Adds user name and UserID to user details list
        User.user_details[new_user] = {"User" : new_user, "UserID" : user_id, "Borrowed Books": "N/A"}

        print(f"Thank you, user: -{new_user_check}, UID: {user_id}- has been added.")

#Created search user details function to search for and display user with user detail
    def search_user_details():
        search = False
        searched_user_check = input("What is the first and last name of the user you would like to search? ").title()
#Using regex split method to turn user entry into temporary list and eliminating spacing
        parts = re.split(r" ", searched_user_check)
#Sends user back to function upon incorrect entry type
        if len(parts) < 2 or len(parts) > 2:
                print("Apologies, please enter both first and last name only. Numbers and special characters are accepted.")
        for user in users.get_user_details():
                if searched_user_check in user:
                    search = True
        if search == True:
            print (f"Here are the details for your searched user:\n{User.user_details[searched_user_check]}")
        else:
            print ("Apologies, search failed: User searched must be in user list. Please try again.")
        
        UserOperations.user_operations()       

#Created function to display all users
    def display_user_details():
        print("Here is your current list of users")
#using for loop for formatting
        for user, detail in users.get_user_details().items():
            print(f"{user} - Info: {detail}")
        UserOperations.user_operations()      

#Created Exit System
    def exit_system():
        exit()

#Created users obj for encapsulation method
users = User(User.user_details)
# LibraryManagementSystem MiniProject

## Class Description
Hello! The LibraryManagementSystem is designed to collect data from the user for books, authors and user information and display the information when asked.

## main.py
The main class file is designed to help the user navigate to each subclass within the project. It is also used as the central redirect menu and is needed for borrowing and returning books as the user must enter user data first from the UserOperations class and then return to the main menu, then back into the BookOperations class to borrow a book for the any user previously created in the UserOperations class. AuthorOperations is a stand alone class.

## BookOperations.py
The BookOperations class file is designed to take in book data such as title, author, genre, publish date, and return the inforation into a general data collection dictionary named "library", along with borrow and return status for each book. The BookOperations class also takes in borrow and return requests and reallocates based on which user has taken and returned specific books. The BookOperations class also alows for the user to search any book within the library and displays that searched book or option 5 will allow for the user to see all books. Options 6 redirects to the main menu and option 7 exits the program.

## UserOperations.py
The UserOperations class file is designed to take in the user name and automate a random 5 digit user ID. The user information is then stored within a data collection dictionary named users details. There is also an option to display any user upon user search and display all users. Option 5 redirects to the main menu and option 6 exits the program.

## AuthorOperations.py
THe AuthorOperations class file is designed to take in new author first and last names along with author bios. There is also an option to display any author upon user search and display all authors. Option 4 redirects to the main menu and option 5 exits the program

## Additional note:
Redirecting to the main menu will take additional button presses depending on how my operations have been chosen within the subclass. Simply press the menu redirect key again to escape the subclass and return to the main menu.
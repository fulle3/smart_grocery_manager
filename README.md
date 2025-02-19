Smart Grocery List Manager
Project Overview
The Smart Grocery List Manager is a command-line Python application designed to help users efficiently manage their grocery lists. 
Users can add, view, delete, and mark grocery items as purchased, as well as track expiration dates and receive recipe suggestions based on available ingredients. 
The program saves data between sessions using JSON files, ensuring data persistence.
Installation Instructions

1 Prerequisites
Ensure you have the following installed:
Python 3.x
VS Code (Recommended)

2 Clone or Download the Project
Alternatively, manually download the project folder and open it in VS Code.

3 Install Required Libraries
This project only uses built-in Python libraries (json, datetime, unittest, os), so no external dependencies are required.

4 Run the Program
Navigate to the project folder and execute the following command:
python main.py



Features List
Add Grocery Items: Users can enter grocery items, categorize them, and set expiration dates. View Grocery List: Displays all items, their categories, and expiration status. Mark Items as Purchased: Users can mark specific items as "purchased." Data Persistence: Saves grocery items in a JSON file so data remains available between sessions. Expiration Tracking: Notifies users when items are about to expire. Advanced Recipe Suggestions: Provides meal ideas based on available grocery items and ensures valid matches.: Provides meal ideas based on available grocery items.

Usage Guide
1 Recipe Suggestions 
Select Option 4
The system will analyze available grocery items and suggest recipes
If no matching recipes are found, a message will be displayed

2 Main Menu
Upon running the program, the following menu is displayed:
Smart Grocery List Manager
1. Add Grocery Item
2. View Grocery List
3. Mark Item as Purchased
4. View Recipe Suggestions
5. Exit

3 Adding a Grocery Item
Select Option 1
Enter the item name, category, and expiration date (YYYY-MM-DD format)
Item is saved and confirmed

4 Viewing the Grocery List
Select Option 2 to see all saved items
Items display name, category, and purchase status

5 Marking Items as Purchased
Select Option 3
Choose an item number from the displayed list
The item is updated to "purchased"

6 Exiting the Program
Select Option 4 to exit the program

Testing the Program
To ensure the program runs correctly, use the unittest module:
1 Run All Tests
Open the terminal and navigate to the project folder. Run:
python -m unittest test_smart_grocery.py

2 Expected Output if All Tests Pass
....
----------------------------------------------------------------------
Ran 6 tests in 0.XXXs

OK

(Each dot . represents a successful test.)


File Structure
smart_grocery_manager/
│-- main.py              # Main program file
│-- grocery_item.py      # GroceryItem class
│-- recipe.py            # Recipe class
│-- database_handler.py  # Handles JSON storage
│-- test_smart_grocery.py # Automated unit tests (including recipe tests)
│-- grocery_data.json    # Stores saved grocery items
│-- README.md            # Documentation file
Additional Notes
Ensure grocery_data.json exists before running, or the program will create it automatically.
If entering an incorrect option, the program will prompt for a valid selection.
Data validation prevents duplicate or incorrect entries.





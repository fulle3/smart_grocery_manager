from grocery_item import GroceryItem
from database_handler import DatabaseHandler

def display_menu():
    print("\nSmart Grocery List Manager")
    print("1. Add Grocery Item")
    print("2. View Grocery List")
    print("3. Mark Item as Purchased")
    print("4. Exit")


def add_grocery_item():
    name = input("Enter item name: ")
    category = input("Enter category: ")
    expiration_date = input("Enter expiration date (YYYY-MM-DD): ")
    
    item = GroceryItem(name, category, expiration_date)
    grocery_list = DatabaseHandler.load_data()
    grocery_list.append(item.to_dict())
    DatabaseHandler.save_data(grocery_list)
    print(f"{name} added successfully!")


def view_grocery_list():
    grocery_list = DatabaseHandler.load_data()
    if not grocery_list:
        print("No items in the grocery list.")
        return
    
    for index, item in enumerate(grocery_list, start=1):
        print(f"{index}. {item['name']} - {item['category']} - {item['status']}")


def mark_purchased():
    grocery_list = DatabaseHandler.load_data()
    view_grocery_list()
    try:
        choice = int(input("Enter the item number to mark as purchased: ")) - 1
        if 0 <= choice < len(grocery_list):
            grocery_list[choice]['status'] = 'purchased'
            DatabaseHandler.save_data(grocery_list)
            print("Item marked as purchased!")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_grocery_item()
        elif choice == "2":
            view_grocery_list()
        elif choice == "3":
            mark_purchased()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
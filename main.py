from grocery_item import GroceryItem
from database_handler import DatabaseHandler
from recipe import Recipe

def display_menu():
    print("\nSmart Grocery List Manager")
    print("1. Add Grocery Item")
    print("2. View Grocery List")
    print("3. Mark Item as Purchased")
    print("4. View Recipe Suggestions")
    print("5. Exit")


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

def view_recipe_suggestions():
    """Display recipes based on available grocery items."""
    grocery_list = DatabaseHandler.load_data()
    suggested_recipes = Recipe.get_suggested_recipes(grocery_list)

    if not suggested_recipes:
        print("No matching recipes found with your current grocery items.")
        return

    print("\nRecipe Suggestions:")
    for recipe in suggested_recipes:
        print(f"\n🍽 {recipe['name']}")
        print(f"Ingredients: {', '.join(recipe['ingredients'])}")
        print(f"Instructions: {recipe['instructions']}")


def main():
    """Main program loop for user interaction."""
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
            view_recipe_suggestions()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()

import unittest
from grocery_item import GroceryItem
from database_handler import DatabaseHandler
from recipe import Recipe
import os

class TestSmartGrocery(unittest.TestCase):

    def setUp(self):
        """Set up a temporary test file before running tests."""
        self.test_data_file = "test_grocery_data.json"
        DatabaseHandler.FILE_NAME = self.test_data_file  # Use test file instead of real data
        DatabaseHandler.save_data([])  # Start with an empty test file

    def tearDown(self):
        """Remove the test file after tests complete."""
        if os.path.exists(self.test_data_file):
            os.remove(self.test_data_file)

    def test_add_grocery_item(self):
        """Test that a grocery item is added correctly."""
        item = GroceryItem("Milk", "Dairy", "2025-01-30")
        grocery_list = DatabaseHandler.load_data()
        grocery_list.append(item.to_dict())
        DatabaseHandler.save_data(grocery_list)

        loaded_data = DatabaseHandler.load_data()
        self.assertEqual(len(loaded_data), 1)
        self.assertEqual(loaded_data[0]["name"], "Milk")
        self.assertEqual(loaded_data[0]["category"], "Dairy")
        self.assertEqual(loaded_data[0]["expiration_date"], "2025-01-30")

    def test_mark_purchased(self):
        """Test marking an item as purchased."""
        item = GroceryItem("Eggs", "Dairy", "2025-02-10")
        grocery_list = [item.to_dict()]
        DatabaseHandler.save_data(grocery_list)

        # Mark the first item as purchased
        grocery_list = DatabaseHandler.load_data()
        grocery_list[0]["status"] = "purchased"
        DatabaseHandler.save_data(grocery_list)

        loaded_data = DatabaseHandler.load_data()
        self.assertEqual(loaded_data[0]["status"], "purchased")

    def test_check_expiration(self):
        """Test expiration date tracking."""
        item_expired = GroceryItem("Old Bread", "Bakery", "2023-01-01")
        item_fresh = GroceryItem("Fresh Apples", "Produce", "2025-05-20")

        self.assertIn("expired", item_expired.check_expiration().lower())
        self.assertIn("still good", item_fresh.check_expiration().lower())

    def test_empty_grocery_list(self):
        """Ensure the system handles an empty grocery list correctly."""
        DatabaseHandler.save_data([])
        loaded_data = DatabaseHandler.load_data()
        self.assertEqual(len(loaded_data), 0)

    def test_recipe_suggestions_found(self):
        """Test if recipe suggestions are correctly generated based on available grocery items."""
        grocery_list = [
            {"name": "Flour", "category": "Baking", "expiration_date": "2025-06-01"},
            {"name": "Milk", "category": "Dairy", "expiration_date": "2025-06-05"},
            {"name": "Eggs", "category": "Dairy", "expiration_date": "2025-06-10"}
        ]
        suggested_recipes = Recipe.get_suggested_recipes(grocery_list)
        self.assertTrue(len(suggested_recipes) > 0)
        self.assertEqual(suggested_recipes[0]["name"], "Pancakes")

    def test_no_recipe_suggestions(self):
        """Test if no recipes are suggested when the grocery list lacks the required ingredients."""
        grocery_list = [
            {"name": "Rice", "category": "Grains", "expiration_date": "2025-07-01"},
            {"name": "Tomato", "category": "Vegetables", "expiration_date": "2025-06-15"}
        ]
        suggested_recipes = Recipe.get_suggested_recipes(grocery_list)
        self.assertEqual(len(suggested_recipes), 0)

if __name__ == "__main__":
    unittest.main()

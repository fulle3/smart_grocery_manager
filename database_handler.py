import json

class DatabaseHandler:
    """Handles saving and loading grocery data to/from a JSON file."""

    FILE_NAME = "grocery_data.json" # Name of the JSON file

    @staticmethod
    def save_data(data):
        """Save the grocery list data to a JSON file."""
        with open(DatabaseHandler.FILE_NAME, 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load_data():
        """Load the grocery list data from the JSON file.
        If the file does not exist, return an empty list.
        """
        try:
            with open(DatabaseHandler.FILE_NAME, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return [] # Return empty list if no file exists

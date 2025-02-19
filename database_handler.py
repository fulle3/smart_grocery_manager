import json

class DatabaseHandler:
    FILE_NAME = "grocery_data.json"

    @staticmethod
    def save_data(data):
        with open(DatabaseHandler.FILE_NAME, 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load_data():
        try:
            with open(DatabaseHandler.FILE_NAME, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
import json
from datetime import datetime

class GroceryItem:
    """Represents a grocery item with name, category, expiration date, and status."""

    def __init__(self, name, category, expiration_date):
        self.name = name # Name of the grocery item
        self.category = category # Category (e.g., Dairy, Produce)
        self.expiration_date = expiration_date # Expiration date (YYYY-MM-DD)
        self.status = "pending" # Default status: pending

    def check_expiration(self):
        """Check if the item has expired and return a warning if necessary."""
        today = datetime.today().strftime('%Y-%m-%d')
        if self.expiration_date < today:
            return f"WARNING: {self.name} has expired!"
        return "Item is still good."
    
    def mark_purchased(self):
        self.status = "purchased"

    def to_dict(self):
        return self.__dict__

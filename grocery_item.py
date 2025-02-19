import json
from datetime import datetime

class GroceryItem:
    def __init__(self, name, category, expiration_date):
        self.name = name
        self.category = category
        self.expiration_date = expiration_date
        self.status = "pending"

    def check_expiration(self):
        today = datetime.today().strftime('%Y-%m-%d')
        if self.expiration_date < today:
            return f"WARNING: {self.name} has expired!"
        return "Item is still good."
    
    def mark_purchased(self):
        self.status = "purchased"

    def to_dict(self):
        return self.__dict__
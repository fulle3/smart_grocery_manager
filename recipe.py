class Recipe:
    """Represents a recipe with ingredients and instructions."""

    SAMPLE_RECIPES = [
        {"name": "Pancakes", "ingredients": ["Flour", "Milk", "Eggs"], "instructions": "Mix ingredients and cook in a pan."},
        {"name": "Omelette", "ingredients": ["Eggs", "Cheese", "Salt"], "instructions": "Beat eggs, add cheese, and cook."},
        {"name": "Fruit Salad", "ingredients": ["Apple", "Banana", "Orange"], "instructions": "Chop ingredients and mix together."},
        {"name": "Grilled Cheese", "ingredients": ["Bread", "Cheese", "Butter"], "instructions": "Butter bread, add cheese, and grill."}
    ]

    @staticmethod
    def get_suggested_recipes(grocery_list):
        """Suggest recipes based on available grocery items."""
        suggested_recipes = []

        for recipe in Recipe.SAMPLE_RECIPES:
            if all(ingredient in [item['name'] for item in grocery_list] for ingredient in recipe["ingredients"]):
                suggested_recipes.append(recipe)

        return suggested_recipes

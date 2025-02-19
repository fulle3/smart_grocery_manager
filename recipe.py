class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def get_recipe_info(self):
        return f"{self.name}:\nIngredients: {', '.join(self.ingredients)}\nInstructions: {self.instructions}"
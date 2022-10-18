class Recipe:

    def __init__(self, dish_name, minutes, recipe):

        self.dish_name = dish_name
        self.minutes = int(minutes)
        self.recipe = recipe

    def show_recipe(self):
        print("Creating the text of recipe...")
        recipe = f"Name: {self.dish_name}\n" \
                 f"Minutes: {self.minutes}\n" \
                 f"Recipe: {self.recipe}"
        print("Text created")
        return recipe

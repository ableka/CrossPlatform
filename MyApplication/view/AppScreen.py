from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from MyApplication.model.dataset import Dataset
from MyApplication.model.recipe import Recipe


class AppScreen(Screen):
    name = StringProperty("Recipe App")
    recipe_text = StringProperty("There's no recipe")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def random_button_click(self):
        print("Button clicked")
        dish = Dataset().random()
        recipe = Recipe(dish[0], dish[1], dish[2])
        print("We have the dish...")
        print(self.recipe_text)

        text = recipe.show_recipe()
        self.recipe_text = text
        print("Text changed.")
        print(self.recipe_text)

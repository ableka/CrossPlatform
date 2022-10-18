import pandas as pd
import random


class Dataset:

    def __init__(self):
        self.dataset_name = 'RAW_recipes.csv'
        self.dataset = pd.read_csv(self.dataset_name)

    def get_recipe_data(self, id):
        print("Taking recipes name...")
        name = self.dataset.name[id]
        print("Name taken")
        print("Taking recipes minutes...")
        minutes = self.dataset.minutes[id]
        print("Minutes taken")
        print("Taking recipes steps...")
        steps = self.dataset.steps[id]
        print("Steps taken")
        return name, minutes, steps

    def search(self, search):
        pass

    def random(self):
        print("Getting random number...")
        recipe_id = random.randint(0, len(self.dataset))
        print("Random number gotten")
        print("Getting the recipe data...")
        random_dish_data = self.get_recipe_data(recipe_id)
        print("Data gotten")
        return random_dish_data

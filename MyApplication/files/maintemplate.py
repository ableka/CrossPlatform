import sqlite3
import random


class App:

    def __init__(self):
        self.__name = "Food picker"
        self.search = None
        self.randomly = None
        self.dbs = Database()

    def menu(self):
        print(f"Your {self.__name}")
        while self.search != "":
            print("-------Search-------")
            self.search = input("Type the name of dish here: ")
            self.dbs.search(self.search)
        while self.randomly != "":
             if self.randomly == "r":
                print("-------Random-------")
                self.randomly = input("Press 'r' for random dish: ")
                self.dbs.random()

    def create_app(self):
        self.menu()


class Recipe:

    def __init__(self, dish_name, ingredients, recipe):
        self.dish_name = dish_name
        self.ingredients = ingredients
        self.recipe = recipe


class Database:

    def __init__(self):
        self.db = 'mydb'
        self.connection = sqlite3.connect(self.db)

    def close_connection(self):
        self.connection.close()

    def get_cursor(self):
        return self.connection.cursor()

    def search(self, search):
        print(f"I am searching for a {search} match...")

    def random(self):
        print(random.choice(["eggs", "chicken", "buns"]))

if __name__ == "__main__":
    myapp = App()
    myapp.create_app()
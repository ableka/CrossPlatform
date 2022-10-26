from kivy.app import App
from kivy.lang import Builder
from MyApplication.view.RegistrationScreen import RegistrationScreen
from MyApplication.view.LoginScreen import LoginScreen
from MyApplication.view.WindowManager import WindowManager
from MyApplication.view.AppScreen import AppScreen
from MyApplication.view.AdminScreen import AdminScreen



class RecipesApp(App):
    def build(self):
        kv = Builder.load_file("Recipes.kv")
        return kv


if __name__ == "__main__":
    RecipesApp().run()

from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from MyApplication.model.database import DataBase

class AdminScreen(Screen):
    users = StringProperty("")

    def on_press_user_list(self):
        database = DataBase()
        self.users, self.passes = database.get_all_users()
        print(self.users, self.passes)
        self.manager.current = "user_list_screen"

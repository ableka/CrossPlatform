from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from MyApplication.model.database import DataBase


class UserListScreen(Screen):
    users = DataBase().get_all_users()
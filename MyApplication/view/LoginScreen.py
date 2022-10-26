from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import Screen

from MyApplication.model.database import DataBase


class LoginScreen(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    log_label = StringProperty("LogIn Here")
    database = DataBase()

    def on_release_log(self):
        username = self.username.text
        password = self.password.text
        realpass = self.database.log_in(username)
        print(username, password, realpass)
        if realpass:
            if password == realpass:
                self.log_label = "Successfully loged in"
                print("Successfully loged in")
                self.ids.button_login.disabled = False
            else:
                self.log_label = "Password is wrong"
                print("Password is wrong")
        else:
            self.log_label = "There's no such user in the system"

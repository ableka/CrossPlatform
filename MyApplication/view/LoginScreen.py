from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import Screen

from MyApplication.model.database import DataBase
from MyApplication.modelview.LoginFunctional import LoginFunctional


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
        login = LoginFunctional()
        login.login_func(username, password, realpass, self.manager)


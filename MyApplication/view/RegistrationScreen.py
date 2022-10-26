from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import Screen
from MyApplication.model.database import DataBase
from MyApplication.view.WindowManager import WindowManager
import time


class RegistrationScreen(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    rep_password = ObjectProperty(None)
    reg_label = StringProperty("Register")
    database = DataBase()

    def on_press_reg(self):
        username = self.username.text
        password = self.password.text
        rep_password = self.rep_password.text
        if username != '' and password != '' and rep_password != '':
            if password == rep_password:
                self.database.new_user(username, password)
                self.database.delete_duplicates()
                self.reg_label = "You've successfully registered"
                self.manager.current = "log_screen"
            else:
                self.reg_label = "Password doesn't match"
                print("Password doesn't match")
        else:
            self.reg_label = "You didn't fill all of the blanks"
        print(f"Button pressed. {username}, {password}, {rep_password}")

    def on_release_reg(self):
        print("Button released")
        self.reg_label = "Register"

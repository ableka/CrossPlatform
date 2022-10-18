import kivy
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.properties import ObjectProperty

class MyGrid(Widget):
    name = ObjectProperty(None)
    last_name = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)


    def on_button_click(self):
        name = self.name.text
        last_name = self.last_name.text
        email = self.email.text
        password = self.password.text

        print(name, last_name, email, password)

class RegistrationApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    RegistrationApp().run()

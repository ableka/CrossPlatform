from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}
        #add widgets to window
        #label widget
        self.greeting = Label(
                        text="Register here",
                        font_size=18,
                        color="#00FFCE"
                        )
        self.window.add_widget(self.greeting)
        #text input widget
        self.username = TextInput(
            hint_text = 'Username',
            multiline=False,
            padding_y = (20, 20),
            size_hint = (1, 0.5)
        )
        self.window.add_widget(self.username)
        # text input widget
        self.password = TextInput(
            hint_text = 'Password',
            multiline=False,
            padding_y=(20, 20),
            size_hint=(1, 0.5)
        )
        self.window.add_widget(self.password)
        # text input widget
        self.repeatpassword = TextInput(
            hint_text='Repeat Password',
            multiline=False,
            padding_y=(20, 20),
            size_hint=(1, 0.5)
        )
        self.window.add_widget(self.repeatpassword)
        #button widget
        self.button = Button(
            text="Confirm",
            size_hint = (1,0.5),
            bold = True,
            background_color = "#00FFCE"
        )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        if self.username.text:
            if len(self.password.text) >= 8:
                if self.password.text == self.repeatpassword.text:
                    self.greeting.text = f"You've successfully registered"
                    self.greeting.color = "#AFFF87"
                else:
                    self.greeting.text = f"Your passwords match wrong, please try again"
                    self.greeting.color = "#E74C3C"
            else:
                self.greeting.text = f'Your password is lower than 8 symbols, please try again'
                self.greeting.color = "#E74C3C"
        else:
            self.greeting.text = "Hey, you didn't type anything"
            self.greeting.color = "#E74C3C"



if __name__ == "__main__":
    SayHello().run()
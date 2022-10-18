from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class WidgetsExample(GridLayout):
    my_text = StringProperty("Hello!")
    count_enabled = False
    count = 0

    def on_button_click(self):
        if self.count_enabled:
            pass
        else:
            self.count += 1
            self.my_text = f"You clicked {self.count} times!"

    def on_toggle_button_state(self, widget):
        if widget.state == 'down':
            self.count_enabled = True
            widget.text = "Turn off"
            self.my_text = f"Button is inactive. "
        else:
            self.count_enabled = False
            widget.text = "Turn on"
            self.my_text = f'Button is active'


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "rl-bt"
        for i in range(100):
            size = dp(100)
            b = Button(text=str(i + 1), size_hint=(None, None), size=(size, size))
            self.add_widget(b)


# class GridLayoutExample(GridLayout):
#     pass

class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass


# def __init__(self, **kwargs):
#      super().__init__(**kwargs)
#      self.orientation = "vertical"
#      b1 = Button(text='A')
#      b2 = Button(text="B")
#      self.add_widget(b1)
#      self.add_widget(b2)

class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


TheLabApp().run()

import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

class MyOutfit(Screen):
    def __init__(self, screen_manager, **kwargs):
        super(MyOutfit, self).__init__(**kwargs)
        self.screen_manager = screen_manager

        # Create the first button with the text 'Click me'
        btn1 = Button(text='Click me 1', size_hint_y=None, height=50, size_hint_x=0.5, width=100)
        btn1.bind(on_press=self.on_button_press)

        # Create the second button with a specific width
        btn2 = Button(text='Click me 2', size_hint_y=None, height=50, size_hint_x=0.5, width=100)
        btn2.bind(on_press=self.on_button_press)
        btn2.pos_hint = {'right': 1, 'bottom': 0}

        self.add_widget(btn1)
        self.add_widget(btn2)

    def on_button_press(self, instance):
        instance.text = 'going to new screen'
        self.screen_manager.current = 'new_view'
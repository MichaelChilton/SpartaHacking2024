import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

class MyClosetView(Screen):
    def __init__(self, screen_manager, **kwargs):
        super(MyClosetView, self).__init__(**kwargs)
        self.screen_manager = screen_manager
        btn = Button(text='Click me')
        btn.bind(on_press=self.on_button_press)
        self.add_widget(btn)

    def on_button_press(self, instance):
        instance.text = 'going to new screen'
        self.screen_manager.current = 'new_view'

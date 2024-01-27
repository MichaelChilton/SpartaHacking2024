import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.camera import Camera
class cameraView(Screen):
    def __init__(self, **kwargs):
        super(cameraView, self).__init__(**kwargs)
        btn = Camera(play=True, index=0, resolution=(640,480))
        self.add_widget(btn)

    def on_button_press(self, instance):
        instance.text = 'You clicked me!'

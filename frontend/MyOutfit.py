import os
from kivy.uix.behaviors import DragBehavior
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image


class MyOutFit(Screen):
    def __init__(self, screen_manager, **kwargs):
        super(MyClosetView, self).__init__(**kwargs)
        self.screen_manager = screen_manager
        layout = BoxLayout(orientation="vertical")

        ## This section is focused on Imagine Intake
        image_folder = "C:/Users/michael.chilton/Downloads/KivyTest/KivyTest/images"  # hard-coded absolute path for testing purposes
        image_files = "C:/Users/michael.chilton/Downloads/KivyTest/KivyTest/images"  # hard-coded absolute path for testing purposes

        max_photos = 3
        for image_file in image_files[:max_photos]:
            img = Image(source=os.path.join(image_folder, image_file))
            layout.add_widget(img)

        # Create Image widgets for each image file and add them to the layout

        ## This section is focused on Imagine Intake

        btn = Button(text='Click me', size_hint_y=None, height=75)
        btn.bind(on_press=self.on_button_press)

        layout.add_widget(btn)
        self.add_widget(layout)

    def on_button_press(self, instance):
        layout = BoxLayout(orientation="vertical")
        instance.text = 'You clicked me!'

import os
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout


class MyClosetView(Screen):
    def __init__(self, screen_manager, **kwargs):
        super(MyClosetView, self).__init__(**kwargs)
        self.screen_manager = screen_manager
        
        dropdown = DropDown()
        # TODO: make this list load dynamically from somewhere better
        categories = ['Shirt', 'Pants', 'Shoes (raggety)']  # Replace with your own categories
        
        for category in categories:
            btn = Button(text=category, size_hint_y=None, height=44, width=Window.width)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
        
        main_button = Button(text='Select Category', size_hint=(None, None), pos_hint={'top': 1}, width=Window.width)
        main_button.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(main_button, 'text', x))
        
        dropdown.width = Window.width  # Set the width of the dropdown to the width of the screen
        
        self.add_widget(main_button)
        
        # Create a grid layout for the images
        grid_layout = GridLayout(cols=3, spacing=0)
        
        # TODO: Replace 'path_to_images' with logic to get from whatever objects have the images
        path_to_images = 'images/'
        
        # Load images dynamically from the given path
        for image_file in os.listdir(path_to_images):
            if image_file.endswith('.jpg'):
                image = Image(source=f'{path_to_images}/{image_file}')
                grid_layout.add_widget(image)

        self.add_widget(grid_layout)
    
    
    
    def on_button_press(self, instance):
        instance.text = 'going to new screen'
        self.screen_manager.current = 'new_view'
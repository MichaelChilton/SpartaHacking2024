import os
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.logger import Logger

class MyClosetView(Screen):
    def __init__(self, screen_manager, clothing_items, **kwargs):
        super(MyClosetView, self).__init__(**kwargs)
        self.screen_manager = screen_manager
        self.clothing_items = clothing_items
        # Create a ScrollView
        scroll_view = ScrollView()

        # Create a grid layout for the images
        grid_layout = GridLayout(cols=1, spacing=0, size_hint_y=None)
        # Make sure the height is such that there is something to scroll.
        grid_layout.bind(minimum_height=grid_layout.setter('height'))
        grid_layout.row_default_height = 100
        
        # Load images dynamically from the given clothing_items list
        for clothing_item in clothing_items:
            image_file = clothing_item.get_image_path()
            image = Image(source=image_file, size=(Window.width, Window.height), allow_stretch=True)
            grid_layout.add_widget(image)
            if screen_manager.previous() == 'MyOutfit':
                btn = Button(text='select', size_hint_y=None, height=44, width=Window.width)
                btn.bind(on_release=lambda btn: self.on_select(selected_clothing_item=clothing_item))
                grid_layout.add_widget(btn)
            

        # Set default height for rows
        grid_layout.row_force_default = True
        grid_layout.row_default_height = 640

        # Add the grid layout to the scroll view
        scroll_view.add_widget(grid_layout)
        # Add the scroll view to the main widget
        self.add_widget(scroll_view)
        # Create a horizontal BoxLayout for buttons at the bottom
        horizontal_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        # Create the first button with the text 'Click me'
        btn1 = Button(text='My Closet', size_hint_x=1, width=1)
        btn1.bind(on_press=self.on_Closet_UI)
        # Create the second button with the text 'Click me'
        btn2 = Button(text='Add Apparel', size_hint_x=1, width=1)
        btn2.bind(on_press=self.on_add_apparel_UI)

        # Create the third button with the text 'Click me'
        btn3 = Button(text='My Outfit', size_hint_x=1, width=1)
        btn3.bind(on_press=self.on_outfit_UI)

        # Add all three buttons to the horizontal layout
        horizontal_layout.add_widget(btn1)
        horizontal_layout.add_widget(btn2)
        horizontal_layout.add_widget(btn3)

        # Set the position of the horizontal layout to the bottom
        horizontal_layout.pos_hint = {'bottom': 1}

        # Add the horizontal layout to the screen
        self.add_widget(horizontal_layout)

    def on_button_press(self, instance):
        instance.text = 'going to new screen'
        self.screen_manager.current = 'new_view'

    def on_Closet_UI(self, instance):
        self.screen_manager.current = 'MyCloset'
    def on_outfit_UI(self, instance):
        self.screen_manager.current = 'MyOutfit'
    def on_add_apparel_UI(self, instance):
        self.screen_manager.current = 'AddApparelView'
        
    def on_select(self, instance, selected_clothing_item, **kwargs):
        self.screen_manager.selected_clothing_item = selected_clothing_item
        self.screen_manager.current = 'MyOutfit'
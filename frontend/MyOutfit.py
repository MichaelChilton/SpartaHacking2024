import kivy
from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior, TouchRippleBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle
from kivy.graphics import Ellipse, Color
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse



class MyOutfit(Screen):
    def __init__(self, screen_manager, **kwargs):
        super(MyOutfit, self).__init__(**kwargs)
        self.screen_manager = screen_manager
        with self.canvas.before:
            Color(0.2, 0.5, 0.8, 1)  # Set the background color (RGB format, in this case, light gray)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            # Bind size and pos properties to update the background when screen changes
            self.bind(size=self.update_background, pos=self.update_background)

        # Create a horizontal BoxLayout for buttons at the bottom
        horizontal_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

        # Create the first button with the text 'Click me'
        btn1 = Button(text='My Closet', size_hint_x=1, width=1)
        btn1.bind(on_press=self.on_Closet_UI)

        # Create the second button with the text 'Click me'
        btn2 = Button(text='MyApparel', size_hint_x=1, width=1)
        btn2.bind(on_press=self.on_Apparel_View)

        # Create the third button with the text 'Click me'
        btn3 = Button(text='MyOutfit', size_hint_x=1, width=1)
        btn3.bind(on_press=self.on_OutFit_UI)

        # Add all three buttons to the horizontal layout
        horizontal_layout.add_widget(btn1)
        horizontal_layout.add_widget(btn2)
        horizontal_layout.add_widget(btn3)

        # Set the position of the horizontal layout to the bottom
        horizontal_layout.pos_hint = {'bottom': 1}

        # Add the horizontal layout to the screen
        self.add_widget(horizontal_layout)

        # For Head of person
        Head = Button(text='Head', size_hint=(0.2, 0.2))  # Set size_hint directly
        Head.pos_hint = {'center_x': 0.5, 'center_y': .79}  # Center the button
        Head.bind(on_press=self.on_Closet_UI)
        self.add_widget(Head)

        # For Torso of person
        Torso = Button(text='Torso', size_hint_x=0.2, size_hint_y=0.2, width=1)
        Torso.pos_hint = {'center_x': 0.5, 'center_y': .56}
        Torso.bind(on_press=self.on_Closet_UI)
        self.add_widget(Torso)

        # For Legs of person
        Legs = Button(text='Legs', size_hint_x=0.2, size_hint_y=0.2, width=1)
        Legs.pos_hint = {'center_x': 0.5, 'center_y': .33}
        Legs.bind(on_press=self.on_Closet_UI)
        self.add_widget(Legs)

    # Buttons ------------------------------------------
    def on_Closet_UI(self, instance):

        self.screen_manager.current = 'MyCloset'

    def on_OutFit_UI(self, instance):
        instance.text = "This Is the Outfit UI"
        self.screen_manager.current = 'MyOutfit'

    def on_Apparel_View(self, instance):
        self.screen_manager.current = 'MyApparel'

    def on_button_press(self, instance):
        instance.text = "You shouldn't see this"
        self.screen_manager.current = 'MyOutfit'

    def on_outfit_UI(self, instance):
        self.screen_manager.current = 'MyOutfit'
    def on_add_apparel_UI(self, instance):
        self.screen_manager.current = 'AddApparelView'

    # Buttons ------------------------------------------

    # Background Color ---------------------
    def update_background(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos
    # Background Color ---------------------

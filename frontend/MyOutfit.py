import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

class MyOutfit(Screen):
    def __init__(self, screen_manager, **kwargs):
        super(MyOutfit, self).__init__(**kwargs)
        self.screen_manager = screen_manager

        # Create a horizontal BoxLayout for buttons at the bottom
        horizontal_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

        # Create the first button with the text 'Click me'
        btn1 = Button(text='Click me 1', size_hint_x=1, width=1)
        btn1.bind(on_press=self.on_button_press)

        # Create the second button with the text 'Click me'
        btn2 = Button(text='Click me 2', size_hint_x=1, width=1)
        btn2.bind(on_press=self.on_button_press)

        # Create the third button with the text 'Click me'
        btn3 = Button(text='Click me 3', size_hint_x=1, width=1)
        btn3.bind(on_press=self.on_button_press)

        # Add all three buttons to the horizontal layout
        horizontal_layout.add_widget(btn1)
        horizontal_layout.add_widget(btn2)
        horizontal_layout.add_widget(btn3)

        # Set the position of the horizontal layout to the bottom
        horizontal_layout.pos_hint = {'bottom': 1}

        # Add the horizontal layout to the screen
        self.add_widget(horizontal_layout)

        # For Head of person
        Head = Button(text='Head', size_hint_x=0.2,size_hint_y=0.2, width=1)
        Head.pos = (self.center_x + Head.width * 350, self.center_y + Head.height / 0.2)
        Head.bind(on_press=self.on_button_press)
        self.add_widget(Head)

        # For Torso of person
        Torso = Button(text='Torso', size_hint_x=0.2, size_hint_y=0.2, width=1)
        Torso.pos = (self.center_x + Torso.width * 350, self.center_y + Torso.height / 0.35)
        Torso.bind(on_press=self.on_button_press)
        self.add_widget(Torso)

        # For Legs of person
        Legs = Button(text='Legs', size_hint_x=0.2, size_hint_y=0.2, width=1)
        Legs.pos = (self.center_x + Legs.width * 350, self.center_y + Legs.height / 1.3)
        Legs.bind(on_press=self.on_button_press)
        self.add_widget(Legs) 

    def on_button_press(self, instance):
        instance.text = 'going to new screen'
        self.screen_manager.current = 'new_view'

    def on_button_press(self, instance):
        instance.text = 'going to new screen'
        self.screen_manager.current = 'sm'
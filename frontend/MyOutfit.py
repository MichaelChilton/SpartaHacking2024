import os
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import SlideTransition


class MyOutfitScreen(Screen):
    def __init__(self, **kwargs):
        super(MyOutfitScreen, self).__init__(**kwargs)
        self.name = "MyOutfit"

        # Example: Set spacing and padding for the GridLayout
        layout = GridLayout(cols=1, spacing=10, padding=(10, 10), row_force_default=True, row_default_height=100)

        self.label = Label(text="This is the second view")
        layout.add_widget(self.label)

        # Create a button that switches back to the main screen
        button = Button(text="My Outfit", valign='top')
        button.bind(on_release=lambda x: self.change_screen("main"))
        layout.add_widget(button)
        self.add_widget(layout)

    def change_screen(self, screen_name):
        # Set the transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = screen_name


class ImageRowApp(App):
    def build(self):
        # Create a screen manager
        sm = ScreenManager()
        self.manager = sm

        # Create a GridLayout
        layout = GridLayout(cols=1, spacing=10, padding=(10, 10), row_force_default=True, row_default_height=100)

        # Specify the folder containing images
        image_folder = "C:/Users/michael.chilton/Downloads/KivyTest/KivyTest/images"

        # Create a button that switches to the new screen
        button = Button(text="My Outfit", valign='top')
        button.bind(on_release=lambda x: self.change_screen(sm, "new_view"))
        layout.add_widget(button)

        # Get a list of all files in the specified folder
        image_files = [
            f
            for f in os.listdir(image_folder)
            if os.path.isfile(os.path.join(image_folder, f))
        ]

        # Create Image widgets for each image file and add them to the layout
        for image_file in image_files:
            img = Image(source=os.path.join(image_folder, image_file))
            layout.add_widget(img)



        # Create the main screen and add the layout to it
        main_screen = Screen(name="main")
        main_screen.add_widget(layout)
        sm.add_widget(main_screen)

        # Create a new view screen
        new_view_screen = MyOutfitScreen()
        sm.add_widget(new_view_screen)

        return sm

    def change_screen(self, screen_manager, screen_name):
        self.manager.transition = SlideTransition(direction='left')
        screen_manager.current = screen_name


if __name__ == "__main__":
    ImageRowApp().run()

import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import SlideTransition


class SecondView(Screen):
    def __init__(self, **kwargs):
        super(SecondView, self).__init__(**kwargs)
        # Set the name of the screen
        self.name = "new_view"

        # Create a vertical box layout for the second view
        layout = BoxLayout(orientation="vertical")

        # Create a label for the second view
        self.label = Label(text="This is the second view")
        layout.add_widget(self.label)

        # Create a button that switches back to the main screen
        button = Button(text="Go back")
        button.bind(on_release=lambda x: self.change_screen("main"))
        layout.add_widget(button)

        # Add the layout to the screen
        self.add_widget(layout)

    def change_screen(self, screen_name):
        # Set the transition animation to slide to the right
        self.manager.transition = SlideTransition(direction='right')
        # Switch to the specified screen
        self.manager.current = screen_name


class ImageRowApp(App):
    def build(self):
        # Create a screen manager to manage different screens
        sm = ScreenManager()
        # Assign the screen manager to the app for easy access
        self.manager = sm

        # Create a vertical box layout for the main screen
        layout = BoxLayout(orientation="vertical")

        # Specify the folder containing images
        image_folder = "C:/Users/michael.chilton/Downloads/KivyTest/KivyTest/images"  # hard-coded absolute path for testing purposes

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

        # Create a button that switches to the new view
        button = Button(text="Go to new view")
        button.bind(on_release=lambda x: self.change_screen(sm, "new_view"))
        layout.add_widget(button)

        # Create the main screen and add the layout to it
        main_screen = Screen(name="main")
        main_screen.add_widget(layout)
        sm.add_widget(main_screen)

        # Create a new view screen
        new_view_screen = SecondView()
        sm.add_widget(new_view_screen)

        # Return the screen manager as the root widget of the app
        return sm

    def change_screen(self, screen_manager, screen_name):
        # Set the transition animation to slide to the left
        self.manager.transition = SlideTransition(direction='left')
        # Switch to the specified screen
        screen_manager.current = screen_name


if __name__ == "__main__":
    # Run the Kivy application
    ImageRowApp().run()
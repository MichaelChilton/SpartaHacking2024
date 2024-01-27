import os
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

# Custom class for the close button
class CloseButton(BoxLayout):
    def __init__(self, **kwargs):
        super(CloseButton, self).__init__(orientation='horizontal', size_hint=(None, None), size=(100, 50),
                                          pos=(Window.width - 100, Window.height - 50), **kwargs)

        # Create a close button and add it to the layout
        close_button = Button(text='X', on_release=self.close_app, size_hint=(None, None), size=(50, 50))
        self.add_widget(close_button)

    def close_app(self, *args):
        # Close the application when the close button is pressed
        App.get_running_app().stop()

# Main screen of the application
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.name = "main"

        # Set background color
        self.background_color = (0.8, 0.8, 0.8, 1)

        # Create a GridLayout
        layout = GridLayout(cols=1, spacing=10, padding=(10, 10), row_force_default=True, row_default_height=50)

        # Specify the folder containing images
        image_folder = "C:/Users/michael.chilton/Downloads/KivyTest/KivyTest/images"

        # Create a button that switches to the new screen
        button = Button(text="My Outfit", valign='top', size_hint_y=None, height=50)
        button.bind(on_release=lambda x: self.change_screen("MyOutfitScreen"))
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

        self.add_widget(layout)

    # Method that changes the screen when the button is pressed
    def change_screen(self, screen_name):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = screen_name

# Screen that displays a label, buttons, and images
class MyOutfitScreen(Screen):
    def __init__(self, **kwargs):
        super(MyOutfitScreen, self).__init__(**kwargs)
        self.name = "MyOutfit"

        # Set background color
        self.background_color = (0.8, 0.8, 0.8, 1)

        # Example: Set spacing and padding for the GridLayout
        layout = GridLayout(cols=2, spacing=10, padding=(10, 10), row_force_default=True, row_default_height=50)

        self.label = Label(text="This is the second view")
        layout.add_widget(self.label)

        # Create a button that switches back to the main screen
        button = Button(text="My Outfit", valign='top', size_hint_y=None, height=50)
        button.bind(on_release=lambda x: self.change_screen("main"))
        layout.add_widget(button)

        # Create a close button
        close_button = CloseButton()
        layout.add_widget(close_button)

        self.add_widget(layout)

        # Specify the folder containing images
        self.image_folder = "C:/Users/michael.chilton/Downloads/KivyTest/KivyTest/images"
        self.image_files = [
            f
            for f in os.listdir(self.image_folder)
            if os.path.isfile(os.path.join(self.image_folder, f))
        ]

        # Display the first three images
        for i in range(3):
            self.display_next_image()

    # Method that changes the screen when the button is pressed
    def change_screen(self, screen_name):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = screen_name

    # Method that displays the next image
    def display_next_image(self):
        if self.image_files:
            image_file = self.image_files.pop(0)
            img = Image(source=os.path.join(self.image_folder, image_file))
            self.add_widget(img)

# Main application class
class MyApp(App):
    def build(self):
        # Create a screen manager
        sm = ScreenManager()

        # Create the main screen and add it to the screen manager
        main_screen = MainScreen()
        sm.add_widget(main_screen)

        # Create the MyOutfit screen and add it to the screen manager
        my_outfit_screen = MyOutfitScreen()
        sm.add_widget(my_outfit_screen)

        return sm

    # Method to handle the request to close the application
    def on_request_close(self, *args):
        # Prevent the application from immediately closing when the close button is pressed
        return False

if __name__ == "__main__":
    MyApp().run()

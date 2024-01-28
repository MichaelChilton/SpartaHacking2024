from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.camera import Camera
from rembg import remove
class camView(Screen):
    def __init__(self, screen_manager, **kwargs):
        super(camView, self).__init__(**kwargs)
        self.screen_manager = screen_manager
        self.layout = BoxLayout(orientation='vertical')

        # Create a camera object
        self.camera = Camera(play=True, resolution=(640, 480))
        self.layout.add_widget(self.camera)

        # Create a button to capture the image
        self.capture_button = Button(text='Capture', size_hint=(None, None), size=(100, 50))
        self.capture_button.bind(on_press=self.capture)
        self.layout.add_widget(self.capture_button)
        self.add_widget(self.layout)


    def capture(self, instance):
        # Capture the image from the camera
        self.camera.export_to_png('cool_guy_kivy.png')  # Save the image as 'cool_guy_kivy.png'

    def remove_background(self):
        input_path = '../cool_guy_kivy.png'
        output_path = 'output.png'
        with open(input_path, 'rb') as i:
            with open(output_path, 'wb') as o:
                input = i.read()
                output = remove(input)
                o.write(output)
        print("background removed")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.camera import Camera


class CameraApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # Create a camera object
        self.camera = Camera(play=True, resolution=(640, 480))
        self.layout.add_widget(self.camera)

        # Create a button to capture the image
        self.capture_button = Button(text='Capture', size_hint=(None, None), size=(100, 50))
        self.capture_button.bind(on_press=self.capture)
        self.layout.add_widget(self.capture_button)

        return self.layout

    def capture(self, instance):
        # Capture the image from the camera
        self.camera.export_to_png('cool_guy_kivy.png')  # Save the image as 'cool_guy_kivy.png'


if __name__ == '__main__':
    CameraApp().run()

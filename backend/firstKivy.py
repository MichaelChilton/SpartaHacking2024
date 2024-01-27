from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2

class CameraApp(App):
    def build(self):
        self.img1 = Image()
        layout = BoxLayout()
        layout.add_widget(self.img1)
        # Open the camera
        self.capture = cv2.VideoCapture(0)
        # Schedule the update of the camera image
        Clock.schedule_interval(self.update, 1.0/30.0)
        return layout

    def update(self, dt):
        # Read frame from the camera
        ret, frame = self.capture.read()
        if ret:
            # Convert it to texture
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tostring()
            texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            # Display image from the texture
            self.img1.texture = texture1

    def on_stop(self):
        # Release the camera
        self.capture.release()

if __name__ == '__main__':
    CameraApp().run()

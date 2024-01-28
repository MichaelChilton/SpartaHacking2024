# DragPicture.py

from kivy.uix.image import Image
from kivy.uix.behaviors import DragBehavior
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
import os

# Get the current directory of the script

kv = f'''
<MyLayout>:
    DragLabel:
        size_hint: 0.25, 0.2
        source: "C:/Users/michael.chilton/Downloads/KivyTest/KivyTest/images/image.jpg"
        z: 1
'''

class DragLabel(DragBehavior, Image):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            return super(DragLabel, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            self.x = touch.x - self.width / 2
            self.y = touch.y - self.height / 2

# class MyLayout(FloatLayout):
#     pass

# class DragPictureApp(App):
#     def build(self):
#         return MyLayout()
    
class DragPictureWidget(FloatLayout):
    name : str
    def __init__(self, screen_manager, **kwargs):
        super(DragPictureWidget, self).__init__(**kwargs)
        self.screen_manager = screen_manager
        self.add_widget(FloatLayout())

# if __name__ == '__main__':
#     try:
#         DragPictureApp().run()
#     except Exception as e:
#         print(f"An error occurred: {e}")

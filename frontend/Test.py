from kivy.uix.image import Image
from kivy.app import App
from kivy.uix.behaviors import DragBehavior
from kivy.lang import Builder

kv = '''
<DragLabel>:
    drag_rectangle: self.x, self.y, self.width, self.height
    drag_timeout: 10000000
    drag_distance: 0

FloatLayout:
    DragLabel:
        size_hint: 0.25, 0.2
        source: "C:/Users/michael.chilton/Downloads/KivyTest/KivyTest/images/image1.jpg"
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

class TestApp(App):
    def build(self):
        layout = Builder.load_string(kv)
        return layout

TestApp().run()

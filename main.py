from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from frontend.AddApparelView import AddApparelView
from frontend.MyClosetView import MyClosetView
from frontend.MyOutfit import MyOutfit
from backend.ClothingItem import ClothingItem
import os
from kivy.logger import Logger


# to add new screen, import it here like the MyClosetView above


class MainApp(App):
    def build(self):
        sm = ScreenManager()
        Window.fullscreen = 'auto'
        
        images_folder = 'images'
        images = [os.path.join(images_folder, filename) for filename in os.listdir(images_folder) if filename.endswith('.jpg') or filename.endswith('.png')]

        my_clothing_items = []
        for image in images:
            category = image.split('/')[-1]
            clothing_item = ClothingItem(image, category, image)
            my_clothing_items.append(clothing_item)
            Logger.info(clothing_item.get_name())

        sm.add_widget(MyOutfit(screen_manager=sm, name='MyOutfit'))
        sm.add_widget(MyClosetView(screen_manager=sm, clothing_items=my_clothing_items, name='MyCloset'))
        sm.add_widget(AddApparelView(screen_manager=sm, name='MyApparel'))
        # to add new screen, add it here like the MyClosetView above
        return sm


if __name__ == '__main__':
    MainApp().run()
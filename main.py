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
    selected_clothing_item = None
    def build(self):
        sm = ScreenManager()
        Window.fullscreen = 'auto'
        
        if os.path.exists('images/selfie.png'):
            os.remove('images/selfie.png')
        

        my_clothing_items = []
        images_folder = 'images'
        sub_folders = os.listdir(images_folder)

        for sub_folder in sub_folders:
            apparel = os.listdir(images_folder + '/'+ sub_folder)
            for clothe in apparel:
                image_path = images_folder + '/' + sub_folder + '/' + clothe
                image_name = clothe.split('.')[0]
                category = sub_folder
                clothing_item = ClothingItem(image_name, image_path, category)
                my_clothing_items.append(clothing_item)
                    
        for item in my_clothing_items:
            print(item)

        sm.add_widget(MyOutfit(screen_manager=sm, name='MyOutfit'))
        sm.add_widget(MyClosetView(screen_manager=sm, clothing_items=my_clothing_items, name='MyCloset'))
        sm.add_widget(AddApparelView(screen_manager=sm, name='AddApparelView'))
        # to add new screen, add it here like the MyClosetView above
        return sm

    def get_selected_clothing_item(self):
        return selected_clothing_item
    def set_selected_clothing_item(self):
        return selected_clothing_item

if __name__ == '__main__':
    MainApp().run()
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from frontend.MyClosetView import MyClosetView
# to add new screen, import it here like the MyClosetView above
from frontend.MyOutfit import MyOutFit
from frontend.DragPicture import DragPictureWidget



class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(DragPictureWidget(screen_manager=sm, name='drag_picture'))
        sm.add_widget(MyOutFit(screen_manager=sm, name='my_closet'))
        # to add new screen, add it here like the MyClosetView above
        # sm.add_widget(DragLabel())
        return sm

if __name__ == '__main__':
    MainApp().run()
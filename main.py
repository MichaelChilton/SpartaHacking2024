from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from frontend.MyClosetView import MyClosetView
from backend.cameraView import cameraView
# to add new screen, import it here like the MyClosetView above
from frontend.MyOutfit import SecondView


class MainApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(cameraView(name='cameraView'))
        
        # to add new screen, add it here like the MyClosetView above
        return sm

if __name__ == '__main__':
    MainApp().run()
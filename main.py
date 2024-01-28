from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from frontend.MyClosetView import MyClosetView
from frontend.MyOutfit import MyOutfit
from frontend.AddApparelView import AddApparelView


# to add new screen, import it here like the MyClosetView above


class MainApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(MyOutfit(screen_manager=sm, name='MyOutfit'))
        sm.add_widget(MyClosetView(screen_manager=sm, name='MyCloset'))
        sm.add_widget(AddApparelView(screen_manager=sm, name='AddApparel'))
        # to add new screen, add it here like the MyClosetView above
        return sm

if __name__ == '__main__':
    MainApp().run()
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
Window.size = (400, 600)

 
class HomePage(Screen):
    pass
 
class LoginPage(Screen):
    pass
 
class MyApp(MDApp):
    def build(self):
        screen = Builder.load_file('My.kv')
        screen_manager = ScreenManager()
        screen_manager.add_widget(HomePage(name='homepage'))
        screen_manager.add_widget(LoginPage(name='loginpage'))
        return screen_manager
 
if __name__ == '__main__':
    MyApp().run()
 

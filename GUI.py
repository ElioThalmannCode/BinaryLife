import kivy                                 
from kivy.app import App                    
from kivy.uix.label import Label            
from kivy.uix.gridlayout import GridLayout  
from kivy.uix.textinput import TextInput    
from kivy.uix.button import Button          
from kivy.uix.widget import Widget          
from kivy.properties import ObjectProperty  
from pydblite import *                      
from kivy.factory import Factory            
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_string("""
<MenuScreen>:

    BoxLayout:
        orientation: 'vertical'
        Image:
            source: 'mylogo.png'
            size: self.texture_size
        Button:
            text: 'Start'
            on_press: root.manager.current = 'start'


<StartScreen>:
    BoxLayout:
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
""")

# Declare both screens
class MenuScreen(Screen):
    pass

class StartScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(StartScreen(name='start'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()

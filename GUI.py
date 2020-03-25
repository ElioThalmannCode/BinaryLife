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
import functions
Builder.load_string("""
<MenuScreen>:

    BoxLayout:
        orientation: 'vertical'
        Image:
            source: 'mylogo.png'
            size: self.texture_size
        Button:
            text: 'Start'
            on_press: 
                root.init_life()
                root.manager.current = 'start'


<StartScreen>:
    text_field: text_field
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            orientation: 'horizontal'
            Label:
                id: text_field
                text: "hallo"
        BoxLayout:
            size: root.width, 100
            size_hint: None, None
            orientation: 'horizontal'
            Button:
                text: 'next year'
                on_press: 
                    root.do_action()
""")    
# Declare both screens
class MenuScreen(Screen):
    def init_life(self):
        pass

class StartScreen(Screen):
    def do_action(self):
        self.text_field.text = functions.start()

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(StartScreen(name='start'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()

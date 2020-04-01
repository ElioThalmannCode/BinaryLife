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
from kivy.clock import Clock

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
                text: root.text
        BoxLayout:
            size: root.width, 100
            size_hint: None, None
            orientation: 'horizontal'
            Button:
                text: 'next year'
                on_press: 
                    root.manager.current = 'event'
                    root.add_year()



<EventScreen>:
    button: button
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            orientation: 'horizontal'
            Label:
                text: root.event_text
        BoxLayout:
            size: root.width, 100
            size_hint: None, None
            orientation: 'horizontal'
            Button:
                text: "Event beenden"
                id: button
                on_press: 
                    root.manager.current = 'start'
                    
""")    

# Declare screens
class MenuScreen(Screen):
    def init_life(self):
        pass

class StartScreen(Screen):
    text = functions.start()
    def add_year(self):
        functions.year = functions.year + 1
        print(functions.year)
    def update(self, dt, arg_1, arg_2):
        self.name = arg_1
        sleep(5)
        self.name = arg_2
class EventScreen(Screen):
    event_text = str(functions.year)


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(StartScreen(name='start'))
sm.add_widget(EventScreen(name='event'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()

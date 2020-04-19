import kivy
from time import sleep

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty 
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
                text: root.text
        BoxLayout:
            size: root.width, 100
            size_hint: None, None
            orientation: 'horizontal'
            Button:
                text: 'next year'
                on_press: 
                    root.manager.current = 'event'



<EventScreen>:
    button: button
    text_event: text_event
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            orientation: 'horizontal'
            Label:
                text: "Klick"
                id: text_event
        BoxLayout:
            size: root.width, 100
            size_hint: None, None
            orientation: 'horizontal'
            Button:
                text: "Event anzeigen"
                id: button
                on_press: 
                    root.set_text()
            BoxLayout:
                orientation: 'vertical'
                Button: 
                    text: "ja"
                    on_press:
                        root.yes()
                Button: 
                    text: "nein"
                    on_press:
                        root.no()

#            Button:
#                text: "Event beenden"
#                id: button
#                on_press: 
#                    root.manager.current = 'start'
                    
""")

# Declare screens
class MenuScreen(Screen):
    def init_life(self):
        pass

class StartScreen(Screen):
    text = functions.start()
class EventScreen(Screen):
    def set_text(self):
        global event,yes,no
        event,yes,no = functions.next_year()
        self.text_event.text = event
    def yes(self):
        self.text_event.text = yes[0]
        self.remove_widget(self.btn)

    def no(self):
        self.text_event.text = no[0]




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

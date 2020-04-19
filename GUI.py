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
            Label:
                text: "Jahre Alt"
            Button:
                text: 'nächstes Jahr'
                on_press: 
                    root.manager.current = 'event'
            Button:
                text: 'Aktualisieren'
                on_press: 
                    root.update()




<EventScreen>:
    button: button
    yes_btn: yes_btn
    no_btn: no_btn
    text_event: text_event
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            orientation: 'horizontal'
            Label:
                text: "Klick auf Event anzeigen!!"
                id: text_event
        BoxLayout:
            size: root.width, 100
            size_hint: None, None
            orientation: 'horizontal'
            Button:
                text: "Event anzeigen"
                id: button
                on_release: 
                    root.set_text()
            BoxLayout:
                orientation: 'vertical'
                Button: 
                    text: "ja"
                    id: yes_btn
                    on_press:
                        root.yes()
                Button: 
                    text: "nein"
                    id: no_btn
                    on_release:
                        root.no()
                    
""")

# Declare screens
class MenuScreen(Screen):
    pass

class StartScreen(Screen):
    text = functions.start()
    def update(self):
        self.text_field.text = functions.update()
class EventScreen(Screen):
    def set_text(self):
        global event,yes,no
        event,yes,no = functions.next_year()
        self.text_event.text = event
    def change(self):
        self.remove_widget(self.btn)
        sm.current = "start"
    def yes(self):
        self.btn = Button(text=(f"{yes[0]}\n Klicke zum fortfahren"), on_press=lambda x:self.change())
        self.add_widget(self.btn)
        functions.year += 1
    def no(self):
        self.btn = Button(text=(f"{no[0]}\n Klicke zum fortfahren"), on_press=lambda x:self.change())
        self.add_widget(self.btn)
        functions.year += 1




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

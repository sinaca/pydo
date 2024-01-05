from kivy.app import App 
from kivy.uix.boxlayout import Boxlayout 
from kivy.uix.label import Label 
from player import vibrator 
from kivy.core.video import Video 
from kivy.uix.widget import widget
from kivy.uix.button import Button 
class start(Widget): 
    def __init__(self):
        super(start, self). __init__(**kwgs)
           

 
        
class TestApp(App):
    def build(self):
        return Button(text='Hello world')
TestApp().run()

from kivy.app import App 
from kivy.uix.boxlayout import Boxlayout 
from kivy.uix.label import Label 
from plyer import vibrator 
from kivy.core.video import Video 
from kivy.uix.widget import Widget
from kivy.uix.button import Button 
class start(Widget): 
    pass
           

 
        
class royaleApp(App):
    def build(self):
        return start() 
royaleApp().run()

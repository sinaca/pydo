from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.label import Label 
from plyer import vibrator 
from kivy.core.video import Video 
from kivy.uix.widget import Widget
from kivy.uix.button import Button 
class Start(Widget): 
    pass
           

 class Finish(Widget):
     pass 
        
class RoyaleApp(App):
    def build(self):
        return start() 
RoyaleApp().run()

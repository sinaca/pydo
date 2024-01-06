from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.label import Label 
from plyer import vibrator 
from kivy.core.video import Video 
from kivy.uix.widget import Widget
from kivy.uix.button import Button 
class Start(Widget): 
    def check() :
        pass 
    def register () :
        pass 
    def login() :
        pass 
    def logout() :
        pass 
    def vibrat() :
        vibrator(10) 
           

 class Finish(Widget):
     pass 
        
class RoyaleApp(App):
    def build(self):
        return start() 
RoyaleApp().run()

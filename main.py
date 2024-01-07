from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.label import Label 
from plyer import vibration
from kivy.core.video import Video 
from kivy.uix.widget import Widget
from kivy.uix.button import Button 
class Start(Widget): 
    def insert() :
        pass 
    def delet() :
        pass

    def check() :
        pass 
    def register () :
        pass 
    def login() :
        pass 
    #function to logout
    def logout() :
        pass 
    def vibrat() :
        # vibrate for ten secs
        vibration.vibrate(1000) 
    #function to collect information
    def col_info() :
        pass 
     # weight evaluatar   
    def weigher() :
        return 1
    # widget controller
    def wig_manager():
        return 
    # calculate energy
    def energ_v() :
        return 
    # innovation
    def inover() :
        return 




 class Finish(Widget):
     pass 
        
class RoyaleApp(App):
    def build(self):
        return start() 
RoyaleApp().run()

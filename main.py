from kivy.app import App 
from kivy.uix.video import Video

from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.label import Label 
from plyer import vibration
from kivy.core.audio import SoundLoader
from kivy.uix.widget import Widget
from kivy.uix.button import Button 
class Start(Widget):
    def aud_player(self) :
        sound = SoundLoader.load('your_audio_file.mp3')  # Replace with your audio file path

        layout = BoxLayout(orientation='vertical')
        
        play_button = Button(text='Play', on_press=self.play_audio)
        stop_button = Button(text='Stop', on_press=self.stop_audio)
        
        layout.add_widget(play_button)
        layout.add_widget(stop_button) 
    # stop audio
    def stop_audio(self, instance):
        if self.sound:
            self.sound.stop()
     # start audio      
    def play_audio(self, instance):
        if self.sound:
            self.sound.play()
    
    def insert(self) :
        pass 
    # delete user
    def delet(self) :
        pass
    # check status
    def check(self) :
        pass 
    # register

    def register (self) :
        pass 
    # login
    def login(self) :
        pass 
    #function to logout
    def logout(self) :
        pass 
    def vibrat(self) :
        # vibrate for ten secs
        vibration.vibrate(1000) 
    #function to collect information
    def col_info(self) :
        pass 
     # weight evaluatar   
    def weigher(self) :
        return 1
    # widget controller
    def wig_manager(self):
        return 
    # calculate energy
    def energ_v(self) :
        return 
    # innovation
    def inover(self) :
        return 


    def v_player(self) :
        video = Video(source='your_video.mp4', state='play', options={'allow_stretch': True})

 class Finish(Widget):
     pass 
        
class RoyaleApp(App):
    def build(self):
        return start() 
RoyaleApp().run()
    


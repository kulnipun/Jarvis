from playsound import playsound
import eel 

# playing assistant sound function

@eel.expose
def playassistantsound():
    music_dir = "D:\\Jarvis\\www\\assests\\audio\\start_sound.mp3"
    playsound(music_dir)
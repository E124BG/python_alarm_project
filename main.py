from playsound import playsound # this library is used to play mp3 files in python
import time

def alarm(seconds):
    time_elapsed = 0
    
    while time_elapsed < seconds :
        time.sleep(1)# pauses the code for 1 sec
        time_elapsed += 1
        
        #compute remaining minutes and seconds
        
        remaining_time = seconds - time_elapsed
        remaining_minutes = remaining_time//60
        remaining_seconds = remaining_time%60
        print("{}, {}".format(remaining_minutes, remaining_seconds))
        
    playsound("alarm-flute.mp3")

        
alarm(110)
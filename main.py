from playsound import playsound # this library is used to play mp3 files in python
import time

def alarm(seconds):
    time_elapsed = 0
    
    while time_elapsed < seconds :
        time.sleep(1)# pauses the code for 1 sec
        time_elapsed += 1
        
        #compute remaining minutes and seconds
        
        remaining_time = seconds - time_elapsed
        remaining_minutes = remaining_time//60 # integer division
        remaining_seconds = remaining_time%60 # remainder of euclidean division
        print("{:02d}: {:02d}".format(remaining_minutes, remaining_seconds)) # :02d pads the var to be length 2 digits with 0's
        
    playsound("alarm-flute.mp3")

        
alarm(5)
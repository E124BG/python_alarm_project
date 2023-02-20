from playsound import playsound # this library is used to play mp3 files in python
import time

# ANSI escape codes, used to move the cursor, change color of text or underline in console
CLEAR = "\033[2J" # clears the terminal
CLEAR_AND_RETURN = "\033[H" #clears the terminal and goes back left to original position

def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)
    
    while time_elapsed < seconds :
        time.sleep(1)# pauses the code for 1 sec
        time_elapsed += 1
        
        #compute remaining minutes and seconds
        
        remaining_time = seconds - time_elapsed
        remaining_minutes = remaining_time//60 # integer division
        remaining_seconds = remaining_time%60 # remainder of euclidean division
        print(CLEAR_AND_RETURN)
        print("{:02d}: {:02d}".format(remaining_minutes, remaining_seconds)) # :02d pads the var to be length 2 digits with 0's
        
    playsound("alarm-flute.mp3")

#ask for user input here
minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)
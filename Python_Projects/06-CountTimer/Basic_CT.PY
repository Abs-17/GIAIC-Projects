
# ''''''''''''''''''''''''''''''''''''''' Count Down Timer '''''''''''''''''''''''''''''''''''''

#importing library
import time

def countdowntimer(seconds):
    while seconds:
        mins,secs = divmod(seconds,60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer,end = '\r') #to print on the same line
        time.sleep(1)
        seconds -= 1

    print("Time`s up!!")

#Inputation for the countdown
time_input = int(input("Enter time in seconds : "))

#Calling the function
countdowntimer(time_input)

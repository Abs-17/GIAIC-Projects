
#''''''''''''''''''''''''''''''' Countdown Timer With GUI '''''''''''''''''''''''''''''''''

#importing libraries

import tkinter as tk
import time

def cd(time_left):
    mins , secs = divmod(time_left,60)
    timer = '{:02d}:{:02d}'.format(mins,secs)
    label.config(text=timer)

    if time_left > 0:
        root.after(1000,cd,time_left - 1)
    else:
        label.config(text = "Time`s up !!")

def start_timer():
    time_input = int(entry.get())
    cd(time_input)

#creating the main window

root = tk.Tk()
root.title("Countdown Timer ")

#create a label to display the timer

label = tk.Label(root,font =("Arial",40))
label.pack()

#Create an empty widget for the user to enter time
entry = tk.Entry(root,font = ('Arial',20))
entry.pack()

#create a button to start the countdown

start_button = tk.Button(root, text = 'Start Timer', command = start_timer)
start_button.pack()

#Start GUI LOOP
root.mainloop()
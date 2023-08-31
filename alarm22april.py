#import required library

import tkinter 
import pyttsx3 as pt
from tkinter import *
import time
import datetime
from threading import *
import math
from plyer import notification
import random



engine = pt.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',180)
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)
#print(voices)

#speak function
def speak(audio):
    engine.say(audio) # for audio that the alarm will say
    engine.runAndWait() # for a pause before speaking the next sentences 


# Create Object
root = tkinter.Tk()

# title 
root.title("Vocabalarm")

# Set geometry
root.geometry("400x600")
root.maxsize(400,600)
root.minsize(400,600)

 
# Use Threading
def Threading():
    t1=Thread(target=alarm)
    t1.start()

Label(root,text="Current Time",font=("Helvetica 20 bold"),fg="red").pack()    


#list
words = ['conjecture : guess', 'amiable : friendly', 'cozen : trick', 'fastidious: excessive demanding', 'zany : comical', 'broigus : angry',
         'naive : artless', 'ethical : honourable', 'frigid : cool', 'raze : destroy', 'sob : weep', 'savory : delicious', 'dauntless : brave', 'abominable : terrible', 'inequity : difference' ]
c = random.choice(words)


def notify():
    
    notification.notify(app_name ="VocabAlarm",title = "Word of the alarm is",message = c,timeout=10,)   
 
    
def update_clock():
    hour = int(time.strftime("%I"))
    minute = int(time.strftime("%M"))
    second = int(time.strftime("%S"))

    seconds_x = seconds_hand_len *  math.sin(math.radians(second  * 6 )) + center_x
    seconds_y = -1 * seconds_hand_len * math.cos(math.radians(second * 6)) + center_y
    canvas.coords(seconds_hand, center_x ,center_y , seconds_x , seconds_y)

    minutes_x = minutes_hand_len *  math.sin(math.radians(minute  * 6 )) + center_x
    minutes_y = -1 * minutes_hand_len * math.cos(math.radians(minute * 6)) + center_y
    canvas.coords(minutes_hand, center_x ,center_y , minutes_x , minutes_y)

    hours_x = hours_hand_len *  math.sin(math.radians(hour  * 30 )) + center_x
    hours_y = -1 * hours_hand_len * math.cos(math.radians(hour * 30)) + center_y
    canvas.coords(hours_hand, center_x ,center_y , hours_x , hours_y)

    root.after(1000, update_clock)

#def working():
   # h = datetime.now().time().hour 
   # m = datetime.now().time().minute 
    #s = datetime.now().time().second 
    #print(h,m,s)
    #hr = (h/12)*360
    #min_ = (m/60)*360
    #sec_ = (s/60)*360

canvas = tkinter.Canvas(root,width=200,height=200,bg="black")
canvas.pack(expand=True, fill='both')

#clock image
img = PhotoImage(file="image.png")       
canvas.create_image(200,200,image=img)

#create clock hands
center_x = 200
center_y = 200
seconds_hand_len = 50
minutes_hand_len = 45
hours_hand_len = 20

seconds_hand = canvas.create_line(200, 200, 200 +seconds_hand_len, 200 + seconds_hand_len, width=1.5,fill='red')

minutes_hand = canvas.create_line(200, 200, 200 +minutes_hand_len, 200 + minutes_hand_len, width=2,fill='white')

hours_hand = canvas.create_line(200, 200, 200 +hours_hand_len, 200 + hours_hand_len, width=4,fill='white')

def alarm():
    
    # Infinite Loop
    while True:
        # Set Alarm
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        
 
        # Wait for one seconds
        time.sleep(1)
 
        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,set_alarm_time)
 
        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            notify()
            print("alarm is running")
            # Playing sound
            speak("this is an alarm" )
            speak( "and the New word of this alarm is")
            speak(c)
            

# Add Labels, Frame, Button, Optionmenus
#Label(root,text="Alarm Clock",font=("Helvetica 20 bold"),fg="red").pack(pady=10)
Label(root,text="Set Time",font=("Helvetica 17 bold"),fg="red").pack()



frame = Frame(root)
frame.pack()
 
hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
        )
hour.set(hours[0])
 
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)
 
minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])
 
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)
 
second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second.set(seconds[0])
 
secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)
 
Button(root,text="Set Alarm",font=("Helvetica 18"),command=Threading).pack(pady=20)
#Label(root,text="New Word for this alarm is:",font=("Helvetica 12")).pack()

update_clock()

# Execute Tkinter
root.mainloop()

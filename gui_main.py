import tkinter as tk
from tkinter import *

import time, signal, sys
import gpiozero
import board
import busio
import math
i2c = busio.I2C(board.SCL, board.SDA)

import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

ads = ADS.ADS1115(i2c)

    #set up analog pins
a0 = AnalogIn(ads, ADS.P0)
"""
a1 = AnalogIn(ads, ADS.P1)
a2 = AnalogIn(ads, ADS.P2)
"""
#set up
relay_limit1 = 75
relay_limit2 = 75
relay_limit3 = 75

#set up relay and pump pins
relay1_pin = 26
relay2_pin = 19
relay3_pin = 13
pump_pin = 20

#set up gpio relay outputs
relay1 = gpiozero.OutputDevice(relay1_pin, active_high=True, initial_value=False)
relay2 = gpiozero.OutputDevice(relay2_pin, active_high=True, initial_value=False)
relay3 = gpiozero.OutputDevice(relay3_pin, active_high=True, initial_value=False)
pump = gpiozero.OutputDevice(pump_pin, active_high=True, initial_value=False)

    #others
fullscreen = False
lock = False
#create window and configure it
root = tk.Tk()
root.title("Temp Controller rev1")
root.geometry('480x320')
root.rowconfigure([1,2,3,4], minsize=50, weight=1)
root.columnconfigure([0, 1, 2, 3, 4], minsize=50, weight=1)

#function
def generic_label(txt, col, row_):
    labelSet = tk.Label(root, text=txt, font=("bold", 15),  wraplength= 90)
    labelSet.grid(row=row_, column=col)
    #increase and decrease temp set values per relay/thermistor
def increase_r1():
    global relay_limit1
    relay_limit1 += 1
    setTemp1.config(text=relay_limit1)
    
def decrease_r1():
    global relay_limit1 
    relay_limit1 -= 1
    setTemp1.config(text=relay_limit1)

def increase_r2():
    global relay_limit2
    relay_limit2 += 1
    setTemp2.config(text=relay_limit2)
    
def decrease_r2():
    global relay_limit2 
    relay_limit2 -= 1
    setTemp2.config(text=relay_limit2)

def increase_r3():
    global relay_limit3
    relay_limit3 += 1
    setTemp3.config(text=relay_limit3)
    
def decrease_r3():
    global relay_limit3 
    relay_limit3 -= 1
    setTemp3.config(text=relay_limit3)
    #updates whether the indicator lights are green or red based on set vs actual temp (this will probably also update relay on off state, TBD)
def update_light():
    global relay1, relay2, relay3
    update_temp()
    if relay_limit1 >= temp1:
        light1.itemconfig(indicatorLight1, fill='green')
        relay1.on()
    elif relay_limit1 < temp1:
        light1.itemconfig(indicatorLight1, fill='red')
        relay1.off()
    if relay_limit2 >= temp2:
        light2.itemconfig(indicatorLight2, fill='green')
        relay2.on()
    elif relay_limit2 < temp2:
        light2.itemconfig(indicatorLight2, fill='red')
        relay2.off()
    if relay_limit3 >= temp3:
        light3.itemconfig(indicatorLight3, fill='green')
        relay3.on()
    elif relay_limit3 < temp3:
        light3.itemconfig(indicatorLight3, fill='red')
        relay3.off()
    pumpAct()
    root.after(1000, update_light)

def pumpAct():
    global pump
    r1 = relay1.value
    r2 = relay2.value
    r3 = relay3.value
    p = pump.value
    if (r1 == False) or (r2 == False) or (r3 == False):
        pump.off()
        #print(r1, r2, r3, p)
    if (r1 == True) and (r2 == True) and (r3 == True):
        pump.on()
        #print(r1, r2, r3, p)


def fullscreen_toggle():
    global fullscreen
    if fullscreen == False:
        root.attributes("-fullscreen", True)
        toggleFS.config(relief=RAISED)
        fullscreen = True
    else:
        root.attributes("-fullscreen", False)
        toggleFS.config(relief=SUNKEN)
        fullscreen = False

def lock_temp():
    global lock
    if lock == False:
        but_dec1.config(state = DISABLED, relief=SUNKEN)
        but_dec2.config(state = DISABLED, relief=SUNKEN)
        but_dec3.config(state = DISABLED, relief=SUNKEN)
        but_inc1.config(state= DISABLED, relief=SUNKEN)
        but_inc2.config(state= DISABLED, relief=SUNKEN)
        but_inc3.config(state= DISABLED, relief=SUNKEN)
        setTemp1.config(relief=FLAT)
        setTemp2.config(relief=FLAT)
        setTemp3.config(relief=FLAT)
        lockTemp.config(relief=SUNKEN)
        lockTemp.config(text="UNLOCK TEMP")
        lock = True
    else:
        but_dec1.config(state = NORMAL, relief=RAISED)
        but_dec2.config(state = NORMAL, relief=RAISED)
        but_dec3.config(state = NORMAL, relief=RAISED)
        but_inc1.config(state= NORMAL, relief=RAISED)
        but_inc2.config(state= NORMAL, relief=RAISED)
        but_inc3.config(state= NORMAL, relief=RAISED)
        setTemp1.config(relief=RIDGE)
        setTemp2.config(relief=RIDGE)
        setTemp3.config(relief=RIDGE)
        lockTemp.config(relief=RAISED)
        lockTemp.config(text=" LOCK  TEMP")
        lock = False


def converter(ads_val, Ro=4000.0, To=25.0, beta=3435.0): #Ro is not accurate
    r = 10000.0 / (65535.0 /ads_val-1.0)
    #stienhart temp equation
    sth = r/Ro
    sth = math.log(sth)
    sth /= beta
    sth += 1.0/(To + 273.15)
    sth = (1.0 / sth)
    sth-= 273.15
    sth = (sth * (9/5)) + 32
    
    return int(sth)
def update_temp():
    global temp1, temp2, temp3
    temp1 = converter(a0.value)
    """
    temp2 = converter(a1.value)
    temp3 = converter(a2.value)
    """
    currTemp1.config(text=f"{temp1}\N{DEGREE FAHRENHEIT}")
    #currTemp2.config(text=f"{temp2}\N{DEGREE FAHRENHEIT}")
    #currTemp3.config(text=f"{temp3}\N{DEGREE FAHRENHEIT}")
#set up analog values
temp1 = converter(a0.value)
"""
temp2 = converter(a1.value)
temp3 = converter(a2.value)
"""
    #DELETE ME ONCE YOU HAVE ALL THERMISTORS
temp2 = 60
temp3 = 75
#set up gui items
    #initial label config
setTemp1 = tk.Label(root, text=relay_limit1, relief=RIDGE)
setTemp2 = tk.Label(root, text=relay_limit2, relief=RIDGE)
setTemp3 = tk.Label(root, text=relay_limit3, relief=RIDGE)
currTemp1 = tk.Label(root, text=f"{temp1}\N{DEGREE FAHRENHEIT}")
currTemp2 = tk.Label(root, text=f"{temp2}\N{DEGREE FAHRENHEIT}")
currTemp3 = tk.Label(root, text=f"{temp3}\N{DEGREE FAHRENHEIT}")
    #initial button config
but_dec1 = tk.Button(root, text="-", command=decrease_r1, font=("bold", 15))
but_inc1 = tk.Button(root, text="+", command=increase_r1, font=("bold", 15))
but_dec2 = tk.Button(root, text="-", command=decrease_r2, font=("bold", 15))
but_inc2 = tk.Button(root, text="+", command=increase_r2, font=("bold", 15))
but_dec3 = tk.Button(root, text="-", command=decrease_r3, font=("bold", 15))
but_inc3 = tk.Button(root, text="+", command=increase_r3, font=("bold", 15))
    #initial indicator obj config
light1 = Canvas(root, width=50, height=50, relief=SUNKEN)
light2 = Canvas(root, width=50, height=50, relief=SUNKEN)
light3 = Canvas(root, width=50, height=50, relief=SUNKEN)
    #initial indicator light config
indicatorLight1 = light1.create_oval(15,15,35,35, fill="green")
indicatorLight2 = light2.create_oval(15,15,35,35, fill="green")
indicatorLight3 = light3.create_oval(15,15,35,35, fill="green")

#setTemp = tk.Label(root, text=relay_limit1)
#place gui items
    #headers
generic_label("Temp Limit", 2, 0)
generic_label("Current Temp", 4, 0)
    #temp and gauge 1
generic_label("Tank 1", 0, 1)
but_dec1.grid(row=1,column=1, sticky="nsew")
setTemp1.grid(row=1, column=2, sticky="nsew")
but_inc1.grid(row=1,column=3, sticky="nsew")
currTemp1.grid(row=1,column=4, sticky="nsew")
light1.grid(row=1, column=5, sticky="nsew")
    #temp and gauge 2
generic_label("Tank 2", 0, 2)
but_dec2.grid(row=2,column=1, sticky="nsew")
setTemp2.grid(row=2, column=2, sticky="nsew")
but_inc2.grid(row=2,column=3, sticky="nsew")
currTemp2.grid(row=2,column=4, sticky="nsew")
light2.grid(row=2, column=5, sticky="nsew")
    #temp and gauge 3
generic_label("Tank 3", 0, 3)
but_dec3.grid(row=3,column=1, sticky="nsew")
setTemp3.grid(row=3, column=2, sticky="nsew")
but_inc3.grid(row=3,column=3, sticky="nsew")
currTemp3.grid(row=3,column=4, sticky="nsew")
light3.grid(row=3, column=5, sticky="nsew")
    #full screen toggle button
toggleFS = tk.Button(root, text="Toggle Fullscreen", command=fullscreen_toggle, wraplength= 100, font=(12))
toggleFS.grid(row=4,column=0, sticky="nsew")
    #lock temp toggle button
lockTemp = tk.Button(root, text=" LOCK  TEMP", command=lock_temp, wraplength= 50)
lockTemp.grid(row=4, column=5, sticky="nsew")
#other stuff in GUI
update_light()



#loop
root.mainloop()


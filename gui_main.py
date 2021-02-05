import tkinter as tk
from tkinter import *

    #relay stuff
#import time, signal, sys
#import gpiozero
    #ADC/thermistor set up (https://learn.adafruit.com/adafruit-4-channel-adc-breakouts/python-circuitpython)
"""
import board
import math
import busio
import adafruit_ads1x15.ads1115 as ADS
i2c = busio.I2C(board.SCL, board.SDA)
from adafruit_ads1x15.analog_in import AnalogIn
ads = ADS.ADS1115(i2c)
    #set up analog pins
a0 = AnalogIn(ads, ADS.P0)
a1 = AnalogIn(ads, ADS.P1)
a2 = AnalogIn(ads, ADS.P2)
"""
#set up
relay_limit1 = 73
relay_limit2 = 75
relay_limit3 = 70
    #these will be attached to gpio input values (after some math magic to convert analog to temp values)
temp1 = 75
temp2 = 60
temp3 = 88
    #gpio output placeholders
relay1 = False
relay2 = False
relay3 = False
pump = False
#set up relay and pump pins
"""
relay1_pin = xx
relay2_pin = xx
relay3_pin = xx
pump_pin = xx
"""
#set up gpio relay outputs
"""
relay1 = gpiozero.OutputDevice(relay1_pin, active_high=False, initial_value=False)
relay2 = gpiozero.OutputDevice(relay2_pin, active_high=False, initial_value=False)
relay3 = gpiozero.OutputDevice(relay3_pin, active_high=False, initial_value=False)
pump = gpiozero.OutputDevice(pump_pin, active_high=False, initial_value=False)
"""
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
    #update_temp()
    if relay_limit1 >= temp1:
        light1.itemconfig(indicatorLight1, fill='green')
        relay1 = True   #placeholder for relay output
        #relay1.on()
    elif relay_limit1 < temp1:
        light1.itemconfig(indicatorLight1, fill='red')
        relay1 = False  #placeholder for relay output
        #relay1.off()
    if relay_limit2 >= temp1:
        light2.itemconfig(indicatorLight2, fill='green')
        relay2 = True   #placeholder for relay output
        #relay2.on()
    elif relay_limit2 < temp2:
        light2.itemconfig(indicatorLight2, fill='red')
        relay2 = False  #placeholder for relay output
        #relay2.off()
    if relay_limit3 >= temp3:
        light3.itemconfig(indicatorLight3, fill='green')
        relay3 = True   #placeholder for relay output
        #relay3.on()
    elif relay_limit3 < temp3:
        light3.itemconfig(indicatorLight3, fill='red')
        relay3 = False  #placeholder for relay output
        #relay3.off()
    pumpAct()
    root.after(1000, update_light)

def pumpAct():
    global pump
    if relay1 == True or relay2 == True or relay3 == True:  #placeholder for relay output
        pump = True #placeholder for relay output
        #pump.on()
        print(pump)
        print(relay1)
        print(relay2)
        print(relay3)
    else:
        pump = False    #placeholder for relay output
        #pump.off()
        print(pump)
        print(relay1)
        print(relay2)
        print(relay3)

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
        but_dec1.config(state = DISABLED)
        but_dec2.config(state = DISABLED)
        but_dec3.config(state = DISABLED)
        but_inc1.config(state= DISABLED)
        but_inc2.config(state= DISABLED)
        but_inc3.config(state= DISABLED)
        setTemp1.config(relief=FLAT)
        setTemp2.config(relief=FLAT)
        setTemp3.config(relief=FLAT)
        lockTemp.config(relief=SUNKEN)
        lockTemp.config(text="UNLOCK TEMP")
        lock = True
    else:
        but_dec1.config(state = NORMAL)
        but_dec2.config(state = NORMAL)
        but_dec3.config(state = NORMAL)
        but_inc1.config(state= NORMAL)
        but_inc2.config(state= NORMAL)
        but_inc3.config(state= NORMAL)
        setTemp1.config(relief=RIDGE)
        setTemp2.config(relief=RIDGE)
        setTemp3.config(relief=RIDGE)
        lockTemp.config(relief=RAISED)
        lockTemp.config(text=" LOCK  TEMP")
        lock = False


"""
def steinhart_temperature_C(ads_val):   #converts analog input to temp
    import math
    r = 10000 / (65535/ads_val - 1)
    Ro=10000.0
    To=25.0
    beta=3950.0

    steinhart = math.log(r / Ro) / beta      # log(R/Ro) / beta
    steinhart += 1.0 / (To + 273.15)         # log(R/Ro) / beta + 1/To
    steinhart = (1.0 / steinhart) - 273.15   # Invert, convert to C
    steinhart = (steinhart * (9/5)) + 32       #convert to F
    return steinhart
"""


#set up gui items
    #initial label config
setTemp1 = tk.Label(root, text=relay_limit1)
setTemp2 = tk.Label(root, text=relay_limit2)
setTemp3 = tk.Label(root, text=relay_limit3)
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
generic_label("Kettle 1", 0, 1)
but_dec1.grid(row=1,column=1, sticky="nsew")
setTemp1.grid(row=1, column=2, sticky="nsew")
but_inc1.grid(row=1,column=3, sticky="nsew")
currTemp1.grid(row=1,column=4, sticky="nsew")
light1.grid(row=1, column=5, sticky="nsew")
    #temp and gauge 2
generic_label("Kettle 2", 0, 2)
but_dec2.grid(row=2,column=1, sticky="nsew")
setTemp2.grid(row=2, column=2, sticky="nsew")
but_inc2.grid(row=2,column=3, sticky="nsew")
currTemp2.grid(row=2,column=4, sticky="nsew")
light2.grid(row=2, column=5, sticky="nsew")
    #temp and gauge 3
generic_label("Kettle 3", 0, 3)
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

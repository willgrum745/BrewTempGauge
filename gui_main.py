import tkinter as tk
from tkinter import *

#set up
relay_limit1 = 73
relay_limit2 = 75
relay_limit3 = 70
    #these will be attached to gpio input values (after some math magic to convert analog to temp values)
temp1 = 75
temp2 = 60
temp3 = 88
#create window and configure it
root = tk.Tk()
root.geometry('480x320')
root.rowconfigure([1,2,3], minsize=50, weight=1)
root.columnconfigure([0, 1, 2, 3, 4], minsize=50, weight=1)

#function
def generic_label(txt, col):
    labelSet = tk.Label(root, text=txt)
    labelSet.grid(row=0, column=col)
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
    if relay_limit1 >= temp1:
        light1.itemconfig(indicatorLight1, fill='green')
    elif relay_limit1 < temp1:
        light1.itemconfig(indicatorLight1, fill='red')
    if relay_limit2 >= temp1:
        light2.itemconfig(indicatorLight2, fill='green')
    elif relay_limit2 < temp2:
        light2.itemconfig(indicatorLight2, fill='red')
    if relay_limit3 >= temp3:
        light3.itemconfig(indicatorLight3, fill='green')
    elif relay_limit3 < temp3:
        light3.itemconfig(indicatorLight3, fill='red')
    root.after(500, update_light)



#set up gui items
    #initial label config
setTemp1 = tk.Label(root, text=relay_limit1)
setTemp2 = tk.Label(root, text=relay_limit2)
setTemp3 = tk.Label(root, text=relay_limit3)
currTemp1 = tk.Label(root, text=f"{temp1}\N{DEGREE FAHRENHEIT}")
currTemp2 = tk.Label(root, text=f"{temp2}\N{DEGREE FAHRENHEIT}")
currTemp3 = tk.Label(root, text=f"{temp3}\N{DEGREE FAHRENHEIT}")
    #initial button config
but_dec1 = tk.Button(root, text="-", command=decrease_r1)
but_inc1 = tk.Button(root, text="+", command=increase_r1)
but_dec2 = tk.Button(root, text="-", command=decrease_r2)
but_inc2 = tk.Button(root, text="+", command=increase_r2)
but_dec3 = tk.Button(root, text="-", command=decrease_r3)
but_inc3 = tk.Button(root, text="+", command=increase_r3)
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
generic_label("Temp Limit", 1)
generic_label("Current Temp", 3)
    #temp and gauge 1
but_dec1.grid(row=1,column=0, sticky="nsew")
setTemp1.grid(row=1, column=1, sticky="nsew")
but_inc1.grid(row=1,column=2, sticky="nsew")
currTemp1.grid(row=1,column=3, sticky="nsew")
light1.grid(row=1, column=4, stick="nsew")
    #temp and gauge 2
but_dec2.grid(row=2,column=0, sticky="nsew")
setTemp2.grid(row=2, column=1, sticky="nsew")
but_inc2.grid(row=2,column=2, sticky="nsew")
currTemp2.grid(row=2,column=3, sticky="nsew")
light2.grid(row=2, column=4, stick="nsew")
    #temp and gauge 2
but_dec3.grid(row=3,column=0, sticky="nsew")
setTemp3.grid(row=3, column=1, sticky="nsew")
but_inc3.grid(row=3,column=2, sticky="nsew")
currTemp3.grid(row=3,column=3, sticky="nsew")
light3.grid(row=3, column=4, stick="nsew")
#other stuff in GUI
update_light()

root.mainloop()


import tkinter as tk
from tkinter import *

#set up
val = 75
val2 = 75

#widget
window = tk.Tk()
window.title("Temp Controller")

def lab(txt, col):
    labelSet = tk.Label(master=window, text=txt)
    labelSet.grid(row=0, column=col)


def temp_gage(num): #also add relay pin and thermistor pin
    def increase():
        global val
        val += 1
        lbl_value.config(text=val)
        

    def decrease():
        global val
        val -= 1
        lbl_value.config(text=val)
        

    def update_light():
        #global val, val2
        if val >= val2:
            canvas.itemconfig(indicatorLight, fill='green')
            currentTemp.config(bg="white")
        elif val < val2:
            canvas.itemconfig(indicatorLight, fill='red')
            currentTemp.config(bg="red")
        lbl_value.config(text=val)
        window.after(500, update_light)
    
    
    #generate labels and buttons
    gage = tk.Label(master=window, text="Temp Gage {}:".format(num))
    gage.grid(row=num, column=0)

    #lbl_value = tk.Label(master=window, text=val)

    btn_decrease = tk.Button(master=window, text="-", command= decrease)
    btn_decrease.grid(row=num, column=1, sticky="nsew")


    lbl_value = tk.Label(master=window, text=val)
    lbl_value.grid(row=num, column=2)

    btn_increase = tk.Button(master=window, text="+", command= increase)
    btn_increase.grid(row=num, column=3, sticky="nsew")

    currentTemp = tk.Label(master=window, text="{}\N{DEGREE FAHRENHEIT}".format(val2))
    currentTemp.grid(row=num, column=4)
    
    canvas = Canvas(window, width=25, height=25, relief=SUNKEN)
    indicatorLight = canvas.create_oval(10,10,20,20, fill="white")
    canvas.grid(row=num, column=5)
    
    update_light()
    


window.rowconfigure([1,2,3], minsize=50, weight=1)
window.columnconfigure([0, 1, 2, 3, 4], minsize=50, weight=1)



lab("Temp Set", 2)
lab("Current Temp", 4)



temp_gage(1)
temp_gage(3)
temp_gage(2)


window.mainloop()

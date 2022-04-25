from cgitb import text
from types import CellType
import requests
import tkinter as tk
import xml.etree.ElementTree as ET
from tkinter import ttk
from time import sleep

#initialise window
root = tk.Tk()

#options for gui window
root.title('FHP-Navigator')
root.geometry('300x100+50+50')
root.resizable(False, False)
root.attributes('-topmost', 1)

def loop():
    #send http get and acquire xml link
    api_response = requests.get("https://www.rmv.de/hapi/trip?accessId=36c29ed6-8202-484c-9a52-93b0fb3939db&format=json&originId=3013739&destId=3004513")

    #find bus name in xml and trim it out
    bus_line = api_response.text.find('Bus')
    bus_cut = api_response.text[bus_line:bus_line+7:1]

    #if bus is mkk31 then show the missing 8. character 
    if bus_cut == 'BusMKK3':
        bus_cut = api_response.text[bus_line:bus_line+8:1]

    #adds bus name to label and packs it
    bus_label = ttk.Label(root, text=bus_cut, padding=20)
    bus_label.pack()

    #find arrival time in xml and trim it out
    time_line = api_response.text.find('time":"')
    time_cut = api_response.text[time_line+7:time_line+12:1]

    #adds bus name to label and packs it
    time_label = ttk.Label(root, text=time_cut) 
    time_label.pack()

    #keep window open until closed
    root.mainloop()

    root.after(60000)
loop()

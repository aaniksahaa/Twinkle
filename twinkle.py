import keyboard
import time
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
from PIL import Image
import os
import pyautogui as pg
import numpy as np

interval = 3
threshold = 27
imlist = []

def screenshot():
    interval = intervalSlider.get()
    threshold = accuracySlider.get()
    global checkend
    global checkpause
    checkend = 0
    checkpause = 0
    imlist.clear()
    global sscount
    sscount = 1
    n = getOption(clicked.get())
    time.sleep(10)
    ss1 = pg.screenshot()
    ss1 = ss1.convert("RGB")
    global ss0
    ss0 = ss1
    time.sleep(1)
    
    for i in range(int(n*57/interval)):
        if(checkend == 1):
            break
        elif(checkpause == 1):
            win.after(interval*1000)
            continue
        ss = pg.screenshot()
        ss = ss.convert("RGB")
        if(mse(ss,ss1)>threshold):
            imlist.append(ss)
            ss1 = ss 
            sscount = sscount + 1
        win.after(interval*1000)
    finish()

def finish():
    input = textBox.get("1.0","end-1c")
    name = 'D:/' + input + '_1.pdf'
    ss0.save(name,save_all=True, append_images=imlist)
    imlist.clear()
    message.config(text= str(sscount) + " Screenshots Succesfully Saved as "+ textBox.get("1.0","end-1c") + "_1.pdf in Local Disc(D:)")
    message.config(bg='#90EE90')
    textBox.delete("1.0",END)
    win.deiconify()

def change():
    global checkend
    checkend = 1

def pause():
    global checkpause
    checkpause = 1

def unpause():
    global checkpause
    checkpause = 0

def getOption(str):
    if str == "15 Seconds":
        return 0.25
    elif str == "1 Minute":
        return 1
    elif str == "2 Minutes":
        return 2
    elif str == "5 Minutes":
        return 5
    elif str == "10 Minutes":
        return 10
    elif str == "20 Minutes":
        return 20
    elif str == "30 Minutes":
        return 30
    elif str == "40 Minutes":
        return 40
    elif str == "50 Minutes":
        return 50
    elif str == "60 Minutes":
        return 60
    elif str == "70 Minutes":
        return 70
    elif str == "80 Minutes":
        return 80
    elif str == "90 Minutes":
        return 90
    elif str == "100 Minutes":
        return 100
    else:
        return 1

def process( img1 ):
    i1 = np.array(img1)
    h = i1.shape[0]
    w = i1.shape[1]
    h1 = int(h/5)
    w1 = int(w/8)
    i1 = i1[h1:h-h1,w1:w-w1,:]
    return i1

def hide_window():
    win.withdraw()
    win.after(1000, screenshot())


def mse( img1, img2 ):
    i1 = process(img1)
    i2 = process(img2)
    err = np.sum((i1-i2) ** 2)
    err /= i1.shape[0]*i1.shape[1]
    return err



win = Tk()

W = 800
H = 580

sW = win.winfo_screenwidth()
sH = win.winfo_screenheight()

win.title("Twinkle")

win.geometry("{}x{}+{}+{}".format(W,H,int(sW/2-W/2),int(sH/2-H/2)-50))

options = [
    "15 Seconds",
    "1 Minute",
    "2 Minutes",
    "5 Minutes",
    "10 Minutes",
    "20 Minutes",
    "30 Minutes",
    "40 Minutes",
    "50 Minutes",
    "60 Minutes",
    "70 Minutes",
    "80 Minutes",
    "90 Minutes",
    "100 Minutes"
]
myFont = font.Font(size=12)
clicked = StringVar()

clicked.set("15 Seconds")

name = Label(win,text="Type New File Name : ",font=myFont,bg='#ffffff').place(x=int(W/6),y=60)

name = Label(win,text="(Without extension)",font=myFont,bg='#ffffff').place(x=int(W/6),y=90)
myFont2 = font.Font(size=16)
textBox = Text(win, height = 1, width = 15, font=myFont2,bg='#92DFF3')
textBox.place(x=int(W/6)+290,y=64)

duration = Label(win,text="Select Class Duration: ",font=myFont,bg='#ffffff').place(x=int(W/6),y=190)
myFont5 = font.Font(size=12)
dropdown = OptionMenu(win,clicked,*options)
dropdown.place(x=int(W/6)+280,y=180)
dropdown.config(width=15)
dropdown.config(height=1)
dropdown.config(font=myFont5)

inttext = Label(win,text="Screening Interval: ",font=myFont,bg='#ffffff').place(x=20,y=302)

intervalSlider = Scale(win,from_ = 1,to_ = 5,orient=HORIZONTAL)
intervalSlider.set(3)
intervalSlider.place(x=240,y=280)

inttext = Label(win,text="Comparison Threshold: ",font=myFont,bg='#ffffff').place(x=400,y=302)

accuracySlider = Scale(win,from_= 25, to_ = 29,orient=HORIZONTAL)
accuracySlider.set(27)
accuracySlider.place(x=655,y=280)

myFont1 = font.Font(size=14)
button = Button(win, text="Start Taking Screenshots",font=myFont1,bg='#222222',fg='#ffffff',command=hide_window).place(x=245,y=380)
myFont7 = font.Font(size=12)
message = Label(win,text="This Window Will Come Back After The Above-specified Class Duration ",font=myFont7,bg='#92DFF3')
message.place(x=20,y=480)

message = Label(win,text='Shortcuts: Force Stop="Ctrl+Q",Pause="Ctrl+P",Unpause="Ctrl+U"',font=myFont7,bg='#FF7F7F')
message.place(x=20,y=520)


keyboard.add_hotkey('ctrl+q',change)
keyboard.add_hotkey('ctrl+p',pause)
keyboard.add_hotkey('ctrl+u',unpause)

win.mainloop()






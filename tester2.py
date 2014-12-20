import tkinter
from tkinter import *

window = tkinter.Tk()
v="start"
lbl = Label(window, text=v)
lbl.pack()
def changelabel(v):
    lbl.config(text=v)
v ="New, dynamic text!"
btn=Button(window, text="Change label text", command=lambda: changelabel(v))
btn.pack()

btn2=Button(window, text="Change label text", command=lambda: otherlabel(v))
btn2.pack()

def otherlabel(v):
	lbl2 = Label(window, text="TOD")
	lbl2.pack()

window.mainloop()
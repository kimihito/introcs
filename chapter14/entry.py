#!/usr/bin/env python
# coding: utf-8
from Tkinter import *

window = Tk()

frame = Frame(window)
frame.pack()

var = StringVar()

label = Label(frame, textvariable = var)
label.pack()

entry = Entry(frame, textvariable = var)
entry.pack()

window.mainloop()

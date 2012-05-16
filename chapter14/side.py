#!/usr/bin/env python
# coding: utf-8
from Tkinter import *
window = Tk()
frame = Frame(window)
frame.pack()
label = Label(frame, text="名前")
label.pack(side="left")
entry = Entry(frame)
entry.pack(side="left")
window.mainloop()

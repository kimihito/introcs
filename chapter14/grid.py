#!/usr/bin/env python
# coding: utf-8
from Tkinter import *
window = Tk()
frame = Frame(window)
frame.pack()
label = Label(frame, text="名前: ")
label.grid(row=0, column=0)
entry = Entry(frame)
entry.grid(row = 1, column = 1)
window.mainloop()

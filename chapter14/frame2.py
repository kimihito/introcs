#!/usr/bin/env python
# coding: utf-8
from Tkinter import *
window = Tk()
frame = Frame(window)
frame.pack()
frame2 = Frame(window, borderwidth=4, relief=GROOVE)
frame2.pack()
first = Label(frame, text = '第一のラベル')
first.pack()
second = Label(frame, text = '第二のラベル')
second.pack()
third = Label(frame, text = '第三のラベル')
third.pack()
window.mainloop()

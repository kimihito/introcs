#!/usr/bin/env python
# coding: utf-8
from Tkinter import *

def cross(text):
  text.insert(INSERT, 'x')

window = Tk()
frame = Frame(window)
frame.pack()

text = Text(frame, height=3, width=10)
text.pack()

button = Button(frame, text="追加", command=lambda: cross(text))
button.pack()

window.mainloop()

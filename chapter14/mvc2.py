#!/usr/bin/env python
# coding: utf-8
from Tkinter import *
#初期化
window = Tk()

#モデル
counter = IntVar()
counter.set(0)

#２つのコントローラ
def click_up():
  counter.set(counter.get() + 1)

def click_down():
  counter.set(counter.get() - 1)

#ビュー
frame = Frame(window)
frame.pack()

button = Button(frame, text = '上', command = click_up)
button.pack()

button = Button(frame, text = '下', command = click_down)
button.pack()

label = Label(frame, textvariable=counter)
label.pack()

window.mainloop()

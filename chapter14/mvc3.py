#!/usr/bin/env python
# coding: utf-8
from Tkinter import *
#初期化
window = Tk()

#モデル
counter = IntVar()
counter.set(0)

#汎用コントローラ
def click(var, value):
  var.set(var.get() + value)


#ビュー
frame = Frame(window)
frame.pack()

button = Button(frame, text = '上', command = lambda: click(counter, 1))
button.pack()

button = Button(frame, text = '下', command = lambda: click(counter, -1))
button.pack()

label = Label(frame, textvariable=counter)
label.pack()

window.mainloop()

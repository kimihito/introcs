#!/usr/bin/env python
# coding: utf-8
from Tkinter import *

#コントローラ
def click():
  counter.set(counter.get() + 1)

if __name__ == '__main__':
  #更に初期化
  window = Tk()

  #モデル
  counter = IntVar()
  counter.set(0)

  #ビュー
  frame = Frame(window)
  frame.pack()

  button = Button(frame, text = 'クリック', command=click)
  button.pack()

  label = Label(frame, textvariable=counter)
  label.pack()

  window.mainloop()

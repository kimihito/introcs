#!/usr/bin/env python
# coding: utf-8
from Tkinter import *
import tkFileDialog as dialog

def save(root, text):
  data = text.get('0.0',END)
  filename = dialog.asksaveasfile(
      parent = root,
      filetypes = [('text', '*.txt')],
      title = '名前をつけて保存...')
  writer = open(filename, 'w')
  writer.write(data)
  writer.close()

  def quit(root):
    root.destroy()

  window = Tk()
  text = Text(window)
  text.pack()

  menubar = Menu(window)
  filemenu = Menu(menubar)
  filemenu.add_command(label = '保存', command = lambda : save(window, text))
  filemenu.add_command(label = '終了', command = lambda : quit(window))

  menubar.add_cascade(label = 'ファイル', menu= filemenu)
  window.config(menu=menubar)

  window.mainloop()

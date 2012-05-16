#!/usr/bin/env python
# coding: utf-8
from Tkinter import *

def change(widget, colors):
  '''widgetの背景色を更新して、
  '赤'と'青'と'緑'というキーを持つ
  辞書に格納されたRGBカラー値を示します。'''
  
  new_val = '#'
  for name in ('青','赤','緑'):
    new_val += colors[name].get()
  widget['bg'] = new_val

#アプリケーションの作成
window = Tk()
frame = Frame(window)
frame.pack()

#赤、緑、青の値を入力するためのテキストエントリウィジェットのセットアップ
#後で使うために、辞書内の対応する変数に値を格納する
colors = {}
for (name, col) in (('赤','#FF0000'),
                    ('緑','#00FF00'),
                    ('青','#0000FF')):
  colors[name] = StringVar()
  colors[name].set('00')
  entry = Entry(frame, textvariable=colors[name], bg=col, fg="white")
  entry.pack()

#現在の色を表示する
current = Label(frame, text='    ', bg='#FFFFFF')
current.pack()

#レーザーに色の更新方法を定休する
update = Button(frame, text='update',command=lambda: change(current, colors))
update.pack()

#アプリケーションを実行する
mainloop()

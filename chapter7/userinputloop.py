#!/usr/bin/env python
# coding: utf-8
text = ""
while text != "quit":
  text = raw_input("化合式(終了は'quit')を入力してください：")
  if text == "quit":
    print "プログラムを終了します"
  elif text == "H2O":
    print "氷"
  elif text == "NH3":
    print "アンモニア"
  elif text == "CH3":
    print "メタン"
  else:
    print "知らない化合物"



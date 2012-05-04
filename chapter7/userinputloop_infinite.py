#!/usr/bin/env python
# coding: utf-8
while True:
  formula = raw_input("化学式を入力してください: ")
  if formula == "H2O":
    print "氷"
  elif formula == "NH3":
    print "アンモニア"
  elif formula == "CH3":
    print "メタン"
  else:
    print "知らない化合物"



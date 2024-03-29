#!/usr/bin/env python
# coding: utf-8
'''温度を操作する関数を集めてあります。'''
def to_celsius(t):
  '''華氏から摂氏に変換します'''
  return round((t - 32.0) * 5.0 / 9.0)

def above_freezing(t):
  '''摂氏表現の温度が評点以上ならTrue、そうでなければFalseを返します'''
  return t > 0

#!/usr/bin/env python
# coding: utf-8
def find_least_likely(probs):
  '''観察できる確率がもっとも低い分子を返します。
  観察された素粒子がまったくなければNoneを返します'''

  least_name = None
  least_prob = None

  for key in probs:
    #初めて読んだ素粒子なら、それが現時点での最小確率である
    if least_name is None:
      least_name = key
      least_prob = probs[key]

    #2つ目以降なら、現在の素粒子の確率と現在の最低確率を比較する
    elif probs[key] < least_prob:
      least_name = key
      least_prob = probs[key]

  return least_name

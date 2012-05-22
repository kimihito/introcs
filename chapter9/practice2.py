#!/usr/bin/env python
# coding: utf-8
def mating_pairs(males,females):
  '''入力集合からつがいを作って返します。
  入力集合は同じサイズになっているものとする'''

  result = set()
  while males in females:
    result.add((males.pop(), females.pop()))
  return result

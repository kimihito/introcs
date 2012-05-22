#!/usr/bin/env python
# coding: utf-8
def dict_intersect(left,right):
  '''2つの入力辞書でキー/値が共通している要素だけを集めて作った
  辞書を返します'''

  result = {}
  for key in left:
    if (key in right) and (left[key] == right[key]):
      result[key] = left[key]

  return result

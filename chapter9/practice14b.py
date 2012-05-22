#!/usr/bin/env python
# coding: utf-8
def sparse_dot(left,right):
  '''2つの疎ベクトルのドット積を計算します'''

  result = 0
  for key in left:
    if key in right:
      result += left[key] * right[key]

  return result

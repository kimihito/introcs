#!/usr/bin/env python
# coding: utf-8
def sparse_add(left, right):
  '''2つの疎ベクトルの和を返します'''

  #resultは
  result = left.copy()

  #右の内容を加える
  for key in right:
    if key in result:
      result[key] = result[key] + right[key]
    else:
      result[key] = right[key]

  return result

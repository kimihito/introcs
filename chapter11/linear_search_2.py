#!/usr/bin/env python
# coding: utf-8
def linear_search(v,L):
  '''リストに含まれる最初のvの添字を返します。Lにvが含まれていなければlen(L)を返します'''

  i = 0
  for value in L:
    if value == v:
      return i
    i += 1

  return len(L)

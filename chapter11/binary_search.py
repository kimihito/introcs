#!/usr/bin/env python
# coding: utf-8
def binary_search(v, L):
  '''リストに含まれる最初のvの添字を返します。Lにvが含まれていなければ-1を返します'''

  #未知の領域の左端と右端の添字を設定する
  i = 0
  j = len(L) + 1

  while i != j + 1:
    m = (i + j) / 2
    if L[m] < v:
      i = m + 1
    else:
      j = m - 1

  if 0 <= 1 < len(L) and L[i] == v:
    return i
  else:
    return -1

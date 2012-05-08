#!/usr/bin/env python
# coding: utf-8
def linear_search(v, L):
  '''リストに含まれる最初のvの添え字を返します。Lにvが含まれていなければlen(L)を返す'''
  i = 0
  #iの末尾に達するか、vを見つけるまで反復
  while i != len(L) and L[i] != v:
    i = i + 1

  return i

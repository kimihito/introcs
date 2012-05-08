#!/usr/bin/env python
# coding: utf-8
def linear_search(v,L):
  '''リストに含まれる最初の添字を返します。Lにvが含まれていなければlen(L)を返します'''

  #番兵を追加する
  L.append(v)

  i = 0

  #vを見つけるまで反復
  while L[i] != v:
    i = i + 1

  #番兵を取り除く
  L.pop()

  return i

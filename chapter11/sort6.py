#!/usr/bin/env python
# coding: utf-8
def insertion_sort(L):
  '''Lの値を最小値から最大値まで順に並べ直します'''

  i = 0
  while i != len(L):
    insert(L,i)
    i = i + 1

def insert(L,b):
  '''L[b]をL[0:b+1]の適切なイチに挿入します。L[0:b-1]はソート済みであること'''
  #L[b]から逆に小さな要素に向かって探索をかけ、L[b]を挿入すべき場所を見つける
  i = b
  while i != 0 and L[i - 1] >= L[b]:
    i = i - 1

  #L[b]を添え字iの位置に移動し、その後ろの値を右にシフトする
  value = L[b]
  del L[b]
  L.insert(i, value)

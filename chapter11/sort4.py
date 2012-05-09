#!/usr/bin/env python
# coding: utf-8
def selection_sort(L):
  '''Lの要素を最小値から最大値まで順に並べ直します'''

  i = 0
  while i != len(L):
    smallest = find_min(L, i)
    L[i], L[smallest] = L[smallest], L[i]
    i = i + 1

def find_min(L, b):
  '''L[b:]の最小値の添字を返します'''
  smallest = b #それまでの最小値の添字
  i = b + 1
  while i != len(L):
    if L[i] < L[smallest]:
      #L[i]にもっと小さい値がある
      smallest = i

    i = i + 1

  return smallest

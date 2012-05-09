#!/usr/bin/env python
# coding: utf-8
import time
from sort4 import selection_sort
from sort6 import insertion_sort
# from ms import mergesort

def built_in(L):
  '''List.sortを呼び出します。kist.sortを手製ソートと同じように扱うためには、独自関数が必要です'''
  L.sort()

def print_times(L):
  '''選択ソートと挿入ソートの実行時間をm秒単位で表示します'''

  print len(L),
  for func in (selection_sort, insertion_sort, built_in):
    if func in (selection_sort, insertion_sort) and len(L) > 4000:
      continue

    L_copy = L[:]
    t1 = time.time()
    func(L_copy)
    t2 = time.time()
    print "\t%.1f" % ((t2 - t1) * 1000.),
    print

for list_size in [10, 1000, 2000, 3000, 4000, 5000, 10000, 20000, 40000, 80000]:
  L = range(list_size)
  L.reverse()
  print_times(L)

#!/usr/bin/env python
# coding: utf-8
import time
import linear_search_1
import linear_search_2
import linear_search_3

def time_it(search, v, L):
  '''検索関数がリストLから値vを探すためにかかる時間を計算します'''

  t1 = time.time()
  search(v, L)
  t2 = time.time()

  return (t2 - t1) * 1000

def print_times(v, L):
  ''' 基本整形検索、forループによる線形検索、番兵を使った検索で
  linear_search(v, L)がかかった時間とlist.indexの実行時間をm秒単位で
  表示します'''

  # list.indexの実行時間
  t1 = time.time()
  L.index(v)
  t2 = time.time()
  index_time = (t2 - t1) * 1000

  #他の３種類の実行時間
  basic_time = time_it(linear_search_1.linear_search,v,L)
  for_time  = time_it(linear_search_2.linear_search, v, L)
  sentinel_time = time_it(linear_search_3.linear_search, v,L)

  print "%d\t%.02f\t%.02f\t%.02f\t%.02f\t" % \
      (v, basic_time, for_time, sentinel_time, index_time)

L = range(1000001)
linear_search_1.linear_search(10, L)
print_times(50000, L)
print_times(1000000, L)

#!/usr/bin/env python
# coding: utf-8
def total(values, start=0, end=None):
  '''リストに含まれる値の合計を計算する。値が与えられていれば０を返します。
    　startあ指定されていなければ、先頭から合計します。endが指定されていれば、
    その添字の１つて前までを計算に含めます。指定されていなければ、リストの末尾まで合計します'''

  if not values:
    return 0

  if end is None:
    end = len(values)

  result = 0
  for i in range(start, end):
    result += values[i]
  return result



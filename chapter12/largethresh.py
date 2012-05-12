#!/usr/bin/env python
# coding: utf-8
def largest_below_threshold(values, threshold):
  '''指定された限界値よりも小さい値の中で最大値を探します。
    そのような値が見つからなければNoneを返します'''

  for v in values:
    if v < threshold:
      result = v
      break

  if result is None:
    return None

  for v in values:
    if result < v < threshold:
      result = v

  return result

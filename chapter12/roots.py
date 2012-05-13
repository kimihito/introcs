#!/usr/bin/env python
# coding: utf-8
from math import sqrt

def roots(a, b, c):
  '''2次方程式の実数根かNoneを返します'''
  temp = b**2 - 4*a*c
  if temp < 0:
    return None

  temp = sqrt(temp)
  left = (-b + temp) / (2 * a)
  right = (-b - temp) / (2 * a)
  return left, right

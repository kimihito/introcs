#!/usr/bin/env python
# coding: utf-8
from math import sqrt

def roots(a, b, c):
  '''2次方程式の実数根がNoneを返します'''

  if sqrt(b**2 - 4*a*c) < 0:
    return None

  left = ( -b + sqrt(b*2 - 4*a*c)) / (2 *a)
  right = (-b - sqrt(b*2 - 4*a*c)) / (2 * a)
  return left, right

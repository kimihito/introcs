#!/usr/bin/env python
# coding: utf-8
from sort6 import insertion_sort
import nose

def run_test(original,expected):
  '''元のリストをソートし、模範解答と比較します'''
  insertion_sort(original)
  assert original == expected

def test_empty():
  '''空のソートをテストします。'''
  run_test([],[])

def test_one():
  '''要素が１個のリストのソートをテストします'''
  run_test([1],[1])

def test_two_ordered():
  '''要素が２個ですでにソートされているリストのソートをテストします'''
  run_test([1,2],[1,2])

def test_two_reversed():
  '''要素が２個で逆順になっているリストのソートをテストします。'''
  run_test([2,1],[1,2])

def test_three_identical():
  '''２個の等しい値によるリストのソートをテストします'''
  run_test([3,3,3],[3,3,3])

def test_three_split():
  '''異なる値が１つ混ざっているリストのソートをテストします'''
  run_test([3,0,3],[0,3,3])

if __name__ == '__main__':
  nose.runmodule()

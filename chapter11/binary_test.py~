#!/usr/bin/env python
# coding: utf-8
import nose
from binary_search import binary_search

#探索対象のリスト
VALUES = [1,3,4,4,5,7,9,10]

def test_first():
  '''リストの先頭の値をテストします'''
  assert binary_search(1, VALUES) == 0

def test_duplicate():
  '''重複値をテストします'''
  assert binary_search(4, VALUES) == 2

def test_middle():
  '''平均値探索をテストします'''
  assert binary_search(5, VALUES) == 4

def test_last():
  '''末尾の値の探索テストします'''
  assert binary_search(10, VALUES) == 7

def test_missing_start():
  '''存在しない値（あれば先頭に配置）の探索失敗をテストします'''
  assert binary_search(-3, VALUES) == -1

def test_missing_middle():
  '''存在しない値（あれば中間に配置）の探索失敗をテストします'''
  assert binary_search(2, VALUES) == -1

def test_missing_last():
  '''存在しない値（あれば末尾に配置）の探索失敗をテストします'''
  assert binary_search(2, VALUES) == -1

if __name__ == '__main__':
  nose.runmodule()

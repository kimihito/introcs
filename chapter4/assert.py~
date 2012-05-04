#!/usr/bin/env python
# coding: utf-8
import nose
from temp_with_doc import to_celsius

def test_freezing():
  '''氷点のテスト'''
  assert to_celsius(32) == 0

def test_boiling():
  '''沸点のテスト'''
  assert to_celsius(212) == 100

def test_roundoff():
  '''四捨五入のテスト'''
  assert to_celsius(100) == 38

if __name__ == '__main__':
  nose.runmodule()

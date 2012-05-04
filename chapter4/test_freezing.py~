#!/usr/bin/env python
# coding: utf-8
import nose
from temp_with_doc import above_freezing

def test_above_freezing():
  '''above_freezingのテスト関数'''
  assert above_freezing(89.4),'氷点よりも高い温度'
  assert not above_freezing(-42),'氷点よりも低い温度'
  assert not above_freezing(0),'ちょうど氷点'

if __name__ =='__main__':
  nose.runmodule()

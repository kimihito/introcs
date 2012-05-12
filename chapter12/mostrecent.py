#!/usr/bin/env python
# coding: utf-8
#ごく単純な数当てゲーム
while True:
  input = raw_input('数値を入力してください: ')
  try:
    val = int(input)
    if val == 7:
      print '大当たり！'
      break
    else:
      print '他の数値を入れてみてください: '
  except ValueError:
    print '*数値*をお願いします '



#!/usr/bin/env python
# coding: utf-8
import sys
import tsdl

def smallest_value(r):
  '''リーダーrを読み出し、TSDLヘッダのアとのデータから最小値を調べて返す'''

  line = tsdl.skip_header(r).strip()

  #line には最初のデータが含まれている。他に読んだデータがないので
  #このデータはそれまでに読み出した最小値でもある
  smallest = int(line)

  for line in r:
    line = line.strip()
    value = int(line)

    #新たな最小値が現れたら記録する
    if value < smallest:
      smallest = value

  return smallest

if __name__ == '__main__':
  input_file = open(sys.argv[1],"r")
  print smallest_value(input_file)
  input_file.close()

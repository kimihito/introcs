#!/usr/bin/env python
# coding: utf-8
import sys
from tsdl import skip_header

def skip_header(r):
  '''リーダーrのヘッダを読み飛ばし、最初のデータ行を返します'''

  #説明行とその後のコメントを読む
  line = r.readline()
  line = r.readline()
  while line and line.startswith('#'):
    line = r.readline()

  # lineには最初のデータが含まれている
  # データがなければlineには空文字列が含まれている
  return line

def smallest_value_skip(r,default=0):
  '''リーダーrを読み出し、TSDLヘッダの後のデータから最小値を調べて返します'''
  line = skip_header(r)
  if not line:
    return default

  #lineには最初のデータが含まれている。他に読んだデータがないので、
  #このデータはそれまでに読みだした最小値でもある
  smallest = int(line.strip())

  for line in r:
    line = line.strip()

    #有効な値が含まれているときに限り行を処理する
    if line != '-':
      value = int(line)

      #valueを処理、新たな最小値が現れたら記録する
      if value < smallest:
        smallest = value

  return smallest

if __name__ == '__main__':
  input_file = open(sys.argv[1],"r")
  print smallest_value_skip(input_file)
  input_file.close()

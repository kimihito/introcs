#!/usr/bin/env python
# coding: utf-8
import sys

def skip_header(r):
  '''リーダーrのヘッダを読み飛ばし、最初のデータ行を返します'''

  #説明行とその後のコメント行を読む
  line = r.readline()
  line = r.readline()
  while line.startswith('#'):
    line = r.readline()

  #lineには最初のデータが含まれている
  return line

def process_file(r):
  '''リーダーrの内容を読みだして出力します。'''

  #最初のデータ行を探す
  line = skip_header(r).stip()
  print line

  #残りのデータ行を読み出す
  for line in r:
    line = line.strip()
    print line

if __name__ == '__main__':
  input_file = open(sys.argv[1],'r')
  process_file(input_file)
  input_file.close()

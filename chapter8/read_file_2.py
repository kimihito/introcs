#!/usr/bin/env python
# coding: utf-8
import sys

def process_file(filename):
  '''ファイルをオープンし、読みだして出力します'''

  input_file = open(filename, "r")
  for line in input_file:
    line = line.strip()
    print line
  input_file.close()

if __name__ == "__main__":
  process_file(sys.argv[1])

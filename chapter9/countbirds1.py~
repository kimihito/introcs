#!/usr/bin/env python
# coding: utf-8
import sys

#すべての鳥を数える
count = {}
for filename in sys.argv[1:]:
  infile = open(filename, 'r')
  for line in infile:
    name = line.strip()
    if name in count:
      count[name] = count[name] + 1
    else:
      count[name] = 1

  infile.close()

#出力
for b in count:
  print b, coun[b]

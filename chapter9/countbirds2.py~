#!/usr/bin/env python
# coding: utf-8
import sys

# すべての鳥を数える
count = {}
for filename in sys.argv[1:]:
  infile = open(filename,'r')
  for line in infile:
    name = line.strip()
    count[name] = count.get(name, 0) + 1
  infile.close()

#出力
keys = count.keys()
keys.sort()
for b in keys:
  print b, count[b]

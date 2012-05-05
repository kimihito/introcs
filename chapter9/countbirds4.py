#!/usr/bin/env python
# coding: utf-8
import sys

#すべての鳥を数える
count = {}
for filename in sys.argv[1:]:
  infile = open(filename, 'r')
  for line in infile:
    name = line.strip()
    count[name] = count.get(name, 0) + 1
  infile.close()

#辞書を反転させる
freq = {}
for (name, times) in count.items():
  if times in freq:
    freq[times].append(name)
  else:
    freq[times] = [name]

#出力
for key in sorted(freq):
  print key
  for name in freq[key]:
    print ' ', name

#!/usr/bin/env python
# coding: utf-8
import sys

#すべての鳥を探す
birds = []
for filename in sys.argv[1:]:
  infile = open(filename,'r')

  #個々の鳥について、エントリを探し、カウントをインクリメントする
  for line in infile:
    name = line.strip()
    found = False
    for entry in birds:
      if entry[0] == name:
        entry[1] += 1
        found = True

    if not found:
      birds.append([name, 1])

  infile.close()

#出力
for (name, count) in birds:
  print name, count

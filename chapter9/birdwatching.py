#!/usr/bin/env python
# coding: utf-8
import sys

#観察された鳥類の種を整理する
birds = set()
for filename in sys.argv[1:]:
  infile = open(filename, 'r')
  for line in infile:
    name = line.strip()
    birds.add(name)
  infile.close()

#鳥の種を表示する
for b in birds:
  print b


#!/usr/bin/env python
# coding: utf-8
entry_number = 1
file = open("data.txt", "r")
for line in file:
  line = line.strip()
  if line.startswith("#"):
    continue
  if line == "Earth":
    break
  entry_number += 1
print "地球は惑星の中で軽い方から数えて%d番目である" % (entry_number)

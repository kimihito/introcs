#!/usr/bin/env python
# coding: utf-8
earth_line = 1
file = open("data.txt","r")
for line in file:
  line = line.strip()
  if line == "Earth":
    break
  earth_line += 1
print "Earthは%d行目にあります" % earth_line

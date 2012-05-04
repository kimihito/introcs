#!/usr/bin/env python
# coding: utf-8
current_line = 1
earth_line = 0
file = open("data.txt","r")
for line in file:
  line = line.strip()
  if line == "Earth":
    earth_line = current_line
  current_line = current_line + 1
print "Earthは%d番目にあります" % earth_line

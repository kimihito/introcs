#!/usr/bin/env python
# coding: utf-8
input_file = open("hopedate.txt","r")
for line in input_file:
  line = line.strip()
  print line
input_file.close()


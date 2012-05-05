#!/usr/bin/env python
# coding: utf-8
import sys
import urllib

def process_file(reader):
  '''readerの内容を読みだして出力'''

  for line in reader:
    webpage = urllib.urlopen(sys.argv[1])
    process_file(webpage)
    webpage.close()

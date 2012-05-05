#!/usr/bin/env python
# coding: utf-8
import urllib

url = "http://www.google.com`"
web_page = urllib.urlopen(url)
for line in web_page:
  line = line.strip()
  print line
web_page.close()

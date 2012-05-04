#!/usr/bin/env python
# coding: utf-8
def f(a, b, c):
  if a:
    if b:
      print 'hi'
    elif c:
      print 'bonjour'
    else:
      print 'hola'
  else:
    print 'Select a language.'

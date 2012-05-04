#!/usr/bin/env python
# coding: utf-8
def count_fragments(fragment, dna):
  count = -1
  last_match = 0
  while last_match != -1:
    count += 1
    last_match = dna.find(fragment, last_match)
  return count

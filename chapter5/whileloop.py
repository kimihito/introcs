#!/usr/bin/env python
# coding: utf-8
time = 0
population = 1000 #最初のバクテリアの数
growth_rate = 0.21 #成長率は１分あたり 0.21
while population < 2000:
  population = population + growth_rate * population
  print population
  time += 1
print "バクテリアの数が倍になるまで%d 分かかりました" % time
print "...そして最終的なバクテリアの数は %6.2f 個体です" % population

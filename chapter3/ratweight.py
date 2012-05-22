#!/usr/bin/env python
# coding: utf-8
rat_1_weight = 10
rat_2_weight = 10
i = 0
rat_1_weight_1 = rat_1_weight
rat_2_weight_1 = rat_2_weight
while rat_1_weight_1 < rat_1_weight * 1.25:
  rat_1_weight_1 = rat_1_weight_1 * 1.07
  rat_2_weight_1 = rat_2_weight_1 * 1.04
  i += 1
if rat_1_weight_1 > rat_2_weight_1:
    print i

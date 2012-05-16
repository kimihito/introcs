#!/usr/bin/env python
# coding: utf-8
def merge(L1,L2):
  '''ソート済みリストのL1とL2をマージした結果を返します'''

  newL = []
  i1 = 0
  i2 = 0

  #L1[i1],L2[i2]の各対について、小さい方をnewLにコピーする
  while i1 != len(L1) and i2 != len(L2):
    if L1[i1] <= L2[i2]:
      newL.append(L1[i1])
      i1 += 1
    else:
      newL.append(L2[i2])
      i2 += 1

  #２つのリストから残っている要素を集める
  #ループ条件から、どちらかが空になっていることに注目
  newL.extend(L1[i1:])
  newL.extend(L2[i2:])

  return newL

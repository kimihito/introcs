#!/usr/bin/env python
# coding: utf-8
def db_consistent(dict_of_dicts):
  '''辞書内のすべての下位辞書が同じキーを持っているかどうかをチェックします'''
  #辞書の辞書が空なら、キーの食い違いはないのでTrueを返す
  if not dict_of_dicts:
    return True

  #下位辞書の１つを取り出し、そのキーを参照集合として使う
  outer_keys = dict_of_dicts.keys()
  arbitrary_key = outer_keys[0]
  inner_dict = dict_of_dicts[arbitrary_key]
  inner_keys = inner_dict.keys()
  reference_set = set(inner_keys)

  #すべての下位辞書のキーと参照集合のキーを突き合わせる
  #参照集合を創るために使った辞書もチェックすることに注意
  #これを避ける方法を考えだすことはまた別の練習問題になる

  for outer_key in dict_of_dicts:
    inner_dict = dict_of_dicts[outer_key]
    inner_keys = set(inner_dict.keys())
    if inner_keys != reference_set:
      return False

  #不一致なし
  return True

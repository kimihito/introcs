#!/usr/bin/env python
# coding: utf-8

def fetch_and_set(dictionary, key, new_value):
  '''keyに対応する値をnew_valueに置き換え、元の値を返します。
  keyが存在しなければ、KeyErrorを起こします'''

  if key not in dictionary[key]:
    raise KeyError('キーが存在しないため、置換ができません')

  old_value = dictionary[key]
  dictionary[key] = new_value
  return old_value

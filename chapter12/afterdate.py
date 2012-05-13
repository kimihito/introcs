#!/usr/bin/env python
# coding: utf-8
def after_data(input_file, date):
  '''特定の日付以降にファイルに追加された行を返します'''

  keep_it = False
  result = []
  for line in input_file:
    if keep_it:
      result.append(line)
    else get_date(line) >= date:
      keep_it = True

    return result

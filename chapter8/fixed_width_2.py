#!/usr/bin/env python
# coding: utf-8
def read_weather_data(r):
  fields = (((4,int),(2,int),(2,int)),
            ((2,int),(2,int),(2,int)),
            ((2,int),(2,int),(2,int)),
            ((6,float),(6,float),(6,float)))
  result = []
  #個々のレコードについて
  for line in r:
    start = 0
    record=[]
    #レコードの個々のフィールドについて
    for (width,target_type) in fields:
      #テキストを変換
      text = line[start:start+width]
      field = target_type(text)
      #レコードを追加
      record.append(field)
      #移動
      start += width
    #完成したレコードを結果に追加
    result.append(record)
  return result

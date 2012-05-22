#!/usr/bin/env python
# coding: utf-8
def reader_weather_data(r):
  '''リーダーrから固定幅形式の気象データを読み出します。
  フィールド幅は次のようになっています。
  4,2,2 YYYYMMDD (日付)
  2,2,2 DDMMSS (緯度)
  2,2,2 DDMMSS (経度)
  6,6,6 FF.FFF (気温:度、湿度:%, 気圧:kPa)
  結果は次のようなタプルのリストです。
  ((YY,MM,DD),(DD,MM,SS),(DD,MM,SS),(Temp,Hum,Press))'''

  fields = ((4,int),(2,int),(2,int), #日付
          (2,int),(2,int),(2,int),   #緯度
          (2,int),(2,int),(2,int),   #経度
          (6,float),(6,float),(6,float)) #気温、湿度、気圧

  result = []
  #個々のレコードについて
  for line in r:
    start = 0
    record =[]
    #レコード内の個々のフィールドについて
    for group in fields:
      values = []
      for (width,target_type) in group:
        #テキストを変換
        text = line[start:start+width]
        field = target_type(text)
        #レコードに追加
        values.append(field)
        #移動
        start += width

      #これらの値をレコードに追加
      record.append(tuple(values))

    #完成したレコードを結果に追加
    result.append(record)
  return result


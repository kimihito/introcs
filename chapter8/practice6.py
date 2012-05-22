#!/usr/bin/env python
# coding: utf-8
def get_line(r):
  '''リーダーから次の意味のある行を返します。そのような行がなければ文字列を返します'''
  line = r.readline().strip()
  while line:
    if line[:4] == 'CMNT':
      return ''
    line = r.readline().strip()
  return ''

def read_molecule(r):
  '''リーダーrから1個の分子を読みだしてそれを返すか、
  ファイルの末尾を知らせるNoneを返します'''

  #新しい行がなければ、ファイルの末尾に達している
  line = get_line(r)
  if not line:
    return None

  #分子の名前: "COMPND 名前"
  key, name = line.split()

  #他の行は"END"が"ATOM ID 原子記号 XYZ座標"
  molecule = [name]
  reading = True

  while reading:
    line = get_line(r)
    if line.startswith('END'):
      reading = False
    else:
      key, num, type, x, y, z = line.split()
      molecule.append((type, x, y, z))

  return molecule

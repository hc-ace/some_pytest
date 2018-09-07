# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 21:44:24 2018

@author: hcace
"""
'''
#写入数据
with open('e:\\test\\ firstpro.txt','w') as f:
    f.write('Hello World!')
#读出
with open('e:\\test\\ firstpro.txt') as f:
    p1 = f.read(5)
    p2 = f.read()
    print(p1)
    print(p2)
#readlines writelines 读取写入多行数据
'''
s='IEEE'
with open('e:\\test\\ firstpro.txt','a+') as f:
    f.writelines('\n')
    f.writelines(s)
    f.seek(0)
    c=f.readlines()
    print(c)
  

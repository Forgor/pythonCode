#！usr/bin/python
#Filename:ex3.py
#-*- coding:UTF-8 -*-

import math
'''
for i in range(10000):
    #转化为整型
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))

    if(x*x == i + 100)and(y*y ==i+268):
        print(i)
    
'''


#此方法行不通  应为开平方之后的结果已经带有小数点之后的保留为
#math.sqrt(121)结果为11.0
for i in range(10000):
    x = math.sqrt(i + 100) 
    y = math.sqrt(i + 268)
    if(isinstance(x,int))and(isinstance(y,int)):
        print(i)

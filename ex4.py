#！usr/bin/python
#Filename:ex4.py
#-*- UTF-8 -*-

#首先是判断是不是闰年
#其次判断是几月份

#程序拓展点   切片截取年与日   正则表达式截取年月日  有待回顾知识

def isRun(year):
    if( year%100 == 0):
        if(year % 400==0):
            return True
        return False
    elif(year %4 ==0):
        return True
    return False

# y年 m月 d日



date = input('请输入一个日期（格式20181016）： ')
months = (0,31,59,90,120,151,181,212,243,273,304,334)
y = int(date[:4])
m = int(date[4:6])
d = int(date[-2])
num = months[m-1]

if(isRun(y)):
    summ = num+1+d
    print('今年总计%d天'%(summ))
summ = num+d
print('这是第%d天'%(summ))


#以下为官方真实版验证方式
#!/usr/bin/python
# -*- coding: UTF-8 -*-
  
year = int(raw_input('year:\n'))
month = int(raw_input('month:\n'))
day = int(raw_input('day:\n'))
  
months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 < month <= 12:
    sum = months[month - 1]
else:
    print 'data error'
sum += day
 
leap = 0 #www.iplaypy.com
 
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print 'it is the %dth day.' % sum

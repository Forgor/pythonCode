# Date 2018年10月15号
# 简述：根据一个奖金的取值判断所在范围计算奖金
'''
def cal(I):
    if I <= 10:
       price = I * 0.1
    elif I > 10 and I <= 20:
        price = 10 * 0.1 + (I-10)*0.75
    elif I > 20 and I <= 40:
        price = 10 * 0.1 + 10 * 0.075 + (I-20)*0.05
    elif I > 40 and I <= 60:
        price = 1+0.75+1+(I -40)*0.03
        
    elif I > 60 and I <= 100:
        price = 3.35+(I-60)*0.015
    else:
        price = 3.95+(I-100)*0.01
    return price


I = int(input('Please input a number'))

value = cal(I)

print(value)
'''

#示例代码
# 比较巧妙的是利用一次for循环以及赋值  实现递归调用

i = int(input('净利润：'))
arr = [1000000,600000,400000,200000,100000,0]
rar = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        value = (i - arr[idx])*rar[idx]
        r += value
        print('超出%d部分奖金为%d'%(arr[idx],value))
        i = arr[idx]

print('最后总的奖金为%d'%(r))

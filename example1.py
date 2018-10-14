# Date 2018年10月14号

#简述：有四个数字分别是1,2,3,4 问能组成互不相同且无重复三位数字多少个
#分析：元组构成一个序列  新的元素跟已经有的做一个比较

#跟模板比较的话  逻辑与可以用 and 链接，举例数字可以  print(i,j,z)

a = []
count = 0
for i in range(1,5):
    for j in range(1,5):
        if (i!=j):
            for z in range(1,5):
                if((z!=i)&(z!=j)):
                    b = i*100+j*10+z
                    a.append(b)
                    count=count+1
                else:
                    continue
        else:
            continue

print(count)
print(a)

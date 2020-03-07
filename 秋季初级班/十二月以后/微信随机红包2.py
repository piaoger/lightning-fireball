#简单随机红包算法
import random

s,n = eval(input('随机红包总金额,人数:'))
mList = [1] * n #初始化
cents = int(s*100 - n) #所剩总金额，单位:分

for i in range(n-1):
    r = random.randint(0,int(cents/(n-i)*2))
    mList[i] += r
    cents -= r
mList[n-1] += cents #剩下的钱归最后一个人
for i in range(n):
    print(mList[i]/100) #打印时恢复单位：元


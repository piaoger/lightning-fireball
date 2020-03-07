# REALTHINK LESSON
#简单随机红包算法

import random

s,n = eval(input('total money , people number:'))
mList = [1] * n #没人钱包一分钱
cents = int(s*100 - n)

for i in range(n-1):
    r = random.randint(0,cents)
    mList[i] += r
    cents -= r
mList[n-1] += cents  #剩下的钱全归一个人

for i in range(n):
    print(mList[i]/100)
           
           

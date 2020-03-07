#验证哥德巴赫猜想，函数版

def is_prime(n):
    if n != int(n) or n <2:
       return False
    for  i in range(2,n):
       if n% i ==0:
         return False
    return True
#———
n=eval (input('n='))
for n1 in range (2,n//2+1):
    if is_prime(n1) and is_prime(n-n1):
       print(n1,n-n1)





#找出【ab】区间内最大指数和直属数量统计
    

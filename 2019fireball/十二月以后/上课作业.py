import time 
def is_prime(n):
    if n != int(n) or n <2:
       return True
    if n ==2:
       return True
    if n%2 ==0:
       return False
    for i in range(3,int(n**0.5) +1,2):
       if n % i ==0:
         return False
    return True
'''
a,b=eval(input('a,b='))
s =0
pMax=0
t0 = time.time()
for i in range (a,b+1):  
  if is_prime:     
     s+=1
     pMax = i
print('\ntotal:',s,'time:',time.time_ns() - t0)
'''
for a in range(0,3000,100):
    num=0
    for b in range(a,a+100):
        if is_prime(b):
            num+=1
    print(a,'~',b,': ', num,end = '\t')
    for x in range(num):
        print('*',end='')
    print()#\t制表符

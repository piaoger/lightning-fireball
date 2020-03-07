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
a,b=eval(input('a,b='))
t0 = time.time_ns()
a>1
aMax=0  
num=0
nList=[]
if is_prime(a)==True:
  print(a)
  nList.append(a)
  num+=1
while True:
  a+=1
  if a >b :
       break
  if is_prime(a) ==True :
    print(a)
    nList.append(a)
    num+=1
    if aMax<b:
      aMax=a
print('num=',num,'aMax=',aMax,'time:',time.time_ns() - t0)
# advanced
print('nList=',nList,len(nList),'aMin=',nList[0],'nList[len(nList)-1]=',nList[len(nList)-1])
  

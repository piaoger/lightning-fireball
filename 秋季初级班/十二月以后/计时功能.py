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

n=eval(input('n='))
s =1


t0 = time.time_ns()

for i in range (3,n+1,2):
  is_prime_or_not = is_prime(i)
  
  if is_prime_or_not:
     
     s+=1
     
print('\ntotal:',s,'time:',time.time_ns() - t0)
      

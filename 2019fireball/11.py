from turtle import *
speed(0)
sum_1,sum_2=0,0
def plus_1(a,b):
  s=a+b
  return s

def mu_ti (a,b):
  s=a*b
  return s

def to_1 (a,b):
  s=a-b
  return s

a,b = eval(input('a,b='))

if a>b:
  print(plus_1(a,b))
elif a==b:
  print(mu_ti(a,b))
else:
  print( to_1 (a,b))
  for i in range(900):
     fd(10+i)
     rt(58)
  

  
  



  
 

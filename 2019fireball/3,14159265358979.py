#RT

a,b =eval(input('[a,b]='))
num=0
s=0
n1,n2,n=0,1,1
while n<=b:
    if a<= n:
        num += 1
        s+=n
        print(n)
    n1,n2=n2,n
    n=n1 +n2
print('num=',num)
print('s=',s)

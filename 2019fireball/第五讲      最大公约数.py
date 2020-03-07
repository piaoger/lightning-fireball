a,b = eval(input('a,b='))
for n in range(b,0,-1):
    if a>b:
        a,b=b,a
        if  a%n==0 and b&0==0:
            print(n)
            break

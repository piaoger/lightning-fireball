#RT

a,b =eval(input('a,b='))

c=a%b
while c>0:
    
    print(a,b,c)
    a,b=b,c
    c=a%b

print(b)

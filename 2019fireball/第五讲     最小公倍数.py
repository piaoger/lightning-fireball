a , b = eval (input('a,b='))
if a<b     #make sure a>= b
    a,b = b,a #最小公倍数
for n in range (a,a*b+1,b):
    if n % a == 0 and n % b == 0: 
        print(n)
        break # jump out of the loop

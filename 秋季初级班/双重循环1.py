#x,y LOOPS
n=eval (input('n='))
for y in range (n):
    for x in range (n-1-y):
         print(' ',end = '')
    for x in range (2*y+1):
         print('&',end = '')
    print()
for y in range ( n-2, -1,-1):
    for x in range (n-1-y):
         print(' ',end = '')
    for x in range (2*y+1):
         print('@',end = '')
    print()

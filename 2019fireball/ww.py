# Montecarlo Pi
import random
nz = eval(input('times='))
ns = 0 # times in the sector
for i in range(nz):#nz次试验
     x = random.random() #0~1
     y = random.random()
     if x*x + y*y<1 : #(x,y) in the sector
          ns += 1
print('pi=', 4 * ns/nz)

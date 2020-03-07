# guess number
x,point= eval(input('x,point:'))
t = 10 ** point
bottom,top = 1, x
while True:
     a = (bottom + top) / 2
     print(bottom,top,a)
     if a*a <x:
         bottom=a#bottom go up
     elif a*a>x:
         top =a  #top go down
     else:
          print(a)
          print('Got it')
          break
    
     if int ( bottom * t ) == int ( top * t):
         break
     print(bottom,top,a)
print ( int ( top * t ) / t)

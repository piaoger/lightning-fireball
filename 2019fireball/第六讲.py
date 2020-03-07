# guess number
n= eval (input('range(1~n):'))
bottom,top = 1, n+1
while True:
     a = (bottom + top) // 2
     print(a)
     s = input('< or > or =:')
     if s=='>':
         bottom=a#bottom go up
     elif s == '<':
         top =a  #top go down
     else:
          print('Got it')
          break
          
          

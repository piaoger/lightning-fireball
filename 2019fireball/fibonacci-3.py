
# fibonacci
start_value=eval(input('start_value='))
stop_value = eval(input('stop_value='))

n1 = 0
n2 = 1
n3 = n1 + n2

sum_value = 0

while True:

    n1 = n2
    n2 = n3
    n3 = n1 + n2

    if n3 >= stop_value:
        break

    if n3 >=start_value: 
    
        print(n3, n2/n3)
        sum_value = sum_value + n3
            
print(sum_value)

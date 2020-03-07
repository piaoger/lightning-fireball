
# fibonacci
stop_value = eval(input('stop_value='))

n1 = 0
n2 = 1
n3 = n1 + n2

print(n1)
print(n2)
print(n3)

sum_value = n3

while n3 <= stop_value:
    n1 = n2
    n2 = n3

    
    n3 = n1 + n2
    
    print(n3, n2/n3)
    sum_value = sum_value + n3
            
print(sum_value)

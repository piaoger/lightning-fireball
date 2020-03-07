num= eval(input('num='))
s=0
aMax = 0 #假设当前最高分
aMaxId = 0  
for i in range(num):  #循环num次
    print('No.', i +1)
    a = eval(input('a='))
    s = s + a   #累加
    if aMax < a: #如果这个分更高
        aMax = a #记住这个分
        aMaxId = i #同时记住编号
print('sum=')
print('aug=',s / num)
print('max=' , aMax , 'No.' , aMaxId +1)

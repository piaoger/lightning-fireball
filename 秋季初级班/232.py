# daa
num = eval(input('num='))
s=0
nMIN,nMINId=100,0 
nMAX,nMAXId=0,0
nList = [0] * num
for i in range(num):
    print('No.',i+1)
    nList[i] = eval(input('n='))
    s +=nList[i]
    if nList[i] <nMIN:
        nMIN,nMAXID=nList[i],i
    if nList[i] > nMAX:
        nMAX,nMINID=nList[i],i
    
print('s=',s)
print('MIN=',nMIN)
print('MAX=',nMAX)


    

#
nList = list(eval(input('n[]=')))
aList=[]
for i in range(len(nList)-1):
  aList.append(i+1)
print(nList)
print(aList)
for a in range (len(nList)-1):
  flag=0
  if nList[i] < nList[i+1]:
    nList[i],nList[i+1] = nList[i+1],nList[i]
    flag=1
  print(nList)
  if flag==0:
    break    
print(nList)











  #排序带编号信息

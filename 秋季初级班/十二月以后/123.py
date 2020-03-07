# 0,1,2
nList = list(eval(input('n[]=')))

aList=[]
count = len(nList)-1 #count=3-1
for i in range(count): #[0,1,2]
  aList.append(i+1)
  print(i)

  
print(nList) #[0,1,2]
print(aList) #aList=[1,2]

for i in range (len(nList)):
  flag=0
  
  if nList[i] < nList[i+1]:
    nList[i],nList[i+1] = nList[i+1],nList[i]
    flag=1

  # [2,1,3]
  # [2,3,1]
  #
  print(nList)
  
  if flag==0:
    break

print(nList)

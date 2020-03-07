
def bubble_sort(nList,aList):

  for i in range(len(nList)-1):
    up=False
    # sort sub-list
    for a in range(len(nList)-1-i):
      if nList[a]<nList[a+1]:
        print(a)
        nList[a],nList[a+1]= nList[a+1],nList[a]
        aList[a],aList[a+1]= aList[a+1],aList[a]
        up=True
        
    if up==False:
      break
  return nList,aList
  

nList =list(eval(input('nList=')))
aList=[]
for b in range(len(nList)):
  aList.append(b+1)              
  print('No.',aList[b],'Data.',nList[b])

print("-------before------")
print("aList=", aList)
print("nList=",nList)

print("-------after-------")
bubble_sort(nList,aList)

print(aList)
 

print("nList=",nList)

# expect: aList = [3,1,2], nList=[600,30,1]


#rt 课程 体操积分
s=0
scMax =0 
average=0
scMin,scMinId=10,0
p=0
q=0
scList=[9.8, 9.2, 9.5, 10, 9.4, 10, 9.3, 9.7]
for i in range(len(scList)):
    sc=scList[i]
    s+=sc # add score
    print(sc)
    if scMax < sc:
        scMax = sc
    if scMin > sc:
        scMin = sc
average=s/len(scList)
p=s-scMax-scMin
q=len(scList)-2
scMin,scMinId=sc,i
print("sum", s)
print('average=',average)
print(scMin,scMax)
print('fair average=',int(average *1000 +0.5)/1000)
#ASSIGNMENTS:1求平均分
            #2.去掉一个最高分，最低分以后的平均分
            #3. 定位最低分裁判编号  

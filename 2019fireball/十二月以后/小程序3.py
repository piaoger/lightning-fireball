point = 1
t = 10** point
pList = eval(input('4 poker cards:'))
cList =['+','-','*','/']
aList = []
kList = []

kList.append(['','','','','','']) #0

kList.append(['(','',')','','','']) #1,p:0,2

kList.append(['','(','','',')','']) #2,p:1,4

kList.append(['','','','(','',')']) #3,p:3,5

kList.append(['','(','','','',')']) #4,p:1,5

kList.append(['(','',')','(','',')']) #5,p:0,2,3,5

for p1 in range(4):
    for p2 in range(4):
        if p1 == p2:    
            continue
        for p3 in range(4):
            if p1 == p3 or p2==p3:
               continue
            p4 = 6  - p1 - p2 - p3
            for c1 in range(4):
                for c2 in range(4):
                    for c3 in range(4):
                        for k in kList:
                        #拼合出算式
                            s = k[0] +\
                                str(pList[p1]) + cList[c1] +k[1] + \
                                str(pList[p2]) + k[2] + cList[c2] + k[3]+ \
                                str(pList[p3]) + k[4] + cList[c3] + \
                                str(pList[p4]) + k[5]
                            
                            try: #是否计算出错（除0）
                                if eval(s) == 24 :
                                    print(s)
                                    print(int(eval(s)*t)/t)
                                    break
                            except:
                                
                                pass #pass表示什么也不做

                                

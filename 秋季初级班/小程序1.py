# 24
for p1 in range(4):
    for p2 in range(4):
        if p1 == p2:    #提前剪枝cut
            continue
        for p3 in range(4):
            if p1 == p3 or p2==p3:
               continue
            p4 = 6  - p1 - p2 - p3
            print(p1,p2,p3,p4)

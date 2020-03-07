import random

scoreMax = 0
pWinNum,cWinNum=0,0
PScore,CScore=0,0
for i in range(300):
    print('No.' , i + 1)
    input('go!')
    dice1 = random.randint(1,890)
    dice2 = random.randint(1,890)
    
    score1=dice2+dice1
    
    print('Player\dice1:'  ,dice1,  '\tDice:2' , dice2 ,'\tscore1:' , score1)
    dice3 = random.randint(1,890)
    dice4 = random.randint(1,890)
    
    score2=dice3+dice4
    
    print('CPU\dice3:'  ,dice3 ,'\tDice:4' , dice4 ,'\tscore2:' , score2)

    PScore += score1
    CScore += score2
    if score1 > score2:
        print('you win!')
        pWinNum += 1
    elif score1 < score2:
        cWinNum = cWinNum+1
        print('you lose!')
    else:
        print('tie!')
    print()  #换行
    if pWinNum == 2 or cWinNum ==2:
        break

        
print('final !')        
print('you win!',pWinNum,'CPU win!:' , cWinNum,'tie:' , i + 1 -  pWinNum - cWinNum)
print('Your score:' , PScore ,'Cpu score:' ,  CScore)


#REALTHINK lesson

#太空大逃亡基本版
import pygame,sys,random

SCREEN_W,SCREEN_H = 1000,600 #屏幕尺寸

class CLS_box (object): # box类定义,陨石和飞船都是Box
    def __init__ (self,rect,speed,color = (255,255,255)):
        self.rect = pygame.Rect(rect)
        self.speed=speed
        self.color = color
    def draw (self,screen):
        pygame.draw.rect(screen,self.color,self.rect,0)
    def move(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
def create_box(rectList):#随机产生不重叠的box，并保证不在基地homebox内
    while True:   #随机产生新box，并保证符合要求
        x = random.randint(0,SCREEN_W)
        y = random.randint(0,SCREEN_H)
        w = random.randint(10,40)
        h = random.randint(10,40)
        rect = pygame.Rect(x,y,w,h)
        if (not rect.colliderect(homebox)) and (rect .collidelist(rectList) ==-1):
            break #如果不在homebox内，又不与已有box重叠，符合要求
    while True: #随机产生初始速度
        speed = [random.randint(0,2) -1,random.randint(0,2) -1]
        if speed !=[0,0]:
            break #初始速度不是静止，符合要求
    color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    return CLS_box(rect,speed,color)

#_________pygame________________初始化
pygame.init() #pygame初始化函数
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))#产生窗口对象
pygame.display.set_caption("RT Space")  #窗口名称
clock = pygame.time.Clock()#帧率定时器吃实话
font = pygame.font.Font(None,32)#fontd对象初始化
#_______程序初始化
homebox =  [300,200,200,200]#基地区举行初始化
myBox =CLS_box([380,280,10,10],[0,0],(0,255,0)) #飞船初始化
boxNumber = 300#陨石数量
boxList,rectList = [],[]
for i in range(boxNumber):
    b = create_box(rectList)
    boxList.append(b)
    rectList.append(b.rect)
timeStart = pygame.time.get_ticks()#记录开始时间

#---------------主程序-------------------
while True:#主循环
    for event in pygame.event.get():#时间便利
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.quit()
        if event.type == pygame.KEYDOWN:#如果是按键KEYDOWN事件
              #方向键处理，改变速度
            if event.key == pygame.K_LEFT:
                myBox.speed[0] = -10
            if event.key == pygame.K_RIGHT:
                myBox.speed[0] = 5
            if event.key == pygame.K_UP:
                myBox.speed[1] = -10
            if event.key == pygame.K_DOWN:
                myBox.speed[1] = 5

    screen.fill((0,0,0))#背景重绘为黑色
    myBox.move() #飞船坐标计算
    myBox.draw(screen) #绘制飞船
    for b in boxList: #遍历每个陨石bix
       if b.rect.x>SCREEN_W - b.rect.width  or b.rect.x ==0:
           b.speed[0] = -b.speed[0] #如果这个box水平过节 ， 则x方向转变
       if b.rect.y>SCREEN_H - b.rect.height or b.rect.y ==0:
           b.speed[1] = -b.speed[1] #如果这个box垂直过节 ， 则y方向转变
       for b0 in boxList: #遍历所有其他box
           if b == b0:#如果要比较的 box b0 是其本身 ， 不需要判断碰撞
                continue
            #--------4个方向的碰撞检测---------
           if (abs(b0.rect.bottom - b.rect.top) <=1) and\
                   (b.rect.right >= b.rect.left) and\
                   (b0.rect.right >= b.rect.left):
               b.speed[1] = -b.speed[1]
           if (abs(b0.rect.top - b.rect.bottom) <=1) and\
                   (b.rect.right >= b.rect.left) and\
                   (b0.rect.right >= b.rect.left):
               b.speed[1] = -b.speed[1]
           if (abs(b0.rect.right - b.rect.left) <=1) and\
                   (b.rect.bottom >= b.rect.top) and\
                   (b0.rect.bottom >= b.rect.top):
               b.speed[0] = -b.speed[0]
           if (abs(b0.rect.left - b.rect.right) <=1) and\
                   (b.rect.bottom >= b.rect.top) and\
                   (b0.rect.bottom >= b.rect.top):
               b.speed[0] = -b.speed[0]
       b.move() #box坐标计算
       b.draw(screen) #绘制box
       if myBox.rect.colliderect(b.rect): #判断myBox是否和这个box相碰
            print('score:',(pygame.time.get_ticks() - timeStart) / 1000)
            sys.exit()

    imgText = font.render(str((pygame.time.get_ticks() - timeStart) / 1000),\
              True,(0,0,255))
    screen.blit(imgText,(SCREEN_W -100,0)) #在屏幕右上角绘制当前时间
    pygame.display.update()#屏幕刷新
    clock.tick(25) #帧率可调
                          
        
        
        
        
              
              

        
        
        
        
        
        
    
        
    

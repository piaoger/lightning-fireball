#REALTHINK LESSONS
#PRGAME RGB
import pygame,sys,math
pygame.init()
w,h=800,600
screen = pygame.display.set_mode([w,h])#生成窗口对象
#------draw--------
for a in range(0,10000000,1):
    for y in range(h):
        for x in range(w):
            r = (y/math.cos(x/100))%256
            g = (x*33-y-x*y)%256
            b = (y*y/(x+1)) %256
            if 200**2<(x-400)**2+ (y-300)**2<300**2:
                screen.set_at([x,y],[r,g,b])
        pygame.display.update()
#-----main.loop-----
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
                
        

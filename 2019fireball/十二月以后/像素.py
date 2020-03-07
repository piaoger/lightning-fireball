import sys,pygame

#绘图函数，，对指定像素集pixel，在坐标（x0，y0）以scale大小画图
def RT_draw(screen,pixel,x0,y0,scale):
    color = (pygame.color.THECOLORS['black'],
            pygame.color.THECOLORS['gray32'],
            pygame.color.THECOLORS['gray64'],
            pygame.color.THECOLORS['white'],
            pygame.color.THECOLORS['red'],
            pygame.color.THECOLORS['green'],
            pygame.color.THECOLORS['blue'],
            pygame.color.THECOLORS['orange'],
            pygame.color.THECOLORS['brown'],
            pygame.color.THECOLORS['purple'],
            pygame.color.THECOLORS['yellow'],
            pygame.color.THECOLORS['cyan'],
            pygame.color.THECOLORS['sienna'],
            pygame.color.THECOLORS['chocolate'],
            pygame.color.THECOLORS['coral'],
            pygame.color.THECOLORS['darkgreen'])
    for y in range(len(pixel)): #在高度方面循环
        line=pixel[y]#第y行像素字符串
        for x in range(len(line)): #在宽度方面循环
            if 'A' <=line[x] <='F':
                c = color[ord(line[x])-55]#AF的AC11码产生10，15
            elif '0' <= line[x]<='9':
                c = color[eval(line[x])] #0_9的对应颜色编号0，9
            else:
                continue #透明色
            pygame.draw.rect(screen,c,(x*scale+x0,y*scale+y0,scale,scale),0)
#_________pygame________________初始化
pygame.init() #pygame初始化函数
SCREEN_W,SCREEN_H = 1600,900#产生窗口对象
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
clock = pygame.time.Clock()#帧率定时器初始化
# -----datainit-------
scale=8#显示比例
pixelList = []
# 第1帧像素数据
pixel = []
pixel.append('0000000200000000')
pixel.append('0000002222000000')
pixel.append('0000002322000000')
pixel.append('0000022332200000')
pixel.append('0000003330000000')
pixel.append('0000000300000000')
pixel.append('0000003003030000')
pixel.append('0000303003030000')
pixel.append('0003003003030000')
pixel.append('0000003003030000')
pixel.append('0077712222130000')
pixel.append('0777703003000000')
pixel.append('0777703003000000')
pixel.append('0077003003000000')
pixel.append('0000003003000000')
pixel.append('0000000000000000')
pixelList.append(pixel)

# 第2帧像素数据
pixel = []
pixel.append('0000000000000000')
pixel.append('0000000222000000')
pixel.append('0000002232200000')
pixel.append('0000002233220000')
pixel.append('0000002333000000')
pixel.append('0000000030000000')
pixel.append('0000303003030000')
pixel.append('0000303003030000')
pixel.append('0000303003030000')
pixel.append('0000303003003000')
pixel.append('0000322212100000')
pixel.append('0000003223300000')
pixel.append('0000037770030000')
pixel.append('0000307777003000')
pixel.append('0000007770003000')
pixel.append('0000000000000000')
pixelList.append(pixel)

# 第3帧像素数据
pixel = []
pixel.append('0000000000000000')
pixel.append('0000000222000000')
pixel.append('0000002232200000')
pixel.append('0000002233220000')
pixel.append('0000002333000000')
pixel.append('0000000030000000')
pixel.append('0000303003030000')
pixel.append('0000303003030000')
pixel.append('0000303003030000')
pixel.append('0000303003003000')
pixel.append('0000322222000300')
pixel.append('0000033033700000')
pixel.append('0000300773700000')
pixel.append('0003000777370000')
pixel.append('0000000077300000')
pixel.append('0000000000000000')
pixelList.append(pixel)

# 第4帧像素数据
pixel = []
pixel.append('0000000000000000')
pixel.append('0000000222000000')
pixel.append('0000002232200000')
pixel.append('0000002233220000')
pixel.append('0000002333000000')
pixel.append('0000000030000000')
pixel.append('0000303003030000')
pixel.append('0000303003030000')
pixel.append('0000003003030000')
pixel.append('0003033002003000')
pixel.append('0003322222207700')
pixel.append('0000003033077700')
pixel.append('0000030003077770')
pixel.append('0003000000307770')
pixel.append('0000000000300000')
pixel.append('0000000000000000')
pixelList.append(pixel)
#---------2--------
pixelList2 = []
# 第1帧像素数据
pixel = []
pixel.append('000000CCCC000000')
pixel.append('000000CCCC000000')
pixel.append('0000CCCCCCCC0000')
pixel.append('00000CCCCCC00000')
pixel.append('00000DDDDDD00000')
pixel.append('00000DDD03000000')
pixel.append('000000DD33000000')
pixel.append('0000000330000000')
pixel.append('0000000CC0000000')
pixel.append('000000C22C000000')
pixel.append('000000C22C000000')
pixel.append('000000C22C000000')
pixel.append('000000C33C000000')
pixel.append('000000CCCC000000')
pixel.append('400000CCCC000000')
pixel.append('4400000330000000')
pixelList2.append(pixel)

# 第2帧像素数据
pixel = []
pixel.append('000000CCCC000000')
pixel.append('000000CCCC000000')
pixel.append('0000CCCCCCCC0000')
pixel.append('00000CCCCCC00000')
pixel.append('00000DDDDDD00000')
pixel.append('00000DD030D00000')
pixel.append('000000D333000000')
pixel.append('0000000330000000')
pixel.append('0000000CC0000000')
pixel.append('000000022C000000')
pixel.append('00000022CC200000')
pixel.append('0000033CCC330000')
pixel.append('0000000CCCC00000')
pixel.append('400000CC00CC0000')
pixel.append('44000CC000330000')
pixel.append('4440033000000000')
pixelList2.append(pixel)

# 第3帧像素数据
pixel = []
pixel.append('000000CCCC000000')
pixel.append('000000CCCC000000')
pixel.append('0000CCCCCCCC0000')
pixel.append('00000CCCCCC00000')
pixel.append('00000DDDDDD00000')
pixel.append('00000D030DD00000')
pixel.append('000000333D000000')
pixel.append('0000000330000000')
pixel.append('0000000CC0000000')
pixel.append('000000C22C000000')
pixel.append('000000C22C000000')
pixel.append('000000C22C000000')
pixel.append('400000C33C000000')
pixel.append('440000CCCC000000')
pixel.append('444000CCCC000000')
pixel.append('4444000330000000')
pixelList2.append(pixel)

# 第4帧像素数据
pixel = []
pixel.append('000000CCCC000000')
pixel.append('000000CCCC000000')
pixel.append('0000CCCCCCCC0000')
pixel.append('00000CCCCCC00000')
pixel.append('00000DDDDDD00000')
pixel.append('00000DD030D00000')
pixel.append('000000D333000000')
pixel.append('0000000330000000')
pixel.append('0000000CC0000000')
pixel.append('000000022C000000')
pixel.append('00000022CC200000')
pixel.append('4000033CCC330000')
pixel.append('440000CCCC000000')
pixel.append('44400CC00CC00000')
pixel.append('4444033000CC0000')
pixel.append('4444400000330000')
pixelList2.append(pixel)

#------------------------
pixelList3 = []
# 第1帧像素数据
pixel = []
pixel.append('0000000000000000')
pixel.append('0000000000000000')
pixel.append('0000000040000000')
pixel.append('0000000444000000')
pixel.append('0000000AAA000000')
pixel.append('0000222AA0000000')
pixel.append('000022011A000000')
pixel.append('0222201111220000')
pixel.append('0220001110007700')
pixel.append('0000001110077770')
pixel.append('0011111011077770')
pixel.append('0111000011007700')
pixel.append('0111000011000000')
pixel.append('1100000011000000')
pixel.append('0000000011000000')
pixel.append('0000000000000000')
pixelList3.append(pixel)

# 第2帧像素数据
pixel = []
pixel.append('0000000000000000')
pixel.append('0000000000000000')
pixel.append('0000000440000000')
pixel.append('0000000444000000')
pixel.append('0000000AAA000000')
pixel.append('0000002AA0000000')
pixel.append('0000002112000000')
pixel.append('0000022112000000')
pixel.append('0002222110222000')
pixel.append('0002000110770000')
pixel.append('0000001117777000')
pixel.append('0000001107777000')
pixel.append('0000111100770000')
pixel.append('0001110001100000')
pixel.append('0001000001100000')
pixel.append('0000000001100000')
pixelList3.append(pixel)

# 第3帧像素数据
pixel = []
pixel.append('0000000000000000')
pixel.append('0000000040000000')
pixel.append('0000000040000000')
pixel.append('0000000444000000')
pixel.append('0000000AAA000000')
pixel.append('0000000AAA000000')
pixel.append('0000022220220000')
pixel.append('0000220122202000')
pixel.append('0002200077002000')
pixel.append('0000001777722000')
pixel.append('0000011777720000')
pixel.append('0000110077000000')
pixel.append('0000110000110000')
pixel.append('0000110000110000')
pixel.append('0000110000110000')
pixel.append('0000000000000000')
pixelList3.append(pixel)

# 第4帧像素数据
pixel = []
pixel.append('0000000000000000')
pixel.append('0000000400000000')
pixel.append('0000000040000000')
pixel.append('0000000444000000')
pixel.append('0000000AAA000000')
pixel.append('000220AAA0000000')
pixel.append('0770222A22000000')
pixel.append('7777200112222200')
pixel.append('7777001100000200')
pixel.append('0770001111000000')
pixel.append('0000111001100000')
pixel.append('0001110000110000')
pixel.append('0001100000110000')
pixel.append('0001000000011000')
pixel.append('0011000000000000')
pixel.append('0000000000000000')
pixelList3.append(pixel)
#--------------------------------------------------
pixelList4 = []
# 第1帧像素数据
pixel = []
pixel.append('0000000000000000')
pixel.append('0440000000000000')
pixel.append('0040000000000000')
pixel.append('0044000000000000')
pixel.append('0004000000000000')
pixel.append('0011100000000000')
pixel.append('7777777777717000')
pixel.append('7777777777771000')
pixel.append('7777777777717000')
pixel.append('00CC000CC0000000')
pixel.append('0C01C0C01C000000')
pixel.append('0C10C0C10C000000')
pixel.append('00CC000CC0000000')
pixel.append('0000000000000000')
pixel.append('0000000000000000')
pixel.append('0000000000000000')
pixelList4.append(pixel)

# 第2帧像素数据
pixel = []
pixel.append('0000000000000000')
pixel.append('0000000000000000')
pixel.append('0000000000000000')
pixel.append('0444000000000000')
pixel.append('0004000000000000')
pixel.append('0011100000000000')
pixel.append('7777777777717000')
pixel.append('7777777777771000')
pixel.append('7777777777717000')
pixel.append('00CC000CC0000000')
pixel.append('0C10C0C10C000000')
pixel.append('0C01C0C01C000000')
pixel.append('00CC000CC0000000')
pixel.append('0000000000000000')
pixel.append('0000000000000000')
pixel.append('0000000000000000')
pixelList4.append(pixel)

# 第3帧像素数据
pixel = []
pixel.append('0000000000000000')
pixel.append('0000000000000000')
pixel.append('0000000000000000')
pixel.append('0000000000000000')
pixel.append('0004000000000000')
pixel.append('0011100000000000')
pixel.append('7777777777717000')
pixel.append('7777777777771400')
pixel.append('7777777777717000')
pixel.append('00CC000CC0000000')
pixel.append('0C01C0C01C000000')
pixel.append('0C10C0C10C000000')
pixel.append('00CC000CC0000000')
pixel.append('0000000000000000')
pixel.append('0000000000000000')
pixel.append('0000000000000000')
pixelList4.append(pixel)

# 第4帧像素数据
pixel = []
pixel.append('0000000000000000')
pixel.append('0000000000000000')
pixel.append('0000000000000000')
pixel.append('0000000000000000')
pixel.append('0000000000000000')
pixel.append('0011100000000000')
pixel.append('7777777777717000')
pixel.append('7777777777771044')
pixel.append('7777777777717000')
pixel.append('00CC000CC0000000')
pixel.append('0C10C0C10C000000')
pixel.append('0C01C0C01C000000')
pixel.append('00CC000CC0000000')
pixel.append('0000000000000000')
pixel.append('0000000000000000')
pixel.append('0000000000000000')
pixelList4.append(pixel)

pixelList5 = []
# 第1帧像素数据
pixel = []
pixel.append('BBB99BBBB99BBBBB')
pixel.append('BBB99BBBB99BBBBB')
pixel.append('BBB11111111BB6BB')
pixel.append('BBB14411441B666B')
pixel.append('BBB11222211B666B')
pixel.append('BBBB12AA21B66666')
pixel.append('BBBB122221BBB6BB')
pixel.append('BBBB111114BBB6BB')
pixel.append('BBB44666644446BB')
pixel.append('BB44B6666B4446BB')
pixel.append('B444B6666BBB46BB')
pixel.append('44BBB6BB6BBBBBBB')
pixel.append('BBBB66BBB66BBBBB')
pixel.append('BBB66BBBBB6BBBFF')
pixel.append('5555555555F55F5F')
pixel.append('FFFF55555FFFFFFF')
pixelList5.append(pixel)

# 第2帧像素数据
pixel = []
pixel.append('BBBBBBBBBBBBBBBB')
pixel.append('BB6BBBBB4BBBBBBB')
pixel.append('BB6BBBB4BBBBBBBB')
pixel.append('BB6BBB44BBBBBBBB')
pixel.append('BB6BB44BBB111199')
pixel.append('BBB6B4BBBB144199')
pixel.append('BBBB66666111110B')
pixel.append('BBBBB666611A110B')
pixel.append('BBBB66466111110B')
pixel.append('BBBB6446BB144199')
pixel.append('BBBB644BBB111199')
pixel.append('BBB66B44BBBBBBBB')
pixel.append('8B66BBB44BBBBBBB')
pixel.append('86BBBBBBB4BBBBBB')
pixel.append('8888888888888888')
pixel.append('8888888888888888')
pixelList5.append(pixel)

# 第3帧像素数据
pixel = []
pixel.append('BBBB44BBBBBBBBBB')
pixel.append('6BBB4411111BBBBB')
pixel.append('6BBBB414111BBBBB')
pixel.append('B66BB414111BBBBB')
pixel.append('BB664411141BBBBB')
pixel.append('BBB64444111BBBBB')
pixel.append('BBB666444BBBBABB')
pixel.append('BBBB66BB44BBAAAB')
pixel.append('BBBB6BBB44AAAAAA')
pixel.append('BBB66BBBAAAAAAAB')
pixel.append('BB66BBBBBBBBAABB')
pixel.append('BBBBBBBBBBBBBBBB')
pixel.append('BBBBBBBBB11BBBBB')
pixel.append('BBBBBBBB1111BBBB')
pixel.append('BBBBBBBB1111BBBB')
pixel.append('5555555555555555')
pixelList5.append(pixel)

# 第4帧像素数据
pixel = []
pixel.append('BBBBBBBBBBBAAAAB')
pixel.append('BBBBBBBBBBBA44AB')
pixel.append('BBBBBBBBBBBA44AB')
pixel.append('BBBBBBBBBBBAAAAB')
pixel.append('BBBBBBBBBBBBBBBB')
pixel.append('BBBBBBBBBBBBBBBB')
pixel.append('BBBBBBBBBBBBBBBB')
pixel.append('BBBBBB5BB55BB5BB')
pixel.append('BBBBBBB5B55B5BBB')
pixel.append('BBBBBBBB5555BBBB')
pixel.append('BBBBBB6BEEE5BBBB')
pixel.append('BBA6666BE555666B')
pixel.append('BBA6666FFE55566B')
pixel.append('BB6446666666446B')
pixel.append('BBB44BBBBBBB44BB')
pixel.append('BBBBBBBBBBBBBBBB')
pixelList5.append(pixel)





x,y=0,0
spdX,spdY = 0,0
counter=0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill( (0,0,0) )#背景重绘为黑色
    RT_draw(screen,pixelList[counter//16%4],x,y,scale)#绘制动画
    RT_draw(screen,pixelList2[counter//16%4],x+16*scale,y,scale)
    RT_draw(screen,pixelList3[counter//16%4],x+16*scale*2,y+1,scale)
    RT_draw(screen,pixelList4[counter//16%4],x+16*scale*3,y+2,scale)
    RT_draw(screen,pixelList5[counter//32%4],x+16*scale*4,y+3,scale)
    counter+=1
    x += spdX
    y += spdY
    if x <0 or x>SCREEN_W:
        spdX *= -1
    if y <0 or y>SCREEN_H:
        spdY *= -1
    
    pygame.display.update()#屏幕刷新
    clock.tick(100) #帧率可调
    

            
             
           

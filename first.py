import pygame as pg
##初始化
from mysprites import *

enemy=gamesprites("./materials/敌机.png")

enemy_group=pg.sprite.Group(enemy)#敌机精灵族


pg.init()
screen=pg.display.set_mode((480,700))
back=pg.image.load("./materials/背景1.jpg")
back1=pg.transform.scale(back,(480,700))
screen.blit(back1,(0,0))
pg.display.update()

myplane0=pg.image.load("./materials/飞机.png")
myplane1=pg.transform.scale(myplane0,(100,100))
# screen.blit(myplane,(200,500))
pg.display.update()
#游戏开始
clock=pg.time.Clock()
myplane_rec=pg.Rect(150,500,50,50)
while True:
    clock.tick(60)
    myplane_rec.y-=1
    if myplane_rec.y<=-50:
        myplane_rec.y=500
    screen.blit(back1, (0, 0))
    screen.blit(myplane1,myplane_rec)
    pg.display.update()

    # enemy_group.update()
    enemy_group.draw(screen)
    enemy_group.update()
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()

    pass
pg.quit()

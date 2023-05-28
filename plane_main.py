

import pygame as pg
from mysprites import *

class planegame:
    def __init__(self):
        self.screen=pg.display.set_mode(SCREEN_RECT.size)

        self.clock=pg.time.Clock()

        self.create_sprites()

        pg.time.set_timer(ENEMY_EVENT,900)
        # pg.time.set_timer(HERO_FIRE_EVENT,500)
    def startgame(self):

     while True:
        #设置刷新帧率
        self.clock.tick(PER_SEC)
        #事件监听
        self.event_handler()
        #碰撞检测
        self.check_collide()
        #更新和绘制精灵族
        self.update_sprites()
        # 更新显示
        pg.display.update()

    def event_handler(self):
        for event in pg.event.get():
            if event.type==pg.QUIT:
                self.game_over()

            elif event.type==ENEMY_EVENT:
                ene=enemy()
                self.enemy_group.add(ene)

            # elif event.type==HERO_FIRE_EVENT:
            #     self.plane.fire()
        keys_pressed=pg.key.get_pressed()
        if keys_pressed[pg.K_RIGHT]:
            self.plane.speed=2
        elif keys_pressed[pg.K_LEFT]:
            self.plane.speed=-2
        elif keys_pressed[pg.K_UP]:
            self.plane.speedy=-2
        elif keys_pressed[pg.K_DOWN]:
            self.plane.speedy=2
        elif keys_pressed[pg.K_SPACE]:
            self.plane.fire()
        else:
            self.plane.speedy=0
            self.plane.speed=0

    def check_collide(self):
        pg.sprite.groupcollide(self.plane.bullets,self.enemy_group,1,1)

       # pg.sprite.spritecollideany(self.plane,self.enemy_group)
        if pg.sprite.spritecollideany(self.plane,self.enemy_group):
            self.plane.blood-=1
            print('%d'%(self.plane.blood))
    def create_sprites(self):
        #创建背景精灵和精灵组
        bg1=background()
        bg2 = background(1)
        bg2.rect.y=-bg2.rect.height
        self.backgroup=pg.sprite.Group(bg1,bg2)
        # 创建敌机精灵组
        self.enemy_group=pg.sprite.Group()
        #创建飞机精灵和精灵组
        self.plane=plane()
        self.plane_group=pg.sprite.Group(self.plane)

        # self.plane.bullets.update()
        # self.plane.bullets.draw(self.screen)

    def update_sprites(self):
        self.backgroup.update()
        self.backgroup.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.plane_group.update()
        self.plane_group.draw(self.screen)

        self.plane.bullets.update()
        self.plane.bullets.draw(self.screen)

    @staticmethod
    def game_over():
        print("游戏结束啦")
        pg.quit()
        exit()
if __name__ == '__main__':
    game=planegame()

    game.startgame()


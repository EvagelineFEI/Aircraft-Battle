import random
import pygame as pg
SCREEN_RECT=pg.Rect(0,0,480,700)

PER_SEC=60


#创建敌机的定时器常量
ENEMY_EVENT=pg.USEREVENT
HERO_FIRE_EVENT = pg.USEREVENT+1
class gamesprites(pg.sprite.Sprite):

    def __init__(self,imagename,speed=1):
        super().__init__()
        self.image=pg.image.load(imagename)
        if imagename=="./materials/敌机.png":
            self.image = pg.transform.scale(self.image, (80, 80))
        elif imagename=="./materials/原子弹.png":
            self.image = pg.transform.scale(self.image, (20,20))
        self.rect=self.image.get_rect()
        self.speed=speed

    def update(self):
        self.rect.y+=self.speed


class background(gamesprites):
    def __init__(self,is_alt=False):
        super().__init__("./materials/背景1.jpg")

        if is_alt:
            self.rect.y=-self.rect.height

class enemy(gamesprites):
    def __init__(self):
        super().__init__("./materials/敌机.png")
        #设置敌机的初始随机速度和位置
        self.speed=random.randint(1,2)

        max_x=SCREEN_RECT.width-self.rect.width
        self.rect.x=random.randint(0,max_x)
        self.rect.bottom=0
    def update(self):
        super().update()
        if self.rect.y>=SCREEN_RECT.height:
           self.kill()


    def __del__(self):
        print("敌机飞出屏幕了\n")


class plane(gamesprites):
    def __init__(self):
       super().__init__("./materials/飞机.png",0)
       self.rect.y=SCREEN_RECT.bottom-190
       self.rect.centerx=SCREEN_RECT.centerx
       self.speedy=0

       self.blood=3
       self.bullets=pg.sprite.Group()


    def update(self):
       self.rect.x+=self.speed
       if self.rect.x<0:
           self.rect.x=0
       elif self.rect.right>SCREEN_RECT.right:
           self.rect.right= SCREEN_RECT.right
       self.rect.y+=self.speedy

    def fire(self):
        print("发射子弹")
        zidan=bullet()
        zidan.rect.bottom=self.rect.y-20
        zidan.rect.centerx=self.rect.centerx
        self.bullets.add(zidan)

class bullet(gamesprites):
    def __init__(self):
      super().__init__("./materials/原子弹.png",-2)

    def update(self):
      super().update()

      if self.rect.bottom<0:
          self.kill()



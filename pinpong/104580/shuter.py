#Создай собственный Шутер!
from pygame import *
from random import randint
from time import time as timer
mixer.init()
last_time = timer()
num_fire = 0
rec_time = False
life = 3
win_w = 800
win_h = 600
class GameSprite(sprite.Sprite):
    def __init__(self,p_im,p_x,p_y,p_s,p_h,p_w):
        super().__init__()
        self.image =transform.scale(image.load(p_im),(p_h,p_w))
        self.speed = p_s
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 20:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_w - 80:
            self.rect.x += self.speed
    def fire(self):
        kick = mixer.Sound("fire.ogg")
        kick.play()
        bullet = Bullet("knife.png",self.rect.centerx-10,self.rect.top,-10,50,50)
        Bullets.add(bullet)
class Bullet(GameSprite):
    def update(self):
        self.rect.y+=self.speed
        if self.rect.y<0:
            self.kill

class Enemy(GameSprite):
    def update(self):
        self.rect.y+=self.speed
        global lost
        if self.rect.y>500:
            #self.kill()
            self.rect.y = 0
            self.rect.x = randint(10,620)
            lost = lost +1



window = display.set_mode((win_w,win_h))
display.set_caption("Шутер")
color = (255, 236, 51)
window.fill(color)
#background = transform.scale(image.load("Столовая_(The_Skeld)2.png"),(800,600))
hero = Player("among_cr1.png",5 ,530 ,4,60,60)
monsters = sprite.Group()
Bullets = sprite.Group()
for i in range (3):
    monster = Enemy("among_imp.png",randint(10,620),0,randint(1,3),50,50)
    monsters.add(monster)
    monster2 = Enemy("among_cr2.png",randint(10,620),0,randint(1,3),70,70)
    monsters.add(monster2)
    monster3 = Enemy("among_cr3.png",randint(10,620),0,randint(1,3),50,50)
    monsters.add(monster3)
font.init()
font1 = font.SysFont("Arial",36)   
clock = time.Clock()
fps = 60
finish = False
game = True
lost = 0
score = 0
start = True
win_im = transform.scale(image.load("win_im.jpg"),(800,600))
lose_im = transform.scale(image.load("lose_im.jpeg"),(800,600))
last_time2 = timer()
while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_w:
                if num_fire<10 and rec_time == False:
                    num_fire +=1
                    hero.fire()
                elif num_fire>=10 and rec_time == False:
                    last_time = timer()
                    rec_time = True
    if start == True:
        now_time2 = timer()
        #window.blit(background,(0,0))
        text_int = font1.render("У тебя 3 жизни, выжывай,и да это нападание crewmatов",5,(255,255,255))
        window.blit(text_int,(100,300))
        display.update()
        if now_time2 - last_time2 >= 2:
            #time.delay(9000)
            start = False

    if finish != True and start !=True:
        #window.blit(background,(0,0))
        window.fill
        hero.update()
        hero.reset()
        text_lose  = font1.render("Членов экипажов не убито"+str(lost),1,(255,255,255))
        text_score = font1.render("Членов экипажов убито"+str(score),1,(255,255,255))
        window.blit(text_lose,(10,30))
        window.blit(text_score,(30,50))
        monsters.draw(window)
        monsters.update()
        Bullets.draw(window)
        Bullets.update()
        if rec_time ==True:
            now_time = timer()
            if now_time - last_time>1.5:
                num_fire =0
                rec_time = False
            else:
                print('work!')
                text_reload = font1.render("Перезарядка",1,(255,0,0))
                window.blit(text_reload,(50,70))

        if sprite.spritecollide(hero,monsters,True):
            life -=1
            monster = Enemy("among_imp.png",randint(10,620),0,randint(1,2),50,50)
            monsters.add(monster)
            monster2 = Enemy("among_cr2.png",randint(10,620),0,randint(1,2),70,70)
            monsters.add(monster2)
            monster3 = Enemy("among_cr3.png",randint(10,620),0,randint(1,2),50,50)
            monsters.add(monster3)

        if life == 0 or lost>70:
            finish = True
            window.blit(lose_im,(0,0))

        if score>=150:
            finish = True
            window.blit(win_im,(0,0))
        collides = sprite.groupcollide(monsters,Bullets,True,True)
        for coll in collides:
            score+=1
            if score%2 == 0:
                monster = Enemy("among_imp.png",randint(10,620),0,randint(1,3),50,50)
                monsters.add(monster)
                monster2 = Enemy("among_cr2.png",randint(10,620),0,randint(1,3),70,70)
                monsters.add(monster2)
                monster3 = Enemy("among_cr3.png",randint(10,620),0,randint(1,3),50,50)
                monsters.add(monster3)
    display.update()
    clock.tick(fps)
from pygame import *
from random import randint
#init()
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
    def updatel(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y > 20:
            self.rect.y -= self.speed
        if keys[K_UP] and self.rect.y < 500:
            self.rect.y += self.speed
    def updater(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y > 20:
            self.rect.y -= self.speed
        if keys[K_w] and self.rect.y < 500:
            self.rect.y += self.speed
window = display.set_mode((win_w,win_h))
color = (255, 236, 51)
window.fill(color)
finish = False
start = True
game = True
clock = time.Clock()
fps = 60
p1 = Player("Knife.png",5 ,290 ,4,90,300)
p2 = Player("Knife2.png",250 ,150 ,4,90,300)
while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill(color)
    p1.reset()
    p2.reset()
    p1.updatel()
    p2.updater()
    display.update()
    clock.tick(fps)
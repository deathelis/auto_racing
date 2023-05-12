from pygame import *
from time import sleep
from random import *


#создай игру "Лабиринт"!
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Шутер")
background = transform.scale(
    image.load("road.png"),
    (win_width, win_height)
)
mixer.init()
mixer.music.load("sfonk.ogg")
mixer.music.play()
kick = mixer.Sound("end.ogg")


seconds_left = 100
score = 0
game = True
finish = False
clock = time.Clock()
FPS = 60
score1 = 0
goal = 10
lost = 0
max_lost = 3
gray = (176, 176, 176)

font.init()
font = font.Font(None, 70)
win = font.render('Победа', True, (220, 20, 60))
lose = font.render("Проигрыш", True, (220, 20, 60))




class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        #if keys[K_UP] and self.rect.y < win_height:
            #self.rect.y -= self.speed
        #if keys[K_DOWN] and self.rect.y < win_height - 80:
            #self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = choice(rund)
            self.rect.y = 0
            lost = lost + 1

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def go(self):
        self.rect.y += 1
        if self.rect.y > win_height + 80:
            self.rect.x = 172
            self.rect.y = -140

    def goo(self):
        self.rect.y += 1
        if self.rect.y > win_height + 80:
            self.rect.x = 522
            self.rect.y = -140



rund = [50, 230, 410, 580]
car = Player("car.png", 300, win_height - 150, 80, 140, 4)
monsters = sprite.Group()
for i in range(1, 4):
    monster = Enemy("car1.png", choice(rund), -40, 80, 160, 3)
    monsters.add(monster)
w1 = Wall(176, 176, 176, 172, 100, 7, 80)
w2 = Wall(176, 176, 176, 172, 240, 7, 80)
w3 = Wall(176, 176, 176, 172, 380, 7, 80)
w4 = Wall(176, 176, 176, 172, -40, 7, 80)
w5 = Wall(176, 176, 176, 172, -180, 7, 80)

w6 = Wall(176, 176, 176, 522, 100, 7, 80)
w7 = Wall(176, 176, 176, 522, 240, 7, 80)
w8 = Wall(176, 176, 176, 522, 380, 7, 80)
w9 = Wall(176, 176, 176, 522, -40, 7, 80)
w10 = Wall(176, 176, 176, 522, -180, 7, 80)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background,(0,0))
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w1.go()
        w2.go()
        w3.go()
        w4.go()
        w5.go()
        w6.goo()
        w7.goo()
        w8.goo()
        w9.goo()
        w10.goo()
        sleep(0.01)
        car.update()
        monsters.update()
        car.reset()
        monsters.draw(window)
        score = font.render('Счёт:' + str(lost), True, (220, 20, 60))
        window.blit(score, (10, 50))
        if sprite.spritecollide(car, monsters, False):
            mixer.music.pause()
            kick.play()
            finish = True 



        display.update()
    clock.tick(FPS)
       
       



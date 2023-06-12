#Создай собственный Шутер!

from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self, b_1, b_2):
        keys = key.get_pressed()
        if keys[b_1] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[b_2] and self.rect.y < 625:
            self.rect.y += self.speed

win = display.set_mode((700,500))
background = transform.scale(image.load("background.jpg"), (700, 500))
display.set_caption('Ping pong')
clock = time.Clock()
FPS = 60

win_1 = transform.scale("win1.jpg",(700,500))
win_2 = transform.scale("win2.jpg",(700,500))

player_1 = Player("platform.png", 10, 300, 3)
player_2 = Player("platform.png", 550, 300, 3)

ball = GameSprite("ball.png", 200, 200, 3)

speed_x = 3
speed_y = 3

game = True

finish = False

while game:
    win.blit(background, (0,0))
    
    player_1.reset()
    player_1.update(K_w, K_s)
    
    player_2.reset()
    player_2.update(K_UP, K_DOWN)
    
    ball.reset()
    
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    
    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(player_1, ball) or sprite.collide_rect(player_2, ball):
        speed_x *= -1

    if ball.rect.x < 0:
        finish = True
        win.blit(win_2, (0,0))
    if ball.rect.x > 650:
        finish = True
        win.blit(win_1, (0,0))

    clock.tick(FPS)
    display.update()
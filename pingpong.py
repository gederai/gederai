from pygame import *
'''Required Classes'''

#Fonts
font.init()
Font = font.SysFont("Arial", 35)
Lose1 = Font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
Lose2 = Font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

#FPS
clock = time.Clock()
FPS = 60



#Parent class
class GameSprites(sprite.Sprite):
        #class constructor
   def __init__(self, player_image, player_x, player_y, player_size_x, player_size_y, player_speed):
       sprite.Sprite.__init__(self)
       #every sprite must store the image property
       self.image = transform.scale(image.load(player_image), (player_size_x, player_size_y))
       self.speed = player_speed
       #every sprite must have the rect property – the rectangle it is fitted in
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

   
   def reset(self):
       windows.blit(self.image, (self.rect.x, self.rect.y))


class player(GameSprites): #A command to control the rackets
    def update1(self): #Racket/Player 1
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < Win_W - 80:
            self.rect.y += self.speed

    def update2(self): #Racket/Player 2
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < Win_W - 80:
            self.rect.y += self.speed



#Game Scene
back = (0, 128, 0)
Win_W = 600
Win_H = 500
windows = display.set_mode((Win_W, Win_H))
display.set_caption("Ping-Pong")
windows.fill(back)

speed_x = 3
speed_y = 3 

racket1 = player('racket.png', 30, 200, 20, 52, 15)
racket2 = player('racket.png', 532, 200, 20, 52, 15)
ball = GameSprites('tenis_ball.png', 5, Win_H - 100, 15, 15, 15)

Game = True
Finish = False

while Game:
    for e in event.get():
        if e.type == QUIT:
            Game = False

    if not Finish:
        
        windows.fill(back)
        racket1.update1()
        racket2.update2()

        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > Win_H - 50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            Finish = True
            windows.blit(Lose1, (180, 200))
            game_over = True

        if ball.rect.x > Win_W:
            Finish = True
            windows.blit(Lose2, (180, 200))
            game_over = True

        racket1.reset()
        racket2.reset()
        ball.reset()


    display.update()
    clock.tick(FPS)
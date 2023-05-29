from pygame import *
import time as timmy

class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale( image.load(player_image), (70,70))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)

    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y <= 430:
            self.rect.y += self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y <= 430:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, speed_x, speed_y):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update_ball(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y


window = display.set_mode((700, 500))
display.set_caption("Супер мега крутая игра 2к23")

background = transform.scale(image.load("list.jpg"), (700, 500))

sprite_1 = Player(("player1.png"), 0, 420, 10)
sprite_2 = Player(("player2.png"), 627, 420, 10)
ball = Ball(("ball.png"), 330, 200, 3, 3, 3)

clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None, 20)

lost1 = 0
lost2 = 0

game = True
finish = False

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False 

    if finish != True:
        window.blit(background,(0, 0))
        sprite_1.reset()
        sprite_2.reset()
        ball.reset()
        sprite_1.update_l()
        sprite_2.update_r()
        ball.update_ball()

        text_blue = font.render("всего побед:"+ str(lost1), True, (0, 82, 245))
        window.blit(text_blue, (0, 450))
        text_red = font.render("всего побед:"+str(lost2), True, (245, 0, 24))
        window.blit(text_red, (570, 450))

        if ball.rect.y >= 450 or ball.rect.y <= 0:
            ball.speed_y *= -1 

        if sprite.collide_rect(ball, sprite_1) or sprite.collide_rect(ball, sprite_2):
            ball.speed_x *= -1

        if ball.rect.x <= 0:
            # timmy.sleep(2)
            ball = Ball("ball.png", 330, 200, 3, 3, 3)
            lost2 += 1

            for i in range(1):
                if lost1 >= 5 or lost2 >= 5:
                    ball.speed_x = 5
                    ball.speed_y = 5

        if ball.rect.x >= 640:
            # timmy.sleep(2)
            ball = Ball("ball.png", 330, 200, 3, 3, 3)
            lost1 += 1

            for i in range(1):
                if lost1 >= 5 or lost2 >= 5:
                    ball.speed_x = 5
                    ball.speed_y = 5

        if lost1 >= 10:
            text_27 = font.render("ПРОИГРАЛ КРАСНЫЙ ИГРОК ... :(", True, (0, 82, 245))
            window.blit(text_27, (20, 20))
            finish = True

        if lost2 >= 10:
            text_72 = font.render("ПРОИГРАЛ СИНИЙ ИГРОК ... :(", True, (245, 0, 24))
            window.blit(text_72, (20, 20))
            finish = True

        clock.tick(FPS)
        display.update()
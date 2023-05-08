from pygame import *

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
        if keys_pressed[K_w]: #and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s]: #and self.rect.y < 650:
            self.rect.y += self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP]: #and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN]: #and self.rect.y < 650:
            self.rect.y += self.speed


window = display.set_mode((700, 500))
display.set_caption("Супер мега крутая игра 2к23")

background = transform.scale(image.load("list.jpg"), (700, 500))

sprite_11 = transform.scale( image.load("player1.png"), (10,200))
sprite_22 = transform.scale( image.load("player2.png"), (10,100))
sprite_1 = Player(("player1.png"), 0, 420, 10)
sprite_2 = Player(("player2.png"), 635, 420, 10)
ball = Player(("ball.png"), 150, 200, 3)

clock = time.Clock()
FPS = 60

speed_x = 3
speed_y = 3

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

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y >= 450 or ball.rect.y <= 0:
            speed_y *= -1 

        if sprite.collide_rect(ball, sprite_1) or sprite.collide_rect(ball, sprite_2):
            speed_x *= -1

        clock.tick(FPS)
        display.update()
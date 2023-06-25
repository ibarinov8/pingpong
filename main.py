from pygame import *
from random import randint

SPRITE_RESOLUTION = (100, 100)

class GameSprite(sprite.Sprite):
    def __init__(self, filename, speed, x, y, resolution = SPRITE_RESOLUTION):
        super().__init__()
        self.image = transform.scale(image.load(filename), resolution)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):

        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 615:
            self.rect.y += self.speed

    def update_r(self):

        keys = key.get_pressed()

        if keys[K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.x < 1175:
            self.rect.x += self.speed

class Ball(GameSprite):
    def __init__(self, filename, speed, x, y, resolution = SPRITE_RESOLUTION):
        super().__init__(filename, speed, x, y, resolution)
        self.speed_x = speed
        self.speed_y = speed


    def update():
        # if (self.rect.x > 5 and self.rect.x < 1175):
        #     self.rect.x *= -1
        if (self.rect.y > 5 and self.rect.y < 615):
            self.rect.y *= -1

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y



RESOLUTION = (1280, 720)
window = pygame.display.set_mode(RESOLUTION)
window.fill((255, 255, 255))
# системный таймер для работы pygame
# clock = pygame.time.Clock()

player_1 = Player('racket.png', 0, 310, 5, (20, 100))
player_2 = Player('racket.png', 1270, 310, 5, (20, 100))

ball = Ball('ball.png', 550, 310, 5)

FPS = 60
clock = time.Clock()
clock.tick(FPS)

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()

    if not finish:
        # window.blit(background, (0, 0))
        window.fill((250, 250, 250))

        player_1.reset()
        player_2.reset()
        ball.reset()


        player.update_l()
        player.update_r()
        ball.update()

        if ball.colliderect(player_1.rect() or ball.colliderect(player_2.rect)):
            ball.speed_x * -1


    display.update()

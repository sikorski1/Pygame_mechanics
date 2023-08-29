import pygame
from sys import exit

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Space_ship.png")
        self.rect = self.image.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
    def create_bullet(self):
        return Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load("laser.png")
        self.rect = self.image.get_rect(center = (x_pos, y_pos))
    def update(self):
        self.rect.x += 3
        if self.rect.x >= SCREEN_WIDTH + 200:
            self.kill()
pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bullet")

player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

bullet_group = pygame.sprite.Group()

pygame.mouse.set_visible(False)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet_group.add(player.create_bullet())
    screen.fill("Dark Grey")
    bullet_group.draw(screen)
    player_group.draw(screen)
    player_group.update()
    bullet_group.update()
    clock.tick(120)
    pygame.display.update()

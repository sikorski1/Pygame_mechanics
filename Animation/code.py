import pygame
from sys import exit

class Player(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        for i in range(4, 16):
            self.sprites.append(pygame.image.load("graphics/frog_tongue_animationx{}.png".format(i)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect =  self.image.get_rect(center = (x_pos, y_pos))
    def play_animation(self):
        self.is_animating = True
    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.1
            if 2 <= self.current_sprite:
                self.current_sprite += 0.2
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            self.image = self.sprites[int(self.current_sprite)]


pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Animation")

moving_sprites = pygame.sprite.Group()
player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            player.play_animation()

    screen.fill("Light Blue")

    moving_sprites.draw(screen)
    moving_sprites.update()
    clock.tick(60)
    pygame.display.update()

import pygame, random
from sys import exit


class CrossHair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("graphics/crosshair.png")
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("audio/laser_shooting_sfx.wav")
        self.gunshot.set_volume(0.10)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)

class Target(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load("graphics/target.png")
        self.rect = self.image.get_rect(center = (x_pos, y_pos))
class GameState:
    def __init__(self):
        self.state = "intro"
    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = "main_game"
        screen.blit(bg, (0, 0))
        crosshair_group.draw(screen)
        crosshair_group.update()
        pygame.display.update()
    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                crosshair.shoot()
        screen.blit(bg, (0, 0))
        target_group.draw(screen)
        crosshair_group.draw(screen)
        crosshair_group.update()
        pygame.display.update()
    def state_manager(self):
        if self.state == "main_game":
            self.main_game()
        if self.state == "intro":
            self.intro()

pygame.init()
clock = pygame.time.Clock()
game_state = GameState()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shooter")
bg = pygame.image.load("graphics/bg.png")

crosshair = CrossHair()
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)
pygame.mouse.set_visible(False)

target_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target(random.randrange(0, SCREEN_WIDTH), random.randrange(0, SCREEN_HEIGHT))
    target_group.add(new_target)


while True:
    game_state.state_manager()
    clock.tick(120)

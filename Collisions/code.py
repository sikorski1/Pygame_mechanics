import pygame
from sys import exit

def bouncing_rect():
    global first_x_speed, first_y_speed, second_x_speed, second_y_speed
    first_rect.x += first_x_speed
    first_rect.y += first_y_speed

    if first_rect.right >= SCREEN_WIDTH or first_rect.left <= 0:
        first_x_speed *= -1
    if first_rect.bottom >= SCREEN_HEIGHT or first_rect.top <= 0:
        first_y_speed *= -1

    second_rect.y += second_y_speed
    if second_rect.top <= 0 or second_rect.bottom >= SCREEN_HEIGHT:
        second_y_speed *= -1

    if first_rect.colliderect(second_rect):
        if abs(second_rect.top - first_rect.bottom) < 10 and first_y_speed > 0:
            first_y_speed *= -1
        if abs(second_rect.bottom - first_rect.top) < 10 and first_y_speed < 0:
            first_y_speed *= -1
        if abs(second_rect.right - first_rect.left) < 10 and first_x_speed < 0:
            first_x_speed *= -1
        if abs(second_rect.left - first_rect.right) < 10 and first_x_speed > 0:
            first_x_speed *= -1
    if first_rect.bottom > SCREEN_HEIGHT:
            first_rect.y = SCREEN_HEIGHT - first_rect.height
    if first_rect.top < 0:
            first_rect.y = 0
    pygame.draw.rect(screen, "Red", first_rect)
    pygame.draw.rect(screen, "Orange", second_rect)


pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Collision")

first_rect = pygame.Rect(100, 100, 200, 100)
first_x_speed, first_y_speed = 5, 4

second_rect = pygame.Rect(400, 400, 150, 150)
second_x_speed, second_y_speed = 2, 2
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill("Light Green")

    bouncing_rect()
    clock.tick(120)
    pygame.display.update()
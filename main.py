import pygame
import random

pygame.init()

window = pygame.display.set_mode([400, 715])
pygame.display.set_caption("Space mission")

SPACESHIP = pygame.image.load('spaceship.png')
BACKGROUND = pygame.image.load('stars.jpg')
MISSILE = pygame.image.load('missile.png')

CREATE_ASTEROID = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ASTEROID, 250)

missile_coord = []

spaceship_top = 100
spaceship_left = 100

spaceship_left_change = 0
spaceship_top_change = 0

while True:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                spaceship_left = random.randint(0, 400 - 64)
                spaceship_top = random.randint(0, 800 - 64)

            if event.key == pygame.K_a:
                spaceship_left_change = -0.3
                spaceship_top_change = 0

            if event.key == pygame.K_d:
                spaceship_left_change = 0.3
                spaceship_top_change = 0

            if event.key == pygame.K_s:
                spaceship_left_change = 0
                spaceship_top_change = 0.3

            if event.key == pygame.K_w:
                spaceship_left_change = 0
                spaceship_top_change = -0.3

            if event.key == pygame.K_f:
                missile_left =  spaceship_left + (MISSILE.get_width() / 2)
                missile_top = spaceship_top + MISSILE.get_height()

                missile_coord.append([missile_left, missile_top])

    if spaceship_left < 0 or spaceship_left > 336:
        spaceship_left_change = -spaceship_left_change

    if spaceship_top < 0 or spaceship_top > 651:
        spaceship_top_change = -spaceship_top_change

    spaceship_top += spaceship_top_change
    spaceship_left += spaceship_left_change

    window.blit(BACKGROUND, [0, 0])
    window.blit(SPACESHIP, [spaceship_left, spaceship_top])

    for coord in missile_coord:
        coord[1] -= 0.5
        window.blit(MISSILE, coord)
        
        if coord[1] < (0 - MISSILE.get_height()):
            missile_coord.remove(coord)


    pygame.display.update()
import pygame
import random

pygame.init()

window = pygame.display.set_mode([400, 715])
pygame.display.set_caption("Space mission")

SPACESHIP = pygame.image.load('spaceship.png')
BACKGROUND = pygame.image.load('stars.jpg')
MISSILE = pygame.image.load('missile.png')
ASTEROID = pygame.image.load('asteroid.png')

CREATE_ASTEROID = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ASTEROID, 215)

missile_coord = []
asteroid_coord = []

spaceship_top = 100
spaceship_left = 100

spaceship_left_change = 0
spaceship_top_change = 0

while True:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            
        if event.type == CREATE_ASTEROID:
            asteroid_left = random.randint(20, 400)
            asteroid_top = random.randint(-100, -30)
            asteroid_coord.append([asteroid_left, asteroid_top])
            
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

            if event.key == pygame.K_f or event.key == pygame.K_e:
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
            
    for asteroid in asteroid_coord:
        asteroid[1] += 0.4
        window.blit(ASTEROID, asteroid)
        
        if asteroid[1] > 720:
            asteroid_coord.remove(asteroid)
            
        asteroid_rect = ASTEROID.get_rect()
        missiles_rect = MISSILE.get_rect()
        
        asteroid_rect.topleft = asteroid
        
        for missile in missile_coord:
            missiles_rect.topleft = missile
            
            if asteroid_rect.colliderect(missiles_rect):
                asteroid_coord.remove(asteroid)
                missile_coord.remove(missile)

    pygame.display.update()
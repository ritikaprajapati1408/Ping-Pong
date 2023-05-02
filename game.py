import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800,600))
background = pygame.image.load('background.png')
pygame.display.set_caption('Alien Killer')
icon = pygame.image.load('ufo.png')

playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480 
playerX_change = 0

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480 
bulletX_change = 0
bulletY_change = 480 
bullet_state = 'ready'

def player(x, y):
    screen.blit(playerImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))

running = True
while running :
    screen.fill((0,0,0))
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletSound = mixer.Sound('laser.wav')
                    bulletSound.play()

                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

        playerX += playerX_change
        if playerX <= 0:
            playerX = 0

        elif playerX >= 736:
            playerX = 736

        if bulletY <= 0:
            bulletY = 480
            bullet_state = 'ready'

        if bullet_state is "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change


    player(playerX, playerY)
    pygame.display.update()
import math
import random
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_STARTING_X = 370
PLAYER_STARTING_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 40
COLLISION_DISTANCE = 27

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bg = pygame.image.load("elliptical-galaxy-purple-.jpg")
pygame.display.set_caption("Space Invader v0")
icon = pygame.image.load('uf.png')
pygame.display.set_icon(icon)

#Da player stuff

playerimg = pygame.image.load('player.png')
playerx = PLAYER_STARTING_X
playery = PLAYER_STARTING_Y
playerx_change = 0

#DA ENEMY STUFF

enemyimg = []
enemyx = []
enemyy = []
enemyXchange = []
enemyYchange = []
num_of_enemies = 6
for _i in range (num_of_enemies):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyy.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyXchange.append(ENEMY_SPEED_X)
    enemyYchange.append(ENEMY_SPEED_Y)

#Da Bullet stuff

bulletimg = pygame.image.load('bullet.png')
bullet_X = 0
bullet_Y = PLAYER_STARTING_Y
bullet_change_x = 0
bullet_speed = BULLET_SPEED_Y
bullet_state = "ready"

#Da scoring stuff

scoreval = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

#IMAGINE IF YOU GET THIS
over_font = pygame.font.Font('freesansbold.ttf', 64)

def showscoreval(x, y):
    score = font.render('Score: ' + str(scoreval), True, (255, 255, 255))
    screen.blit(score, (x,y))

def game_over_text(): #YOU ARE SO TUFF IF YOU GET THIS
    over_text = over_font.render("GAME OVER (YOURE SO TUFF)", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerimg, (x,y))

def enemy(x, y, i):
    screen.blit(enemyimg[i], (x,y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))
def Collisondetected(enemyx,enemyy,bullet_X,bullet_Y):
    distance = math.sqrt((enemyx-bullet_X) **2 + (enemyy - bullet_Y) **2 )
    return distance < COLLISION_DISTANCE
running = True

while running:
    screen.fill((0,0,0))
    screen.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                playerx_change = -5
            
            if event.key == pygame.K_RIGHT:
                playerx_change = 5
            
            if event.key == pygame.K_SPACE and bullet_state == "ready":
              bullet_X = playerx
              fire_bullet(bullet_X, bullet_Y)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
          playerx_change = 0   
    
    playerx += playerx_change
    playerx = max(0, min(playerx, SCREEN_WIDTH - 64))  
   
    for i in range(num_of_enemies):
        if enemyy[i]>340:
            for j in range(num_of_enemies):
                enemyy[j] = 2000
            game_over_text()
            break
        enemyx[i] += enemyXchange[i]
        if enemyx[i] <= 0 or enemyx[i] >= SCREEN_WIDTH - 64:
            enemyXchange[i] = -1
            enemyy[i] += enemyYchange[i]

        if Collisondetected(enemyx[i],enemyy[i],bullet_X,bullet_Y):
            bullet_Y = PLAYER_STARTING_Y
            bullet_state = "ready"
            scoreval += 1
            enemyx[i] = random.randint(0, SCREEN_WIDTH - 64)
            enemyy[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)
        enemy(enemyx[i], enemyy[i], i)
    
    if bullet_Y <= 0:
        bullet_Y = PLAYER_STARTING_Y
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bullet_X, bullet_Y)
        bullet_Y -= BULLET_SPEED_Y
    player(playerx,playery)
    showscoreval(textX, textY)
    pygame.display.update()

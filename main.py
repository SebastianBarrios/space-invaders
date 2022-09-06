#import requeired lybrari
import pygame
import random
import math

#sounds
from pygame import  mixer 

#intialize pygame
pygame. init()

#window size
screen_width = 600
screen_height = 800

#variables
size = (screen_height, screen_width)
icon = pygame.image.load("86580.png")
player_img = pygame.image.load("space-ship.png")
player_x = 370
player_y = 480
player_change_x = 0
player_change_y = 0

#score varable
score = 0
score_font = pygame.font.Font("score font.ttf", 32)

#text position in screen
text_x = 10
text_y = 10

#game over font
go_font = pygame.font.Font("game over font.ttf", 64)
go_x = 250
go_y = 250


#enemy
enemy_img = []
enemy_x = []
enemy_y = []
enemy_change_x = []
enemy_change_y = []

#numbers of enemys
number_enemys = 10

#create multiple enemys
for item in range(number_enemys):

    

    enemy_img.append(pygame.image.load("enemy-space-ship.png"))
    enemy_x.append(random.randint(0, 748))
    enemy_y.append(random.randint(50, 150))
    enemy_change_x.append(3)
    enemy_change_y.append(20)

#wallpaper
wallpaper_img = pygame.image.load("NPc96f.jpg")

#bacground music
mixer.music.load("daylight.wav")
mixer.music.play(-1)

#player laser
player_laser = pygame.image.load("laser.png")
player_laser_y = 430
player_laser_x = 0
player_laser_change_y = 50
player_laser_state = "ready"

#score
score = 0

game_over_img = pygame.image.load("game-over.png")

#funcion player
def player(x, y):
    screen.blit(player_img, (x, y))

#funcion enemy
def enemy(x, y, item):
    screen.blit(enemy_img[item], (x, y))

#funcion game over
def game_over(x, y):
    go_text = go_font.render("Game Over", True, (255, 255, 255))
    screen.blit(go_text, (x, y))

#score funcion
def show_text(x, y):
    score_text = score_font.render("Score:" + str(score), True, (255, 255, 255))
    screen.blit(score_text, (x, y))

#funcion fire
def fire(x, y):
    global player_laser_state
    player_laser_state = "fired"
    screen.blit(player_laser, (x, y +10))

#collision funcion
def is_collision(enemy_x, enemy_y, player_laser_x, player_laser_y):
    distance = math.sqrt((enemy_x - player_laser_x)**2 + (enemy_y - player_laser_y)**2)
    if distance <= 27:
        return True
    else:
        return False



pygame.display.set_caption("Space Wars")
pygame.display.set_icon(icon)

#game loop
running = True
while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#funcion presionar tecla
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change_x = -4

            if event.key == pygame.K_RIGHT:
                player_change_x = 4

            if event.key == pygame.K_SPACE:
                if player_laser_state == "ready":

                    #bullet sound
                    bullet_sound = mixer.Sound("blaster.wav")
                    bullet_sound.set_volume(0.1)
                    bullet_sound.play()


                    player_laser_x = player_x
                    fire(player_laser_x, player_laser_y)

#funcion soltar tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_change_x = 0



    #color rgb
    screen = pygame.display.set_mode(size)
    rgb = (0, 9, 54)
    screen.fill(rgb)

    #show image
    screen.blit(wallpaper_img, (0,0))

#incrementar valor de x
    player_x += player_change_x
#paredes juego
    if player_x <= 0:
        player_x = 750
    elif player_x >= 750:
        player_x = 0


#enemy mmovement
    for item in range (number_enemys):
        #game over zone
        if enemy_y[item] > 440:
            for j in range (number_enemys):
                enemy_y[j] = 2000
                
            game_over(go_x, go_y)

            break

        enemy_x[item] += enemy_change_x[item]
        if enemy_x[item] <= 0:
            enemy_change_x[item] = 3
            enemy_y[item] += enemy_change_y[item]
        elif enemy_x[item] >= 750:
            enemy_change_x[item] = -3
            enemy_y[item] += enemy_change_y[item]

        enemy(enemy_x[item], enemy_y[item], item)
        #call collision funcion
        collision = is_collision(enemy_x[item], enemy_y[item], player_laser_x, player_laser_y)

        if collision == True:
            player_laser_y = 480
            player_laser_state = "ready"
            score += 10
            print(score)
            enemy_x[item] = random.randint(0, 750)
            enemy_y[item] = random.randint(0, 150) 
            enemy_dies_sound = mixer.Sound("explosion.wav")
            enemy_dies_sound.set_volume(0.3)
            enemy_dies_sound.play()

#laser movement
    if player_laser_y <= 0:
        player_laser_y = 480
        player_laser_state = "ready"



    if player_laser_state == "fired":
        fire(player_laser_x, player_laser_y)
        player_laser_y -= player_laser_change_y


    


 

    player(player_x, player_y)

    show_text(text_x, text_y)

    #update window
    pygame.display.update()
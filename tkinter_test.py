import pygame
import time
import random
 
pygame.init()


display_width=450
display_height=450

bg = pygame.image.load("/Users/charlieshang/Documents/GitHub/PADProject/background.png")
screen = pygame.display.set_mode((display_width,display_height))
screen.blit(bg,(0,0))

pygame.display.set_caption("AREA 51")

icon_left = pygame.image.load("/Users/charlieshang/Documents/GitHub/PADProject/pixel_left.png")

clock = pygame.time.Clock()

def alien(alien_x, alien_y):
    alien_icon = pygame.image.load("/Users/charlieshang/Documents/GitHub/PADProject/alien.png")
    screen.blit(alien_icon,(alien_x,alien_y))

def image(icon,x,y):
    screen.blit(icon,(x,y))

def game_loop_pokemon():

    x_change=0
    y_change=0
    x_icon=175
    y_icon=175
    die = False

    while not die:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.KEYUP:
                x_change = 0
                y_change = 0

        
        x_icon+=x_change
        y_icon+=y_change
        screen.fill((255,255,255))
        image(x_icon,y_icon)
        pygame.display.update()
        clock.tick(60)

def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()
    
    time.sleep(2)
    game_loop_pacman()

def fall():
    message_display("You Fell Down")

def game_loop_pacman():

    x_change=0
    x_icon=175
    y_icon=350

    alien_startx = random.randrange(0, display_width-100)
    alien_starty = -200
    alien_speed = 7

    die = False

    while not die:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                x_change = 0
        
        x_icon+=x_change

        screen.blit(bg,(0,0))
        alien(alien_startx, alien_starty)
        alien_starty += alien_speed
        image(icon_left,x_icon,y_icon)

        if x_icon == 0 or x_icon == display_width-100:
            fall()
            die = True

        if alien_starty > display_height:
            alien_starty = -200
            alien_startx = random.randrange(0,display_width-100)
        
        pygame.display.update()
        clock.tick(60)



game_loop_pacman()
pygame.quit()
quit()
import pygame
import time
import random

pygame.init()


display_width = 700
display_height = 1200

# bg = pygame.image.load("../resource/...png") # need edition
screen = pygame.display.set_mode((display_width,display_height))
# screen.blit(bg,(0,0))
screen.fill((156,156,156))

pygame.display.set_caption("Charlie's mini game")

# icon_left = pygame.image.load("/Users/charlieshang/Documents/GitHub/PADProject/pixel_left.png") # need edition
me_length = 20
me = pygame.Surface((me_length,me_length))
me.fill((140,200,13))

clock = pygame.time.Clock()

# def alien(alien_x, alien_y):
#     alien_icon = pygame.image.load("/Users/charlieshang/Documents/GitHub/PADProject/alien.png") # need edition
#     screen.blit(alien_icon,(alien_x,alien_y))

# def image(icon,x,y):
#     screen.blit(icon,(x,y))

enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer,1500)

class Bullet:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.b = pygame.Surface((7,12))
    
    def move(self):
        self.y -= 5

class Enemy:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.e = pygame.Surface((30,30))
    
    def move(self):
        self.y += 7

def game_loop():

    x_change = 0
    y_change = 0
    x = display_width / 2
    y = display_height - 20
    fail = False
    bullets = []
    enemies = []

    while not fail:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == enemy_timer:
                e_x = random.randint(0,display_width-30)
                e_y = 0
                e = Enemy(e_x,e_y)
                enemies.append(e)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    b = Bullet(x+3.5,y-12)
                    bullets.append(b)

            if event.type == pygame.KEYUP:
                x_change = 0
                y_change = 0

        keys_pressed = pygame.key.get_pressed()
        
        if keys_pressed[pygame.K_RIGHT]:
            x_change = 5
        if keys_pressed[pygame.K_LEFT]:
            x_change = -5
        if keys_pressed[pygame.K_UP]:
            y_change = -5
        if keys_pressed[pygame.K_DOWN]:
            y_change = 5
        
        # if keys_pressed[pygame.K_SPACE]:
        #     b = Bullet(x+3.5,y-12)
        #     bullets.append(b)

        x += x_change
        y += y_change

        if x <= 0:
            x = 0
        if (x+me_length) >= display_width:
            x = display_width - me_length
        if(y <= 0):
            y = 0
        if (y+me_length) >= display_height:
            y = display_height - me_length

        screen.fill((156,156,156))
        screen.blit(me,(x,y))

        for bullet in bullets:
            if bullet != None:
                bullet.move()
                screen.blit(bullet.b,(bullet.x,bullet.y))
                if bullet.y <= 0:
                    bullet = None

        for enemy in enemies:
            if enemy != None:
                enemy.move()
                screen.blit(enemy.e,(enemy.x,enemy.y))
                if enemy.y >= display_height:
                    enemy = None
        
        for bullet in bullets:
            for enemy in enemies:
                if bullet != None and enemy != None:
                    if (((bullet.x >= enemy.x and bullet.x <= enemy.x+30) or 
                        (bullet.x+7 >= enemy.x and bullet.x+7 <= enemy.x+30)) and
                        ((bullet.y <= enemy.y+30 and bullet.y >= enemy.y) or 
                        (bullet.y+12 >= enemy.y and bullet.y+12 <= enemy.y+30))):
                        bullet = None
                        enemy = None

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

def fall():
    message_display("You Fell Down")


game_loop()
pygame.quit()
quit()
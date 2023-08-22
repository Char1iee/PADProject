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


score = 0

clock = pygame.time.Clock()

# def alien(alien_x, alien_y):
#     alien_icon = pygame.image.load("/Users/charlieshang/Documents/GitHub/PADProject/alien.png") # need edition
#     screen.blit(alien_icon,(alien_x,alien_y))

# def image(icon,x,y):
#     screen.blit(icon,(x,y))

enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer,1000) # frequency of enemy generation = 1 enemy per 1000ms

class Character:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.me = pygame.Surface((20,20))
        self.me.fill((140,200,13))
        self.x_speed = 0
        self.y_speed = 0

    def move(self,instruction):
        self.x += self.x_speed
        self.y += self.y_speed

    def check_border(self):
        if self.x <= 0:
            self.x = 0
        if (self.x+20) >= display_width:
            x = display_width - 20
        if(self.y <= 0):
            self.y = 0
        if (self.y+20) >= display_height:
            self.y = display_height - 20


# probably enemy does not need check collision but bullet and character do
# the logic is that enemy does not need to care if they hit something because they have highest priority
# but bullet needs to check if it hits enemy and character needs to check if it hits enemy


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

    def check_collision(self,object):
        collide = False
        if isinstance(object,Character):
            if ((object.x >= self.x and object.x <= self.x+30 or 
                object.x+20 >= self.x and object.x+20 <= self.x+30) and
                (object.y <= self.y+30 and object.y >= self.y or
                object.y+20 >= self.y and object.y+20 <= self.y+30)):
                collide = True
        else:
            if ((object.x >= self.x and object.x <= self.x+30 or 
                object.x+7 >= self.x and object.x+7 <= self.x+30) and
                (object.y <= self.y+30 and object.y >= self.y or
                object.y+12 >= self.y and object.y+12 <= self.y+30)):
                collide = True

        return collide

class Enemy2: # enemy with larger size and faster speed
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.e = pygame.Surface((50,50))
    
    def move(self):
        self.y += 10

    def check_collision(self,object):
        collide = False
        if ((object.x >= self.x and object.x <= self.x+50 or 
            object.x+20 >= self.x and object.x+20 <= self.x+50) and
            (object.y <= self.y+50 and object.y >= self.y or
            object.y+20 >= self.y and object.y+20 <= self.y+50)):
            collide = True
        return collide

class Enemy3: # enemy with smaller size and faster speed
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.e = pygame.Surface((20,20))
    
    def move(self):
        self.y += 13

    def check_collision(self,object):
        collide = False
        if ((object.x >= self.x and object.x <= self.x+30 or 
            object.x+20 >= self.x and object.x+20 <= self.x+30) and
            (object.y <= self.y+30 and object.y >= self.y or
            object.y+20 >= self.y and object.y+20 <= self.y+30)):
            collide = True
        return collide

def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

def message_display(text,size,x,y): # displace text center at x,y, not leftmost
    largeText = pygame.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (int(x/2),int(y/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.flip()

    # time.sleep(2)


def game_loop():
    global score

    x_change = 0
    y_change = 0
    x = int(display_width / 2)
    y = display_height - 20 # default height of the character
    me = Character(x,y)

    fail = False
    bullets = []
    enemies = []
    enemy_type  = 0
    
    while not fail:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == enemy_timer:
                if score < 20:
                    e_x = random.randint(0,display_width-30)
                    e_y = 0
                    e = Enemy(e_x,e_y)
                    enemies.append(e)
                elif score < 30:
                    enemy_type = random.randint(0,2)
                    if enemy_type == 0:
                        e_x = random.randint(0,display_width-30)
                        e_y = 0
                        e = Enemy(e_x,e_y)
                        enemies.append(e)
                    else:
                        e_x = random.randint(0,display_width-30)
                        e_y = 0
                        e = Enemy2(e_x,e_y)
                        enemies.append(e)
                else:
                    enemy_type = random.randint(0,3)
                    if enemy_type == 0:
                        e_x = random.randint(0,display_width-30)
                        e_y = 0
                        e = Enemy(e_x,e_y)
                        enemies.append(e)
                    elif enemy_type == 1:
                        e_x = random.randint(0,display_width-30)
                        e_y = 0
                        e = Enemy2(e_x,e_y)
                        enemies.append(e)
                    else:
                        e_x = random.randint(0,display_width-30)
                        e_y = 0
                        e = Enemy3(e_x,e_y)
                        enemies.append(e)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    b = Bullet(x+3,y-12)
                    bullets.append(b)

            if event.type == pygame.KEYUP:
                me.x_speed = 0
                me.y_speed = 0

        keys_pressed = pygame.key.get_pressed()
        
        if keys_pressed[pygame.K_RIGHT]:
            me.x_speed = 5
        if keys_pressed[pygame.K_LEFT]:
            me.x_speed = -5
        if keys_pressed[pygame.K_UP]:
            me.y_speed = -5
        if keys_pressed[pygame.K_DOWN]:
            me.y_speed = 5
        
        # if keys_pressed[pygame.K_SPACE]:
        #     b = Bullet(x+3.5,y-12)
        #     bullets.append(b)

        me.move()
        me.check_border()
        

        screen.fill((156,156,156))
        screen.blit(me,(x,y))

        for bullet in bullets:
            if bullet != None:
                bullet.move()
                screen.blit(bullet.b,(bullet.x,bullet.y))
                # if bullet.y <= 0:
                #     bullets.remove(bullet)

        for enemy in enemies:
            if enemy != None:
                enemy.move()
                screen.blit(enemy.e,(enemy.x,enemy.y))
                # if enemy.y >= display_height:
                #     enemies.remove(enemy)
                if ((x >= enemy.x and x <= enemy.x+30 or 
                        x+20 >= enemy.x and x+20 <= enemy.x+30) and
                        (y <= enemy.y+30 and y >= enemy.y or
                        y+20 >= enemy.y and y+20 <= enemy.y+30)):
                            fail = True
                            lose()
        
        for bullet in bullets:
            for enemy in enemies:
                if bullet != None and enemy != None:
                    if (((bullet.x >= enemy.x and bullet.x <= enemy.x+30) or 
                        (bullet.x+7 >= enemy.x and bullet.x+7 <= enemy.x+30)) and
                        ((bullet.y <= enemy.y+30 and bullet.y >= enemy.y) or 
                        (bullet.y+12 >= enemy.y and bullet.y+12 <= enemy.y+30))):
                        bullets.remove(bullet)
                        enemies.remove(enemy)
                        score += 1
        
        message_display("score: " + str(score),30,120,30)

        pygame.display.flip()
        clock.tick(80)



def lose():
    message_display("You Failed",50,700,1000)


game_loop()
pygame.quit()
quit()
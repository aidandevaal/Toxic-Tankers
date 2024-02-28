import pygame 
import os
import time
import random
pygame.init()                                           #LOTS OF DEFINITIONS (settings)
lives=3
vel=3
win = pygame.display.set_mode((700, 480))
w = 500
h = 373
k = 100
l = 373
bg = pygame.image.load('play.png')
pygame.display.set_caption("Toxic Tankers") 
clock = pygame.time.Clock()
walkRight = [pygame.image.load('pubg.png'), ('pubgr')]
walkLeft = [pygame.image.load('pubg2.png'), ('pubg2l')]
score = 0 
time = 0
seconds = 0
respawn = False
isJump = False                                  #END OF DEFINITIONS (in form of settings)

class player(object):                                           #Player setup
        def __init__(self,x,y,width,height):
                self.x = w
                self.y = h
                self.width = width
                self.height = height
                self.vel = 5
                self.isJump = False
                self.left = False
                self.right = False
                self.walkCount = 0
                self.jumpCount = 10
                self.standing = True
                self.hitbox = (self.x + 17, self.y + 11, 29, 52)

        def draw(self, win):                            #How far the character can walk (boundaries)
                if self.walkCount + 1 >= 27:
                        self.walkCount = 0
                
                if not(self.standing):
                        if self.left:
                                win.blit(walkLeft[self.walkCount//4000], (self.x,self.y))
                                self.walkCount += 1
                        elif self.right:
                                win.blit(walkRight[self.walkCount//4000], (self.x,self.y))
                                self.walkCount +=1
                else:
                        if self.right:
                                win.blit(walkRight[0], (self.x, self.y))
                        else:
                                win.blit(walkLeft[0], (self.x, self.y))
                self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        
        def hit(self):                                  #What happens when the player gets hit
                self.isJump = False
                self.jumpCount = 10
                self.x = 100
                self.y = 410
                self.walkCount = 0
                font1 = pygame.font.SysFont('comicsans', 100)
                text = font1.render('-1 LIFE', 1, (255,0,0))
                win.blit(text, (250 - (text.get_width()/2),200))
                pygame.display.update()
                i = 0
                while i < 200:
                        pygame.time.delay(10)
                        i += 1
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        i = 201
                                        pygame.quit()


class projectiles(object): #SHOTS, SHOTS, SHOTS, SHOTS, SHOTS, SHOTS, EVERYBODY (bullets)                                      
        def __init__(self,x,y,radius,color,facing):
                self.x = x
                self.y = y
                self.radius = radius
                self.color = color
                self.facing = facing
                self.vel = 8 * facing

        def draw(self,win):                             #Shape of bullets
                pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

class enemy(object):                     #Enemy setup
        win.blit(pygame.image.load('Sprite 1.png'), (k, l))
        walkRight = [pygame.image.load('Sprite 2.png')]
        walkLeft = [pygame.image.load('Sprite 1.png')]
        def __init__(self, x, y, width, height, end):
                self.x = k
                self.y = l
                self.width = width
                self.height = height                                    #ADD MULTIPLE ENEMY CLASSES FOR WORKING HEALTH BARS
                self.end = end
                self.path = [self.x, self.end]
                self.walkCount = 0
                self.vel = 3
                self.hitbox = (self.x + 17, self.y + 2, 31, 57)
                self.lives = 4
                self.visible = True

        def draw(self,win):                     #Zombie1 boundaries/increased move speed/hitbox
                self.move()
                if self.visible:
                        if self.walkCount + 1 >= 33:
                                self.walkCount = 0

                        if self.vel > 0:
                                win.blit(self.walkRight[self.walkCount //4000], (self.x, self.y))
                                self.walkCount += 1
                        else:
                                win.blit(self.walkLeft[self.walkCount //4000], (self.x, self.y))
                                self.walkCount += 1

                        pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 25, 10))
                        pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 25 - (5 * (5 - self.lives)), 10))
                        self.hitbox = (self.x + 17, self.y + 2, 31, 57)


        def move(self):                 #How the enemies move on their own
                if self.vel > 0:
                        if self.x + self.vel < self.path[1]:
                                self.x += self.vel
                        else:
                                self.vel = self.vel * -1
                                self.walkCount = 0
                else:
                        if self.x - self.vel > self.path[0]:
                                self.x += self.vel
                        else:
                                self.vel = self.vel * -1
                                self.walkCount = 0

        def hit(self):                          #Hit detection for each zombie
                if self.lives > 0:
                        self.lives -= 1
                else:
                        zombie.x = 699
                        self.lives = 4
                print('hit')

class enemy2(object):                     #Enemy setup
        win.blit(pygame.image.load('Sprite 1.png'), (k, l))
        walkRight = [pygame.image.load('Sprite 2.png')]
        walkLeft = [pygame.image.load('Sprite 1.png')]
        def __init__(self, x, y, width, height, end):
                self.x = k
                self.y = l
                self.width = width
                self.height = height                                    #ADD MULTIPLE ENEMY CLASSES FOR WORKING HEALTH BARS
                self.end = end
                self.path = [self.x, self.end]
                self.walkCount = 0
                self.vel = 3
                self.hitbox2 = (self.x + 17, self.y + 2, 31, 57)
                self.lives2 = 4
                self.visible = True

        def draw2(self,win):                     #Zombie2 boundaries/increased move speed/hitbox
                self.move2()
                if self.visible:
                        if self.walkCount + 1 >= 33:
                                self.walkCount = 0

                        if self.vel > 0:
                                win.blit(self.walkRight[self.walkCount //4000], (self.x, self.y))
                                self.walkCount += 1
                        else:
                                win.blit(self.walkLeft[self.walkCount //4000], (self.x, self.y))
                                self.walkCount += 1

                        pygame.draw.rect(win, (255,0,0), (self.hitbox2[0], self.hitbox2[1] - 20, 25, 10))
                        pygame.draw.rect(win, (0,128,0), (self.hitbox2[0], self.hitbox2[1] - 20, 25 - (5 * (5 - self.lives2)), 10))
                        self.hitbox2 = (self.x + 17, self.y + 2, 31, 57)

        def move2(self):                 #How the enemies move on their own
                if self.vel > 0:
                        if self.x + self.vel < self.path[1]:
                                self.x += self.vel
                        else:
                                self.vel = self.vel * -1
                                self.walkCount = 0
                else:
                        if self.x - self.vel > self.path[0]:
                                self.x += self.vel
                        else:
                                self.vel = self.vel * -1
                                self.walkCount = 0

        def hit2(self):
                if self.lives2 > 0:
                        self.lives2 -= 1
                else:
                        zombie2.x = 1
                        self.lives2 = 4
                print('hit')

class enemy3(object):                     #Enemy setup
        win.blit(pygame.image.load('Sprite 1.png'), (k, l))
        walkRight = [pygame.image.load('Sprite 2.png')]
        walkLeft = [pygame.image.load('Sprite 1.png')]
        def __init__(self, x, y, width, height, end):
                self.x = k
                self.y = l
                self.width = width
                self.height = height                                    #ADD MULTIPLE ENEMY CLASSES FOR WORKING HEALTH BARS
                self.end = end
                self.path = [self.x, self.end]
                self.walkCount = 0
                self.vel = 3
                self.hitbox3 = (self.x + 17, self.y + 2, 31, 57)
                self.lives3 = 4
                self.visible = True

        def draw3(self,win):                     #Zombie3 boundaries/increased move speed/hitbox
                self.move3()
                if self.visible:
                        if self.walkCount + 1 >= 33:
                                self.walkCount = 0

                        if self.vel > 0:
                                win.blit(self.walkRight[self.walkCount //4000], (self.x, self.y))
                                self.walkCount += 1
                        else:
                                win.blit(self.walkLeft[self.walkCount //4000], (self.x, self.y))
                                self.walkCount += 1

                        pygame.draw.rect(win, (255,0,0), (self.hitbox3[0], self.hitbox3[1] - 20, 25, 10))
                        pygame.draw.rect(win, (0,128,0), (self.hitbox3[0], self.hitbox3[1] - 20, 25 - (5 * (5 - self.lives3)), 10))
                        self.hitbox3 = (self.x + 17, self.y + 2, 31, 57)

        def move3(self):                 #How the enemies move on their own
                if self.vel > 0:
                        if self.x + self.vel < self.path[1]:
                                self.x += self.vel
                        else:
                                self.vel = self.vel * -1
                                self.walkCount = 0
                else:
                        if self.x - self.vel > self.path[0]:
                                self.x += self.vel
                        else:
                                self.vel = self.vel * -1
                                self.walkCount = 0

        def hit3(self):
                if self.lives3 > 0:
                        self.lives3 -= 1
                else:
                        zombie3.x = 1
                        self.lives3 = 4
                print('hit')
                   

def redrawGameWindow():                                #Redraw code for whenever needed                                                                 
        win.blit(bg, (0,0))
        text = font.render('Lives: ' + str(lives), 1, (0,0,0))
        win.blit(text, (350, 10))
        man.draw(win)
        zombie.draw(win)
        zombie2.draw2(win)
        zombie3.draw3(win)
        for bullet in bullets:
                bullet.draw(win)

        pygame.display.update()        
                 
run = True                                                                      #Some quick little settings
font = pygame.font.SysFont('comicsans', 30, True)
man = player(500, 373, 64, 64)
zombie = enemy(1, 385, 64, 64, 700)
zombie2 = enemy2(699, 385, 64, 64, 700)
zombie3 = enemy3(699, 385, 64, 64, 700)
shootLoop = 0
bullets = []
num_of_zombies = 1
gameover = False

while run:

        if zombie.visible == True:              #What happens when the player is hit by zombie 1
                if man.hitbox[1] < zombie.hitbox[1] + zombie.hitbox[3] and man.hitbox[1] + man.hitbox[3] > zombie.hitbox[1]:
                        if man.hitbox[0] + man.hitbox[2] > zombie.hitbox[0] and man.hitbox[0] < zombie.hitbox[0] + zombie.hitbox[2]:
                                man.hit()
                                man.x = 350
                                man.y = 373
                                zombie.x = 699
                                zombie2.x = -30
                                zombie3.x = 699
                                lives -= 1
                                text = font.render('Lives: ' + str(lives), 1, (0,0,0))
                                print(text)
                                if lives == 0:
                                        print("You Died --------- Your Score: ", score)
                                        pygame.time.delay(4000000)

        if zombie2.visible == True:              #What happens when the player is hit by zombie 2
                if man.hitbox[1] < zombie2.hitbox2[1] + zombie2.hitbox2[3] and man.hitbox[1] + man.hitbox[3] > zombie2.hitbox2[1]:
                        if man.hitbox[0] + man.hitbox[2] > zombie2.hitbox2[0] and man.hitbox[0] < zombie2.hitbox2[0] + zombie2.hitbox2[2]:
                                man.hit()
                                man.x = 350
                                man.y = 373
                                zombie.x = -30
                                zombie2.x = 699
                                zombie3.x = 699
                                lives -= 1
                                text = font.render('Lives: ' + str(lives), 1, (0,0,0))
                                print(text)
                                if lives == 0:
                                        print("You Died --------- Your Score: ", score)
                                        pygame.time.delay(4000000)

        if zombie3.visible == True:             # #What happens when the player is hit by zombie 3
                if man.hitbox[1] < zombie3.hitbox3[1] + zombie3.hitbox3[3] and man.hitbox[1] + man.hitbox[3] > zombie3.hitbox3[1]:
                        if man.hitbox[0] + man.hitbox[2] > zombie3.hitbox3[0] and man.hitbox[0] < zombie3.hitbox3[0] + zombie3.hitbox3[2]:
                                man.hit()
                                man.x = 350
                                man.y = 373
                                zombie.x = 1
                                zombie2.x = 699
                                zombie3.x = 699
                                lives -= 1
                                text = font.render('Lives: ' + str(lives), 1, (0,0,0))
                                print(text)
                                if lives == 0:
                                        print("You Died --------- Your Score: ", score)
                                        pygame.time.delay(4000000)

        if shootLoop > 0:       #Basically so people don't cheat and try to shoot ~400 bullets at once
                shootLoop += 1
        if shootLoop > 3:
                shootLoop = 0

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        for bullet in bullets:                  #zombie 1 hit
                if bullet.y - bullet.radius < zombie.hitbox[1] + zombie.hitbox[3] and bullet.y + bullet.radius > zombie.hitbox[1]:
                        if bullet.x + bullet.radius > zombie.hitbox[0] and bullet.x - bullet.radius < zombie.hitbox[0] + zombie.hitbox[2]:
                                zombie.hit()
                                score += 5
                                bullets.pop(bullets.index(bullet))

        for bullet in bullets:                  #zombie 2 hit
                if bullet.y - bullet.radius < zombie2.hitbox2[1] + zombie2.hitbox2[3] and bullet.y + bullet.radius > zombie2.hitbox2[1]:
                        if bullet.x + bullet.radius > zombie2.hitbox2[0] and bullet.x - bullet.radius < zombie2.hitbox2[0] + zombie2.hitbox2[2]:
                                zombie2.hit2()
                                score += 5
                                bullets.pop(bullets.index(bullet))

        for bullet in bullets:                  #zombie 3 hit
                if bullet.y - bullet.radius < zombie3.hitbox3[1] + zombie3.hitbox3[3] and bullet.y + bullet.radius > zombie3.hitbox3[1]:
                        if bullet.x + bullet.radius > zombie3.hitbox3[0] and bullet.x - bullet.radius < zombie3.hitbox3[0] + zombie3.hitbox3[2]:
                                zombie3.hit3()
                                score += 5
                                bullets.pop(bullets.index(bullet))

                if bullet.x < 700 and bullet.x > 0:             #Code to make the bullets disappear after they leave the game boundaries so that the game doesn't lag
                        bullet.x += bullet.vel
                else:
                        bullets.pop(bullets.index(bullet))


        pressed = pygame.key.get_pressed()                              #CONTROLS (WOOHOOOO)
        if pressed[pygame.K_SPACE] and shootLoop == 0:          #How to shoot
                if man.left:
                        facing = -1
                else:
                        facing = 1
                        
                if len(bullets) < 5:
                        bullets.append(projectiles(round(man.x + man.width //2), round(man.y + man.height //2), 6, (0,0,0), facing))

                shootLoop = 1

        
        if pressed[pygame.K_a] and man.x > man.vel:             #How to move left
                man.x -= man.vel
                man.left = True
                man.right = False
                man.standing = False
        elif pressed[pygame.K_d] and man.x < 700 - man.width - man.vel:                 #How to move right
                man.x += man.vel
                man.right = True
                man.left = False
                man.standing = False
        else:
                man.standing = True
                man.walkCount = 0

        if not(man.isJump):
                if pressed[pygame.K_w]:                 #How to jump
                        man.isJump = True
                        man.right = False
                        man.left = False
                        man.walkCount = 0
        else:
                if man.jumpCount >= -10:
                        neg = 1
                        if man.jumpCount < 0:
                                neg = -1
                        man.y -= (man.jumpCount ** 2) * 0.5 * neg
                        man.jumpCount -= 1
                else:
                        man.isJump = False
                        man.jumpCount = 10

                
       
        redrawGameWindow()

        clock.tick(30)

pygame.quit()

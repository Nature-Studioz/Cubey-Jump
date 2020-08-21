import pygameHelper as ph
import  pygame
from pygame import mixer
import math
import random
import  time


pygame.init()
screen = pygame.display.set_mode((500, 400))
icon = pygame.image.load("2020.png")
pygame.display.set_caption("Cubey Jump")
pygame.display.set_icon(icon)
#Cube
cube = pygame.image.load("2020.png")
cubeX = -450
cubeY = -160
cube_change = 0
v = 5
m = 1
a = 1
b = 2
c = 3
u = 0.2
d = 2
x = 1
o = 1
p = 80
z = 250
q = 0
r = 1
aa = 1
bb = 1
randoms = random.randint(1, 1000)
#BillBoard
bill = pygame.image.load("2021.png")
billY = -160
billX = 20
bill_change = 0
isJump = True
jumpCount = 10
scores = 0
#Score
score = pygame.font.Font("freesansbold.ttf", 25)
high = pygame.font.Font("freesansbold.ttf", 25)
highs = scores
#Over
over = pygame.font.Font("freesansbold.ttf", 15)
#Title
title = pygame.image.load("Cubey2.png")
titleX = 100
titleY = 0
mixer.music.load("Background.mp3")
mixer.music.play(-1)
#E
E = pygame.image.load("E.png")
EX = 100
EY = -500
def imgblits():
   screen.blit(bill,(billX, billY))

def fonts():
    fonts = score.render("Score:" + str(scores), True, (0, 100, 0))
    screen.blit(fonts,(0, 0))

def fontss():
    fontss = over.render("Game Over, Press The E Key to play again", True, (q, 0, z))
    screen.blit(fontss,(100, 20))

def fontsss():
     fontsss = over.render("High Score:" + str(highs), True, (255, 0, 0))
     screen.blit(fontsss,(0, 40))






while True:
    screen.fill((0, 0, 250))
    if c == 1:
     scores += aa
     print(randoms)











    if cubeY <= -480:
        cubeY = -480


    if cubeY >= -161:
        cubeY = -161
        v = 4


    if v == 4:
        isJump = True

    if billX <= -700:
        billX = 0
        bill_change = 0.3


    if scores >= 10000:
        bill_change = 0.5
        u = 0.3

    if scores >= 30000:
        bill_change = 0.6
        u = 0.4

    if scores >= 600000:
        bill_change = 0.8
        u = 0.5

    if scores >= 150000:
        bill_change = 1
        u = 0.6

    if highs < scores:
        highs = scores

    if highs > scores:
        highs = highs





    C = ph.collision(63, cubeX, cubeY, billX, billY)
    C2 = ph.collision(80, cubeX, cubeY, billX, billY)

    if C:
        print("Hit")
        b = 1
        aa = 0
        bill_change = 0
        cubeX = 1000
        c = 2
        EY = 0
        r = 2
        q = 255
        mix = mixer.Sound("Bomb.wav")
        mix.play()
        bb = 2

    if C2 and x == 2:
        if jumpCount >= 0:
            cubeY -= (jumpCount * abs(jumpCount)) * 1.5
            cube_change = -u
            mix = mixer.Sound("Jump.wav")
            mix.play()
            print(jumpCount)
            v = 3
            isJump = False
        else:
            jumpCount = 10
            isJump = True

















    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()




        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_SPACE and isJump == True and b == 2 and x == 1 and c == 1:


               if jumpCount >= 0:
                   cubeY -= (jumpCount * abs(jumpCount)) * 1.5
                   cube_change = -u
                   print(jumpCount)
                   v = 3
                   mix = mixer.Sound("Jump.wav")
                   mix.play()
                   isJump = False
               else:
                   jumpCount = 10
                   isJump = True

           if event.key == pygame.K_a and c == 3:
               bill_change = 0.3
               titleY = 1000
               c = 1


           if event.key == pygame.K_c:
               x = 2
               o = 2
               print("AI Mode Activade")

           if event.key == pygame.K_d:
               x = 1

           if event.key == pygame.K_e and r == 2:
               cubeX = -450
               cubeY = -160
               cube_change = 0
               v = 5
               m = 1
               a = 1
               b = 2
               c = 3
               u = 0.2
               d = 2
               x = 1
               o = 1
               p = 80
               z = 250
               q = 0
               billY = -160
               billX = 20
               bill_change = 0
               isJump = True
               jumpCount = 10
               EY = -1000
               titleX = 100
               titleY = 0
               aa = 1
               bb = 1
               scores = 0
               mixer.music.load("Background.mp3")
               mixer.music.play(-1)
               r = 1






















    cubeY -= cube_change
    billX -= bill_change






    ph.imgblit(cube, cubeX, cubeY, screen=screen)
    ph.imgblit(bill,billX,billY,screen=screen)
    ph.imgblit(title,titleX, titleY, screen=screen)
    ph.imgblit(E, EX, EY, screen=screen)
    fonts()
    fontsss()












    pygame.display.update()






    
    




import math
import pygame

def collision(dis, x, y, x2, y2):
    distance = math.sqrt(math.pow(x - x2, 2) + math.pow(y - y2, 2))
    if distance < dis:
         return True
    else:
         return False



def imgblit(img, imgX, imgY, screen):
   screen.blit(img,(imgX, imgY))




def quits():
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.QUIT()


    

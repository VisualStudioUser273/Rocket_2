import pygame
import time
from pygame.locals import*
from time import*


pygame.init()
screen=pygame.display.set_mode((600,600))
player=pygame.image.load("Rocket.png")
bg=pygame.image.load("Bakground.png")

playing=True

player_x = 200

player_y = 200


while playing:
    screen.blit(bg,(0,0))
    screen.blit(player,(player_x,player_y))

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key==K_UP:
                player_y=player_y-25


###
           
            if event.key==K_DOWN:
                player_y=player_y+5

###
        
            if event.key==K_LEFT:
                player_x=player_x-5    


###
       
            if event.key==K_RIGHT:
                player_x=player_x+5 

    if player_y==600:
        pygame.quit()        



    player_y+=5
    sleep(0.05)  

            
    
      

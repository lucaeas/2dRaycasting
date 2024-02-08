import pygame
import math
import random

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("DOOM - PYTHON")
previousMousePos = (0,0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mousePos = pygame.mouse.get_pos()
    red = 255
    green = 255
    blue = 255

    if mousePos != previousMousePos:

        for largeur in range(0,880,80):
            pygame.draw.line(screen, (0,0,0), previousMousePos, (previousMousePos[0]+largeur,previousMousePos[1]+800), width=1)
            pygame.draw.line(screen, (red,green,blue), mousePos, (mousePos[0]+largeur,mousePos[1]+800), width=1)
            pygame.draw.line(screen, (0,0,0), previousMousePos, (previousMousePos[0]+largeur,previousMousePos[1]-800), width=1)
            pygame.draw.line(screen, (red,green,blue), mousePos, (mousePos[0]+largeur,mousePos[1]-800), width=1)
            pygame.draw.line(screen, (0,0,0), previousMousePos, (previousMousePos[0]-largeur,previousMousePos[1]+800), width=1)
            pygame.draw.line(screen, (red,green,blue), mousePos, (mousePos[0]-largeur,mousePos[1]+800), width=1)
            pygame.draw.line(screen, (0,0,0), previousMousePos, (previousMousePos[0]-largeur,previousMousePos[1]-800), width=1)
            pygame.draw.line(screen, (red,green,blue), mousePos, (mousePos[0]-largeur,mousePos[1]-800), width=1)
        
        for hauteur in range(0,880,80):
            pygame.draw.line(screen, (0,0,0), previousMousePos, (previousMousePos[0]+800,previousMousePos[1]+hauteur), width=1)
            pygame.draw.line(screen, (red,green,blue), mousePos, (mousePos[0]+800,mousePos[1]+hauteur), width=1)
            pygame.draw.line(screen, (0,0,0), previousMousePos, (previousMousePos[0]-800,previousMousePos[1]+hauteur), width=1)
            pygame.draw.line(screen, (red,green,blue), mousePos, (mousePos[0]-800,mousePos[1]+hauteur), width=1)
            pygame.draw.line(screen, (0,0,0), previousMousePos, (previousMousePos[0]+800,previousMousePos[1]-hauteur), width=1)
            pygame.draw.line(screen, (red,green,blue), mousePos, (mousePos[0]+800,mousePos[1]-hauteur), width=1)
            pygame.draw.line(screen, (0,0,0), previousMousePos, (previousMousePos[0]-800,previousMousePos[1]-hauteur), width=1)
            pygame.draw.line(screen, (red,green,blue), mousePos, (mousePos[0]-800,mousePos[1]-hauteur), width=1)
    
    
    pygame.display.update()
    previousMousePos = mousePos

pygame.quit()
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
        for largeur in range(0,800,40):
            pygame.draw.line(screen, (0,0,0),previousMousePos, (largeur,800))
            pygame.draw.line(screen, (0,0,0),previousMousePos, (largeur,0))
            pygame.draw.line(screen, (red,green,blue),mousePos, (largeur,800))
            pygame.draw.line(screen, (red,green,blue),mousePos, (largeur,0))
        for hauteur in range(0,820,40):
            pygame.draw.line(screen, (0,0,0),previousMousePos, (0,hauteur))
            pygame.draw.line(screen, (0,0,0),previousMousePos, (800,hauteur))
            pygame.draw.line(screen, (red,green,blue),mousePos, (0,hauteur))
            pygame.draw.line(screen, (red,green,blue),mousePos, (800,hauteur))
    pygame.display.update()
    previousMousePos = mousePos

pygame.quit()
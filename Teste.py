import pygame
import random

pygame.init()
pygame.mixer.init()

WIDTH = 480
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Cayman')
background= pygame.image.load("pygame.gv/imagens/base.webp").convert()

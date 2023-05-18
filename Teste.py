import pygame
import random

pygame.init()
pygame.mixer.init()

WIDTH = 480
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Cayman')
bg_img = pygame.image.load("Mega desoft/base.webp")
bg_img = pygame.transform.scale(bg_img,(WIDTH,HEIGHT))

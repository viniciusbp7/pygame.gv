import random
import pygame
import time 


pygame.init()

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Hello World!')

# ----- Inicia estruturas de dados
game = True

# Importa os sprites de personagens e mobs------------------------------------------------------------------------

background = pygame.image.load('imagens/base.webp').convert()
ritsu = pygame.image.load("imagens/Ritsu/General_Ritsu_1.png")
hinoekagura= pygame.image.load("imagens/Hinoekagura/Hinoekagura_Base.png")
veronica = pygame.image.load("imagens/Veronica/Veronica_Base.png")
lobo = pygame.image.load("imagens/Mobs/Lobo_Base.png")
lagarto = pygame.image.load("imagens/Mobs/Lagarto_Base.png")
elefante = pygame.image.load("imagens/Mobs/Elefante_Base.png")

# Define o tamanho dos personagens e mobs--------------------------------------------------------------------------

WIDTH = window.get_width()
HEIGHT = window.get_height()

R_WIDTH = (ritsu.get_width())/1.25
R_HEIGHT = (ritsu.get_height())/1.25

H_WIDTH = (hinoekagura.get_width())/1.25
H_HEIGHT = (hinoekagura.get_height())/1.25

V_WIDTH = (veronica.get_width())
V_HEIGHT = (veronica.get_height())

L_WIDTH = (lobo.get_width())/1.25
L_HEIGHT = (lobo.get_height())/1.25

LA_WIDTH = (lagarto.get_width())*2.2
LA_HEIGHT = (lagarto.get_height())*2.2

E_WIDTH = (elefante.get_width())*2.2
E_HEIGHT = (elefante.get_height())*2.2

# Ajusta o tamanho dos personagens e mobs------------------------------------------------------------------------

background = pygame.transform.scale(background, (WIDTH, HEIGHT))
ritsu = pygame.transform.scale(ritsu, (R_WIDTH, R_HEIGHT))
hinoekagura = pygame.transform.scale(hinoekagura, (H_WIDTH, H_HEIGHT))
veronica = pygame.transform.scale(veronica, (V_WIDTH, V_HEIGHT))
lobo = pygame.transform.scale(lobo, (L_WIDTH, L_HEIGHT))
lagarto = pygame.transform.scale(lagarto, (LA_WIDTH, LA_HEIGHT))
elefante = pygame.transform.scale(elefante, (E_WIDTH, E_HEIGHT))

# ===== Loop principal =====
while game:

    for event in pygame.event.get():

        # Fecha o jogo quando aperta esc-------------------------------------------------------------------------

        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit()

    # Define o Background---------------------------------------------------------------------------------------
    window.blit(background, (0, 0))

    # Escreve o hp----------------------------------------------------------------------------------------------------

    hp_r=str(300)
    hp_v=str(450)
    hp_h=str(150)
    hp_l=str(300)
    hp_la=str(800)
    hp_e=str(3000)

    font = pygame.font.SysFont(None, 48)

    # HP  dos personagens-----------------------------------------------------------------------------------------------

    HP_r=text = font.render(f'HP {hp_r} / 300', True, (46, 255, 0 ))
    HP_v=text = font.render(f'HP {hp_v} / 450' , True, (46, 255, 0 ))
    HP_h=text = font.render(f'HP {hp_h} / 150', True, (46, 255, 0 ))

    # HP dos lobos (WAVE 1)---------------------------------------------------------------------------------------------

    HP_l1=text = font.render(f'HP {hp_l} / 300', True, (239, 3, 3 ))
    HP_l2=text = font.render(f'HP {hp_l} / 300', True, (239, 3, 3 ))
    HP_l3=text = font.render(f'HP {hp_l} / 300', True, (239, 3, 3 ))

    # HP dos lagartos (WAVE 2)-----------------------------------------------------------------------------------------

    HP_la1=text = font.render(f'HP {hp_la} / 800' , True, (239, 3, 3 ))
    HP_la2=text = font.render(f'HP {hp_la} / 800' , True, (239, 3, 3 ))

    # HP do elefante (BOSS WAVE 3)-----------------------------------------------------------------------------------------

    HP_e=text = font.render(f'HP {hp_e} / 3000', True, (239, 3, 3 ))

    # Posiciona os personagens em campo---------------------------------------------------------------------------------

    window.blit(ritsu, (360, HEIGHT-420))
    window.blit(hinoekagura, (60, HEIGHT-650))
    window.blit(veronica, (100, HEIGHT-350))

    # Posiciona a barra de hp dos personagens--------------------------------------------------------------------------

    window.blit(HP_r,(380, HEIGHT-460))
    window.blit(HP_v,(120, HEIGHT-380))
    window.blit(HP_h,(170, HEIGHT-690))

    # Wave 1----------------------------------------------------------------------------------------------------

    #window.blit(lobo, (WIDTH-400,HEIGHT-210))
    #window.blit(lobo, (WIDTH-700,HEIGHT-410))
    #window.blit(lobo, (WIDTH-400,HEIGHT-570))

    # Posiciona o hp dos lobos----------------------------------------------------------------------------------

    #window.blit(HP_l1,(WIDTH-350, HEIGHT-620))
    #window.blit(HP_l2,(WIDTH-640, HEIGHT-450))
    #window.blit(HP_l3,(WIDTH -350 , HEIGHT-260))

    # Wave 2----------------------------------------------------------------------------------------------------

    #window.blit(lagarto, (WIDTH-630,HEIGHT-340))
    #window.blit(lagarto, (WIDTH-630,HEIGHT-660))

    # Posiciona o hp dos lagartos-------------------------------------------------------------------------------

    #window.blit(HP_la1,(WIDTH-700, HEIGHT-560))
    #window.blit(HP_la2,(WIDTH-700, HEIGHT-220))    

    # BOSS Wave-------------------------------------------------------------------------------------------------

    #window.blit(elefante, (WIDTH-800,HEIGHT-635))

    # Posiciona o hp dos elefante-------------------------------------------------------------------------------

    #window.blit(HP_e,(WIDTH-550, HEIGHT-700))

    # ----- Atualiza estado do jogo

    pygame.display.update()  # Mostra o novo frame para o jogador
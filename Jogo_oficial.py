import random
# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
#WIDTH = 500
#HEIGHT = 400
#window = pygame.display.set_mode((WIDTH, HEIGHT))
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Hello World!')

# ----- Inicia estruturas de dados
game = True

# ----- Inicia assets
background = pygame.image.load('imagens/base.webp').convert()
ritsu= pygame.image.load("imagens/Ritsu/General_Ritsu_Base.png")

WIDTH = window.get_width()
HEIGHT = window.get_height()

background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        
        #if event.type == pygame.KEYDOWN:
            #if event.type == pygame.K_1:
                #game = False

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    window.blit(ritsu, (2, 2))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados


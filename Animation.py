
import pygame
import spritesheet

# Importa os sprites de personagens e mobs------------------------------------------------------------------------

background = pygame.image.load('imagens/base.webp').convert()
veronica = pygame.image.load("imagens/Veronica/Veronica_spritesheet_regular.png")

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Hello World!')

game=True

FPS = 60 # Frames por segundo

# Define estados possíveis do jogador
STILL = 0
WALKING = 1
JUMPING = 2
FIGHTING = 3
SWIMMING = 4
V_WIDTH = (veronica.get_width())
V_HEIGHT = (veronica.get_height())
WIDTH = window.get_width()
HEIGHT = window.get_height()

class veronica(pygame.sprite.Sprite):
    
    # Construtor da classe. O argumento player_sheet é uma imagem contendo um spritesheet.
    def __init__(self, player_sheet):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Aumenta o tamanho do spritesheet para ficar mais fácil de ver
        veronica_sheet = pygame.transform.scale(veronica, (640, 640))

        # Define sequências de sprites de cada animação
        spritesheet_V = spritesheet(veronica_sheet, 2, 6)
        self.animations = {
            STILL: spritesheet_V[0:11]
        }
        # Define estado atual (que define qual animação deve ser mostrada)
        self.state = STILL
        # Define animação atual
        self.animation = self.animations[self.state]
        # Inicializa o primeiro quadro da animação
        self.frame = 0
        self.image = self.animation[self.frame]
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza na tela.
        window.blit(veronica, (100, HEIGHT-350))

        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 300
        
    # Metodo que atualiza a posição do personagem
    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()

        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:

            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Atualiza animação atual
            self.animation = self.animations[self.state]
            # Reinicia a animação caso o índice da imagem atual seja inválido
            if self.frame >= len(self.animation):
                self.frame = 0
            
            # Armazena a posição do centro da imagem
            center = self.rect.center
            # Atualiza imagem atual
            self.image = self.animation[self.frame]
            # Atualiza os detalhes de posicionamento
            self.rect = self.image.get_rect()
            self.rect.center = center

            self.rect.centerx = WIDTH / 2
            self.rect.centery = HEIGHT / 2



while game:

    for event in pygame.event.get():

        # Fecha o jogo quando aperta esc-------------------------------------------------------------------------

        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit()

    # Define o Background---------------------------------------------------------------------------------------
    window.blit(background, (0, 0))

    # Posiciona os personagens em campo---------------------------------------------------------------------------------
    window.blit(veronica, (100, HEIGHT-350))
    pygame.display.update()  # Mostra o novo frame para o jogador

pygame.quit()
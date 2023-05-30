import pygame
from os import path
import random

# Estabelece a pasta que contem as figuras e sons.

img_dir = path.join(path.dirname(__file__), 'imagens')

#Estabelece os sons.
pygame.mixer.init()
pygame.mixer.music.load('sons/corrupted-violin-fencer-boss-theme.mp3')
pygame.mixer.music.set_volume(0.4)

# Define dados iniciais para as funções------------------------------------------------------------------------
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
STILL = 0
TITULO = 'NOME DO JOGO'
WIDTH = window.get_width()
HEIGHT = window.get_height()
FPS = 60 # Frames por segundo
background = pygame.image.load('imagens/base.webp')
Win_stat=pygame.image.load('imagens/WIN.webp')
gameover=pygame.image.load('imagens/GAMEOVER.png')
start=pygame.image.load("imagens/Start!.png")
pygame.display.set_caption('Hello World!')

game=True

background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# carrega a função da spritesheet------------------------------------------------------------------------------------

def load_spritesheet(spritesheet, rows, columns):
    # Calcula a largura e altura de cada sprite.
    sprite_width = spritesheet.get_width() // columns
    sprite_height = spritesheet.get_height() // rows
    
    # Percorre todos os sprites adicionando em uma lista.
    sprites = []
    for row in range(rows):
        for column in range(columns):
            # Calcula posição do sprite atual
            x = column * sprite_width
            y = row * sprite_height
            # Define o retângulo que contém o sprite atual
            dest_rect = pygame.Rect(x, y, sprite_width, sprite_height)

            # Cria uma imagem vazia do tamanho do sprite
            image = pygame.Surface((sprite_width, sprite_height), pygame.SRCALPHA)
            # Copia o sprite atual (do spritesheet) na imagem
            image.blit(spritesheet, (0, 0), dest_rect)
            sprites.append(image)

    return sprites

# Classes dos personagens----------------------------------------------------------------------------------------

class Veronica(pygame.sprite.Sprite):
    
    # Construtor da classe. O argumento player_sheet é uma imagem contendo um spritesheet.
    def __init__(self, veronica_sheet):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Aumenta o tamanho do spritesheet para ficar mais fácil de ver
        veronica_sheet = pygame.transform.scale(veronica_sheet, (650, 300))

        # Define sequências de sprites de cada animação
        spritesheet_V = load_spritesheet(veronica_sheet, 1, 5)
        self.animations = {
            STILL: spritesheet_V[0:5]
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
        
        self.rect.centerx = 180
        self.rect.centery = HEIGHT-180


        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 150
        
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

            self.rect.centerx = 180
            self.rect.centery = HEIGHT-180

class Ristu(pygame.sprite.Sprite):
    
    # Construtor da classe. O argumento player_sheet é uma imagem contendo um spritesheet.
    def __init__(self, ritsu_sheet):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Aumenta o tamanho do spritesheet para ficar mais fácil de ver
        ritsu_sheet = pygame.transform.scale(ritsu_sheet, (860, 225))

        # Define sequências de sprites de cada animação
        spritesheet_R = load_spritesheet(ritsu_sheet, 1, 6)
        self.animations = {
            STILL: spritesheet_R[0:6]
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
        
        self.rect.centerx = 470
        self.rect.centery = HEIGHT-305


        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 120

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

            self.rect.centerx = 470
            self.rect.centery = HEIGHT-305

class Hinoekagura(pygame.sprite.Sprite):
    
    # Construtor da classe. O argumento player_sheet é uma imagem contendo um spritesheet.
    def __init__(self, hinoekagura_sheet):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Aumenta o tamanho do spritesheet para ficar mais fácil de ver
        hinoekagura_sheet = pygame.transform.scale(hinoekagura_sheet, (660, 225))

        # Define sequências de sprites de cada animação
        spritesheet_H = load_spritesheet(hinoekagura_sheet, 1, 2)
        self.animations = {
            STILL: spritesheet_H[0:3]
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
        
        self.rect.centerx = 200
        self.rect.centery = HEIGHT-570


        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 520

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

            self.rect.centerx = 200
            self.rect.centery = HEIGHT-570

# Classes dos lobos--------------------------------------------------------------------------------------------------------

class Lobo1(pygame.sprite.Sprite):
    
    # Construtor da classe. O argumento player_sheet é uma imagem contendo um spritesheet.
    def __init__(self, lobo_sheet):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Aumenta o tamanho do spritesheet para ficar mais fácil de ver
        lobo_sheet = pygame.transform.scale(lobo_sheet, (860, 230))

        # Define sequências de sprites de cada animação
        spritesheet_L = load_spritesheet(lobo_sheet, 1, 4)
        self.animations = {
            STILL: spritesheet_L[0:4]
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
        
        self.rect.centerx = WIDTH-280
        self.rect.centery = HEIGHT-470


        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 140

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

            self.rect.centerx = WIDTH-280
            self.rect.centery = HEIGHT-470

class Lobo2(pygame.sprite.Sprite):
    
    # Construtor da classe. O argumento player_sheet é uma imagem contendo um spritesheet.
    def __init__(self, lobo_sheet):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Aumenta o tamanho do spritesheet para ficar mais fácil de ver
        lobo_sheet = pygame.transform.scale(lobo_sheet, (860, 230))

        # Define sequências de sprites de cada animação
        spritesheet_L = load_spritesheet(lobo_sheet, 1, 4)
        self.animations = {
            STILL: spritesheet_L[0:4]
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
        
        self.rect.centerx = WIDTH-560
        self.rect.centery = HEIGHT-365


        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 140

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

            self.rect.centerx = WIDTH-560
            self.rect.centery = HEIGHT-365

class Lobo3(pygame.sprite.Sprite):
    
    # Construtor da classe. O argumento player_sheet é uma imagem contendo um spritesheet.
    def __init__(self, lobo_sheet):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Aumenta o tamanho do spritesheet para ficar mais fácil de ver
        lobo_sheet = pygame.transform.scale(lobo_sheet, (860, 230))

        # Define sequências de sprites de cada animação
        spritesheet_L = load_spritesheet(lobo_sheet, 1, 4)
        self.animations = {
            STILL: spritesheet_L[0:4]
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
        
        self.rect.centerx = WIDTH-300
        self.rect.centery = HEIGHT-145


        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 140

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

            self.rect.centerx = WIDTH-300
            self.rect.centery = HEIGHT-145

# Classes dos lagartos--------------------------------------------------------------------------------------------------------

class Lagarto1(pygame.sprite.Sprite):
    
    # Construtor da classe. O argumento player_sheet é uma imagem contendo um spritesheet.
    def __init__(self, lagarto_sheet):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Aumenta o tamanho do spritesheet para ficar mais fácil de ver
        lagarto_sheet = pygame.transform.scale(lagarto_sheet, (1460, 330))

        # Define sequências de sprites de cada animação
        spritesheet_La = load_spritesheet(lagarto_sheet, 1, 5)
        self.animations = {
            STILL: spritesheet_La[0:5]
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
        
        self.rect.centerx = WIDTH-400
        self.rect.centery = HEIGHT-525


        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 140

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

            self.rect.centerx = WIDTH-400
            self.rect.centery = HEIGHT-525

class Lagarto2(pygame.sprite.Sprite):
    
    # Construtor da classe. O argumento player_sheet é uma imagem contendo um spritesheet.
    def __init__(self, lagarto_sheet):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Aumenta o tamanho do spritesheet para ficar mais fácil de ver
        lagarto_sheet = pygame.transform.scale(lagarto_sheet, (1460, 330))

        # Define sequências de sprites de cada animação
        spritesheet_La = load_spritesheet(lagarto_sheet, 1, 5)
        self.animations = {
            STILL: spritesheet_La[0:5]
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
        
        self.rect.centerx = WIDTH-400
        self.rect.centery = HEIGHT-195


        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 140

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

            self.rect.centerx = WIDTH-400
            self.rect.centery = HEIGHT-195


# Classe do elefante -------------------------------------------------------------------------------------------------------

class Elefante(pygame.sprite.Sprite):
    
    # Construtor da classe. O argumento player_sheet é uma imagem contendo um spritesheet.
    def __init__(self, elefante_sheet):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Aumenta o tamanho do spritesheet para ficar mais fácil de ver
        elefante_sheet = pygame.transform.scale(elefante_sheet, (1460, 445))

        # Define sequências de sprites de cada animação
        spritesheet_E = load_spritesheet(elefante_sheet, 1, 3)
        self.animations = {
            STILL: spritesheet_E[0:3]
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
        
        self.rect.centerx = WIDTH-400
        self.rect.centery = HEIGHT-395


        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 290

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

            self.rect.centerx = WIDTH-400
            self.rect.centery = HEIGHT-395

# Animações dos personagens------------------------------------------------------------------------------------------------------------

class Hinoekagura_Ani(pygame.sprite.Sprite):
    
    # Construtor da classe. O argumento player_sheet é uma imagem contendo um spritesheet.
    def __init__(self, hinoekagura_ani_sheet):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Aumenta o tamanho do spritesheet para ficar mais fácil de ver
        hinoekagura_ani_sheet = pygame.transform.scale(hinoekagura_ani_sheet, (660, 225))

        # Define sequências de sprites de cada animação
        spritesheet_H_ani = load_spritesheet(hinoekagura_ani_sheet, 1, 3)
        self.animations = {
            STILL: spritesheet_H_ani[0:3]
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
        
        self.rect.centerx = 200
        self.rect.centery = HEIGHT-570


        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 320

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

            self.rect.centerx = 200
            self.rect.centery = HEIGHT-570

class Ristu_Ani(pygame.sprite.Sprite):
    
    # Construtor da classe. O argumento player_sheet é uma imagem contendo um spritesheet.
    def __init__(self, ritsu_sheet):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Aumenta o tamanho do spritesheet para ficar mais fácil de ver
        ritsu_sheet = pygame.transform.scale(ritsu_sheet, (1260, 375))

        # Define sequências de sprites de cada animação
        spritesheet_R = load_spritesheet(ritsu_sheet, 1, 6)
        self.animations = {
            STILL: spritesheet_R[0:6]
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
        
        self.rect.centerx = 470
        self.rect.centery = HEIGHT-305


        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 120

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

            self.rect.centerx = 470
            self.rect.centery = HEIGHT-305

class Veronica_Ani(pygame.sprite.Sprite):
    
    # Construtor da classe. O argumento player_sheet é uma imagem contendo um spritesheet.
    def __init__(self, veronica_sheet):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Aumenta o tamanho do spritesheet para ficar mais fácil de ver
        veronica_sheet = pygame.transform.scale(veronica_sheet, (650, 300))

        # Define sequências de sprites de cada animação
        spritesheet_V = load_spritesheet(veronica_sheet, 1, 3)
        self.animations = {
            STILL: spritesheet_V[0:3]
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
        
        self.rect.centerx = 180
        self.rect.centery = HEIGHT-180


        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 150
        
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

            self.rect.centerx = 180
            self.rect.centery = HEIGHT-180
# Animação dos lobos------------------------------------------------------------------------------------------------------------------

class Lobo1_Ani(pygame.sprite.Sprite):
    
    # Construtor da classe. O argumento player_sheet é uma imagem contendo um spritesheet.
    def __init__(self, lobo_sheet_ani):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Aumenta o tamanho do spritesheet para ficar mais fácil de ver
        lobo_sheet_ani = pygame.transform.scale(lobo_sheet_ani, (860, 330))

        # Define sequências de sprites de cada animação
        spritesheet_L_ani = load_spritesheet(lobo_sheet_ani, 1, 3)
        self.animations = {
            STILL: spritesheet_L_ani[0:4]
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
        
        self.rect.centerx = WIDTH-280
        self.rect.centery = HEIGHT-470


        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 140

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

            self.rect.centerx = WIDTH-280
            self.rect.centery = HEIGHT-470

class Lobo2_Ani(pygame.sprite.Sprite):
    
    # Construtor da classe. O argumento player_sheet é uma imagem contendo um spritesheet.
    def __init__(self, lobo_sheet_ani):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Aumenta o tamanho do spritesheet para ficar mais fácil de ver
        lobo_sheet_ani = pygame.transform.scale(lobo_sheet_ani, (860, 330))

        # Define sequências de sprites de cada animação
        spritesheet_L_ani = load_spritesheet(lobo_sheet_ani, 1, 3)
        self.animations = {
            STILL: spritesheet_L_ani[0:4]
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
        
        self.rect.centerx = WIDTH-560
        self.rect.centery = HEIGHT-365


        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 140

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

            self.rect.centerx = WIDTH-560
            self.rect.centery = HEIGHT-365

class Lobo3_Ani(pygame.sprite.Sprite):
    
    # Construtor da classe. O argumento player_sheet é uma imagem contendo um spritesheet.
    def __init__(self, lobo_sheet_ani):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Aumenta o tamanho do spritesheet para ficar mais fácil de ver
        lobo_sheet_ani = pygame.transform.scale(lobo_sheet_ani, (860, 330))

        # Define sequências de sprites de cada animação
        spritesheet_L_ani = load_spritesheet(lobo_sheet_ani, 1, 3)
        self.animations = {
            STILL: spritesheet_L_ani[0:4]
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
        
        self.rect.centerx = WIDTH-300
        self.rect.centery = HEIGHT-145


        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 140

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

            self.rect.centerx = WIDTH-300
            self.rect.centery = HEIGHT-145

# Animação dos lagartos--------------------------------------------------------------------------------------------------------

class Lagarto1_Ani(pygame.sprite.Sprite):
    
    # Construtor da classe. O argumento player_sheet é uma imagem contendo um spritesheet.
    def __init__(self, lagarto_sheet):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Aumenta o tamanho do spritesheet para ficar mais fácil de ver
        lagarto_sheet = pygame.transform.scale(lagarto_sheet, (1460, 330))

        # Define sequências de sprites de cada animação
        spritesheet_La = load_spritesheet(lagarto_sheet, 1, 4)
        self.animations = {
            STILL: spritesheet_La[0:4]
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
        
        self.rect.centerx = WIDTH-400
        self.rect.centery = HEIGHT-525


        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 140

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

            self.rect.centerx = WIDTH-400
            self.rect.centery = HEIGHT-525

class Lagarto2_Ani(pygame.sprite.Sprite):
    
    # Construtor da classe. O argumento player_sheet é uma imagem contendo um spritesheet.
    def __init__(self, lagarto_sheet):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Aumenta o tamanho do spritesheet para ficar mais fácil de ver
        lagarto_sheet = pygame.transform.scale(lagarto_sheet, (1460, 330))

        # Define sequências de sprites de cada animação
        spritesheet_La = load_spritesheet(lagarto_sheet, 1, 4)
        self.animations = {
            STILL: spritesheet_La[0:4]
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
        
        self.rect.centerx = WIDTH-400
        self.rect.centery = HEIGHT-195


        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 140

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

            self.rect.centerx = WIDTH-400
            self.rect.centery = HEIGHT-195

# Animação do elefante-------------------------------------------------------------------------------------------------------

class Elefante_Ani(pygame.sprite.Sprite):
    
    # Construtor da classe. O argumento player_sheet é uma imagem contendo um spritesheet.
    def __init__(self, elefante_sheet):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Aumenta o tamanho do spritesheet para ficar mais fácil de ver
        elefante_sheet = pygame.transform.scale(elefante_sheet, (2360, 900))

        # Define sequências de sprites de cada animação
        spritesheet_E = load_spritesheet(elefante_sheet, 1, 4)
        self.animations = {
            STILL: spritesheet_E[0:4]
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
        
        self.rect.centerx = WIDTH-400
        self.rect.centery = HEIGHT-565


        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 260

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

            self.rect.centerx = WIDTH-400
            self.rect.centery = HEIGHT-565


# Define situações inicias do jogo------------------------------------------------------------------------------------------

def game_screen(screen):

    # Variável para o ajuste de velocidade---------------------------------------------------------------------------------

    clock = pygame.time.Clock()

    # Carrega spritesheet ----------------------------------------------------------------------------------------------------

    veronica_sheet = pygame.image.load(path.join(img_dir, 'Veronica/Veronica_spritesheet_regular.png')).convert_alpha()
    ritsu_sheet = pygame.image.load(path.join(img_dir, "Ritsu/General_Ritsu_spritesheet_regular.png")).convert_alpha()
    hinoekagura_sheet = pygame.image.load(path.join(img_dir, "Hinoekagura/Hinoekagura_spritesheet_regular.png")).convert_alpha()
    elefane_sheet = pygame.image.load(path.join(img_dir, "Mobs/Elefante_spritesheet_regular.png")).convert_alpha()
    lobo_sheet = pygame.image.load(path.join(img_dir, "Mobs/Lobo_spritesheet_regular.png")).convert_alpha()
    lagarto_sheet= pygame.image.load(path.join(img_dir, "Mobs/Lagarto_spritesheet_regular.png")).convert_alpha()

    # animações de ataque----------------------------------------------------------------------------------------------

    hinoekagura_sheet_ani = pygame.image.load(path.join(img_dir, "Hinoekagura/Hinoekagura_spritesheet_ataque.png")).convert_alpha()
    ritsu_sheet_ani = pygame.image.load(path.join(img_dir, "Ritsu/General_Ritsu_spritesheet_ataque.png")).convert_alpha()
    veronica_sheet_ani = pygame.image.load(path.join(img_dir, 'Veronica/Veronica_spritesheet_ataque.png')).convert_alpha()
    lobo_ani= pygame.image.load(path.join(img_dir, "Mobs/Lobo_spritesheet_ataque.png")).convert_alpha()
    lagarto_ani= pygame.image.load(path.join(img_dir, "Mobs/Lagarto_spritesheet_ataque.png")).convert_alpha()
    elefante_ani=pygame.image.load(path.join(img_dir, "Mobs/Elefante_spritesheet_ataque.png")).convert_alpha()


    # Cria Sprite do jogador------------------------------------------------------------------------------------------------

    veronica = Veronica(veronica_sheet)
    ritsu = Ristu(ritsu_sheet)
    hinoekagura=Hinoekagura(hinoekagura_sheet)
    elefante= Elefante(elefane_sheet)

    # Cria as animações-----------------------------------------------------------------------------------------------------

    hinoekagura_ani=Hinoekagura_Ani(hinoekagura_sheet_ani)
    ritsu_ani=Ristu_Ani(ritsu_sheet_ani)
    veronica_ani=Veronica_Ani(veronica_sheet_ani)
    lobo1_ani=Lobo1_Ani(lobo_ani)
    lobo2_ani=Lobo2_Ani(lobo_ani)
    lobo3_ani=Lobo3_Ani(lobo_ani)
    lagarto1_ani=Lagarto1_Ani(lagarto_ani)
    lagarto2_ani=Lagarto2_Ani(lagarto_ani)
    elefante_ani= Elefante_Ani(elefante_ani)

    # Cria sprites dos lobos ------------------------------------------------------------------------------------------------------

    lobo1 = Lobo1(lobo_sheet)
    lobo2 = Lobo2(lobo_sheet)
    lobo3 = Lobo3(lobo_sheet)
    
    # Cria sprites dos lagartos--------------------------------------------------------------------------------------------

    lagarto1=Lagarto1(lagarto_sheet)
    lagarto2=Lagarto2(lagarto_sheet)

    # Cria um grupo de todos os sprites do jogador-------------------------------------------------------------------------

    all_sprites = pygame.sprite.Group()
    all_sprites.add(veronica)
    all_sprites.add(ritsu)
    all_sprites.add(hinoekagura)

    # Cria os prompts de ataque----------------------------------------------------------------------------------------------

    cor=(32, 29, 27)

    vertices1=[(WIDTH-1000,HEIGHT-30),(WIDTH-1000,HEIGHT-130),(WIDTH-800,HEIGHT-130),(WIDTH-800,HEIGHT-30)]

    vertices2=[(WIDTH-750,HEIGHT-30),(WIDTH-750,HEIGHT-130),(WIDTH-550,HEIGHT-130),(WIDTH-550,HEIGHT-30)]

    # Inicia o loop principal do jogo------------------------------------------------------------------------------------------
    init = 2 
    end=3
    PLAYING = 0
    DONE = 1
    vit=4

    hp_r=(300)
    hp_v=(450)
    hp_h=(225)
    hp_l={'lobo1':700, 'lobo2':700, 'lobo3':700}
    hp_la={'lagarto1':1600, 'lagarto2':1600}
    hp_e=(3000)
    pygame.mixer.music.play(loops=-1)

    turno=0
    deca=0
    ag=0
    cl=2
    ani=0
    cont=0
    add1=0
    hit=0
    #controla o tempo

    tempo_a=0

    # Define se o personagem esta vivo-----------------------------------------------------------------------------------
    ra=True
    va=True
    ha=True

    # Jogo principal---------------------------------------------------------------------------------------------------------

    state = init
    while state != DONE:

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    state = DONE

        # Escreve o hp----------------------------------------------------------------------------------------------------

        font = pygame.font.SysFont(None, 48)

        # HP  dos personagens-----------------------------------------------------------------------------------------------

        if state==init:
            window.blit(start,(WIDTH-1550, HEIGHT-850))
            call=font.render(f'Pressione as setas!', True, (255, 255, 255 ))
            call = pygame.transform.scale(call, (600, 150))
            window.blit(call,(WIDTH-740, HEIGHT-140))
            if event.type == pygame.KEYDOWN:
                state = PLAYING

        if state==PLAYING:

            HP_r= font.render(f'HP {hp_r} / 300', True, (46, 255, 0 ))
            HP_v= font.render(f'HP {hp_v} / 450' , True, (46, 255, 0 ))
            HP_h = font.render(f'HP {hp_h} / 225', True, (46, 255, 0 ))

            if hp_r<=0:
                all_sprites.remove(ritsu)
                ra=False
            
            if hp_h<=0:
                all_sprites.remove(hinoekagura)
                ha=False
            
            if hp_v<=0:
                all_sprites.remove(veronica)
                va=False

            if not ha and not ra and not va:
                state=end

            wave=1

            if wave==1:

                if add1==0:
                    all_sprites.add(lobo1)
                    all_sprites.add(lobo2)
                    all_sprites.add(lobo3)
                    add1=1

                HP_l1= font.render(f'HP {hp_l["lobo1"]} / 700', True, (239, 3, 3 ))
                HP_l2= font.render(f'HP {hp_l["lobo2"]} / 700', True, (239, 3, 3 ))
                HP_l3= font.render(f'HP {hp_l["lobo3"]} / 700', True, (239, 3, 3 ))

                if hp_l['lobo1']<=0:
                    all_sprites.remove(lobo1)

                if hp_l['lobo2']<=0:
                    all_sprites.remove(lobo2)
                
                if hp_l['lobo3']<=0:
                    all_sprites.remove(lobo3)

                if hp_l['lobo1']<=0  and hp_l['lobo2']<=0 and hp_l['lobo3']<=0 :
                    wave = 2

            # HP dos lagartos (WAVE 2)-----------------------------------------------------------------------------------------

            if wave ==2:
                
                if add1==1:
                    all_sprites.add(lagarto1)
                    all_sprites.add(lagarto2)
                    add1=2

                HP_la1= font.render(f'HP {hp_la["lagarto1"]} / 1600' , True, (239, 3, 3 ))
                HP_la2= font.render(f'HP {hp_la["lagarto2"]} / 1600' , True, (239, 3, 3 ))

                if hp_la['lagarto1']<=0:
                    all_sprites.remove(lagarto1)

                if hp_la['lagarto2']<=0:
                    all_sprites.remove(lagarto2)

                if hp_la['lagarto1']<=0 and hp_la['lagarto2']<=0:
                    wave=3

            # HP do elefante (BOSS WAVE 3)-----------------------------------------------------------------------------------------

            if wave ==3:

                if add1==2:
                    all_sprites.add(elefante)
                    add1=3
                
                HP_e = font.render(f'HP {hp_e} / 3000', True, (239, 3, 3 ))

                if hp_e>0:
                    window.blit(HP_e,(WIDTH-540, HEIGHT-640))

                if hp_e<=0:
                    all_sprites.remove(elefante)
                    



            # Atualiza a acao de cada sprite------------------------------------------------------------------------------------
            all_sprites.update()
            
            
            window.blit(background, (0, 0))
            all_sprites.draw(screen)

            if ra:
                window.blit(HP_r,(360, HEIGHT-460))
            if va:
                window.blit(HP_v,(110, HEIGHT-380))
            if ha:
                window.blit(HP_h,(130, HEIGHT-730))
            
            if wave==1:

                if hp_l['lobo1']>0:
                        window.blit(HP_l1,(WIDTH-400, HEIGHT-640))
                
                if hp_l['lobo2']>0:
                        window.blit(HP_l2,(WIDTH-660, HEIGHT-520))

                if hp_l['lobo3']>0:
                        window.blit(HP_l3,(WIDTH-420, HEIGHT-310))

            if wave ==2:
                
                if hp_la['lagarto1']>0:
                        window.blit(HP_la1,(WIDTH-720, HEIGHT-610))

                if hp_la['lagarto2']>0:
                        window.blit(HP_la2,(WIDTH-720, HEIGHT-280))

            if wave ==3:

                if hp_e>0:
                        window.blit(HP_e,(WIDTH-520, HEIGHT-620))

            aviso_de_ataque=font.render('Selecione o ataque', True, (255, 240, 0))
            selecao_de_alvo= font.render('Selecione o alvo', True, (255, 255, 255 ))

            # Mecanica de combate do jogo-------------------------------------------------------------------------------------

            #Turno da Hinoekaura----------------------------------------------------------------------------------------------

            if turno==0:
                
                if not ha:
                    ani=1
                    turno=1

                pygame.draw.polygon(window,cor,vertices1)
                pygame.draw.polygon(window,cor,vertices2)

                cura= font.render('Cura', True, (255, 255, 255 ))
                magia= font.render('Explosão', True, (255, 255, 255 ))

                window.blit(aviso_de_ataque, (WIDTH-930,HEIGHT-175 ))
                window.blit(cura, (WIDTH-695,HEIGHT-95 ))
                window.blit(magia, (WIDTH-980,HEIGHT-95))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    cl=0

                if wave==1:
                    
                    (x, y)= pygame.mouse.get_pos()

                    if (x >= WIDTH-1000 and x<=WIDTH-800) and (y <= HEIGHT-30 and y>=HEIGHT-130):
                            if event.type == pygame.MOUSEBUTTONUP and cl==0:
                                hp_l['lobo1']-=75
                                hp_l['lobo2']-=75
                                hp_l['lobo3']-=75
                                cl=1
                                cont=1

                    if (x >= WIDTH-750 and x<=WIDTH-550) and (y <= HEIGHT-30 and y>=HEIGHT-130) and event.type == pygame.MOUSEBUTTONUP:
                            if event.type == pygame.MOUSEBUTTONUP and cl==0:

                                if hp_r + 100 > 300:
                                    hp_r=300
                                else:
                                    hp_r+=100
                                
                                if hp_h+100 > 225:
                                    hp_h=225
                                else:
                                    hp_h+=100

                                if hp_v+100>450:
                                    hp_v=450
                                else:
                                    hp_v+=100
                                cl=1
                                cont=1
            
                if wave==2:

                    (x, y)= pygame.mouse.get_pos()
                    if (x >= WIDTH-1000 and x<=WIDTH-800) and (y <= HEIGHT-30 and y>=HEIGHT-130) and event.type == pygame.MOUSEBUTTONUP:
                            if event.type == pygame.MOUSEBUTTONUP and cl==0:                        
                                hp_la['lagarto1']-=75
                                hp_la['lagarto2']-=75
                                cl=1
                                cont=1
                                
                    if (x >= WIDTH-750 and x<=WIDTH-550) and (y <= HEIGHT-30 and y>=HEIGHT-130) and event.type == pygame.MOUSEBUTTONUP:
                            if event.type == pygame.MOUSEBUTTONUP and cl==0:
                                if hp_r + 100 > 300:
                                    hp_r=300
                                else:
                                    hp_r+=100
                                
                                if hp_h+100 > 225:
                                    hp_h=225
                                else:
                                    hp_h+=100

                                if hp_v+100>450:
                                    hp_v=450
                                else:
                                    hp_v+=100
                                cl=1
                                cont=1
                                
                if wave==3:
                    (x, y)= pygame.mouse.get_pos()
                    if (x >= WIDTH-1000 and x<=WIDTH-800) and (y <= HEIGHT-30 and y>=HEIGHT-130) and event.type == pygame.MOUSEBUTTONUP:
                            if event.type == pygame.MOUSEBUTTONUP and cl==0:                       
                                hp_e-=75
                                cl=1
                                cont=1

                    if (x >= WIDTH-750 and x<=WIDTH-550) and (y <= HEIGHT-30 and y>=HEIGHT-130) and event.type == pygame.MOUSEBUTTONUP:
                            if event.type == pygame.MOUSEBUTTONUP and cl==0:
                                if hp_r + 100 > 300:
                                    hp_r=300
                                else:
                                    hp_r+=100
                                
                                if hp_h+100 > 225:
                                    hp_h=225
                                else:
                                    hp_h+=100

                                if hp_v+100>450:
                                    hp_v=450
                                else:
                                    hp_v+=100
                                cl=1
                                cont=1

                if cont==1 and ani==0:
                    tempo_a=pygame.time.get_ticks()
                    ani=1
                if cont==1:
                    agora=pygame.time.get_ticks()

                    all_sprites.remove(hinoekagura)
                    all_sprites.add(hinoekagura_ani)

                    if agora-tempo_a>1000:

                        all_sprites.add(hinoekagura)
                        all_sprites.remove(hinoekagura_ani)
                        turno=1

            # Turno do Ritsu---------------------------------------------------------------------------------------------------

            if turno==1:

                if not ra:
                    ani=2
                    turno=2

                pygame.draw.polygon(window,cor,vertices1)
                pygame.draw.polygon(window,cor,vertices2)


                decapitar= font.render('Decapitar', True, (255, 255, 255 ))
                corte= font.render('Corte', True, (255, 255, 255 ))


                window.blit(aviso_de_ataque, (WIDTH-930,HEIGHT-175 ))
                window.blit(decapitar, (WIDTH-720,HEIGHT-95 ))
                window.blit(corte, (WIDTH-945,HEIGHT-95))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    cl=0

                if wave==1:
                    
                    (x, y)= pygame.mouse.get_pos()

                    if (x >= WIDTH-1000 and x<=WIDTH-800) and (y <= HEIGHT-30 and y>=HEIGHT-130):
                            if event.type == pygame.MOUSEBUTTONUP and cl==0:                        
                                hp_l['lobo1']-=100
                                hp_l['lobo2']-=100
                                hp_l['lobo3']-=100
                                cl=1
                                cont=2


                    if (x >= WIDTH-750 and x<=WIDTH-550) and (y <= HEIGHT-30 and y>=HEIGHT-130) and event.type == pygame.MOUSEBUTTONUP:
                        deca=1
                    
                    if deca==1:
                        window.blit(selecao_de_alvo, (WIDTH-930,HEIGHT-675 ))

                    if (x >= WIDTH-400 and x<=WIDTH-180) and (y <= HEIGHT-330 and y>=HEIGHT-600) and deca==1:
                        if event.type == pygame.MOUSEBUTTONUP and cl==0:
                            hp_l['lobo1']-=225
                            cl=1
                            deca=0
                            cont=2

                    if (x >= WIDTH-660 and x<=WIDTH-450) and (y <= HEIGHT-230 and y>=HEIGHT-480) and deca==1:
                        if event.type == pygame.MOUSEBUTTONUP and cl==0:
                            hp_l['lobo2']-=225
                            cl=1
                            cont=2

                    if (x >= WIDTH-420 and x<=WIDTH-190) and (y <= HEIGHT-30 and y>=HEIGHT-280) and deca==1:
                        if event.type == pygame.MOUSEBUTTONUP and cl==0:
                            hp_l['lobo3']-=225
                            cl=1
                            cont=2

                if wave==2:

                    (x, y)= pygame.mouse.get_pos()
                    if (x >= WIDTH-1000 and x<=WIDTH-800) and (y <= HEIGHT-30 and y>=HEIGHT-130) and event.type == pygame.MOUSEBUTTONUP:
                            if event.type == pygame.MOUSEBUTTONUP and cl==0:                        
                                hp_la['lagarto1']-=100
                                hp_la['lagarto2']-=100
                                cl=1
                                cont=2

                    if (x >= WIDTH-750 and x<=WIDTH-550) and (y <= HEIGHT-30 and y>=HEIGHT-130) and event.type == pygame.MOUSEBUTTONUP:
                        deca=1
                    
                    if deca==1:
                        window.blit(selecao_de_alvo, (WIDTH-930,HEIGHT-750 ))

                    if (x >= WIDTH-530 and x<=WIDTH-220) and (y <= HEIGHT-330 and y>=HEIGHT-580) and deca==1:
                        if event.type == pygame.MOUSEBUTTONUP and cl==0:
                            hp_la['lagarto1']-=225
                            cl=1
                            deca=0
                            cont=2

                    if (x >= WIDTH-520 and x<=WIDTH-190) and (y <= HEIGHT-30 and y>=HEIGHT-260) and deca==1:
                        if event.type == pygame.MOUSEBUTTONUP and cl==0:
                            hp_la['lagarto2']-=225
                            cl=1
                            cont=2

                
                if wave==3:
                    (x, y)= pygame.mouse.get_pos()
                    if (x >= WIDTH-1000 and x<=WIDTH-800) and (y <= HEIGHT-30 and y>=HEIGHT-130) and event.type == pygame.MOUSEBUTTONUP:
                            if event.type == pygame.MOUSEBUTTONUP and cl==0:                        
                                hp_e-=100
                                cl=1
                                cont=2

                    if (x >= WIDTH-750 and x<=WIDTH-550) and (y <= HEIGHT-30 and y>=HEIGHT-130) and event.type == pygame.MOUSEBUTTONUP:
                            if event.type == pygame.MOUSEBUTTONUP and cl==0:
                                hp_e-=225
                                cl=1
                                deca=0
                                cont=2

                if cont==2 and ani==1:
                    tempo_a=pygame.time.get_ticks()
                    ani=2
                if cont==2:
                    agora=pygame.time.get_ticks()

                    all_sprites.remove(ritsu)
                    all_sprites.add(ritsu_ani)

                    if agora-tempo_a>820:

                        all_sprites.add(ritsu)
                        all_sprites.remove(ritsu_ani)
                        tempo_a=pygame.time.get_ticks()
                        turno=2

            # Turno da Veronica----------------------------------------------------------------------------------------------------------------
            if turno==2:
                if not va:
                    if wave==3:
                        hit=0
                    ani=3
                    turno=3

                pygame.draw.polygon(window,cor,vertices1)
                pygame.draw.polygon(window,cor,vertices2)


                uppercut= font.render('Uppercut', True, (255, 255, 255 ))
                aggro= font.render('Aggro', True, (255, 255, 255 ))


                window.blit(aviso_de_ataque, (WIDTH-930,HEIGHT-175 ))
                window.blit(uppercut, (WIDTH-720,HEIGHT-95 ))
                window.blit(aggro, (WIDTH-955,HEIGHT-95))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    cl=0

                if wave==1:
                    
                    (x, y)= pygame.mouse.get_pos()

                    if (x >= WIDTH-1000 and x<=WIDTH-800) and (y <= HEIGHT-30 and y>=HEIGHT-130):
                            if event.type == pygame.MOUSEBUTTONUP and cl==0:                        
                                ag=1
                                cl=1
                                cont=3

                    if (x >= WIDTH-750 and x<=WIDTH-550) and (y <= HEIGHT-30 and y>=HEIGHT-130) and event.type == pygame.MOUSEBUTTONUP:
                        deca=1
                        ag=0
                    
                    if deca==1:
                        window.blit(selecao_de_alvo, (WIDTH-930,HEIGHT-675 ))

                    if (x >= WIDTH-400 and x<=WIDTH-180) and (y <= HEIGHT-330 and y>=HEIGHT-600) and deca==1:
                        if event.type == pygame.MOUSEBUTTONUP and cl==0:
                            hp_l['lobo1']-=175
                            cl=1
                            deca=0
                            cont=3

                    if (x >= WIDTH-660 and x<=WIDTH-450) and (y <= HEIGHT-230 and y>=HEIGHT-480) and deca==1:
                        if event.type == pygame.MOUSEBUTTONUP and cl==0:
                            hp_l['lobo2']-=175
                            cl=1
                            cont=3


                    if (x >= WIDTH-420 and x<=WIDTH-190) and (y <= HEIGHT-30 and y>=HEIGHT-280) and deca==1:
                        if event.type == pygame.MOUSEBUTTONUP and cl==0:
                            hp_l['lobo3']-=175
                            cl=1
                            cont=3

                if wave==2:

                    (x, y)= pygame.mouse.get_pos()
                    if (x >= WIDTH-1000 and x<=WIDTH-800) and (y <= HEIGHT-30 and y>=HEIGHT-130) and event.type == pygame.MOUSEBUTTONUP:
                            if event.type == pygame.MOUSEBUTTONUP and cl==0:                        
                                ag=1
                                cl=1
                                cont=3
  
                    if (x >= WIDTH-750 and x<=WIDTH-550) and (y <= HEIGHT-30 and y>=HEIGHT-130) and event.type == pygame.MOUSEBUTTONUP:
                        deca=1
                        ag=0
                    
                    if deca==1:
                        window.blit(selecao_de_alvo, (WIDTH-930,HEIGHT-750 ))

                    if (x >= WIDTH-530 and x<=WIDTH-220) and (y <= HEIGHT-330 and y>=HEIGHT-580) and deca==1:
                        if event.type == pygame.MOUSEBUTTONUP and cl==0:
                            hp_la['lagarto1']-=175
                            cl=1
                            deca=0
                            cont=3

                    if (x >= WIDTH-520 and x<=WIDTH-190) and (y <= HEIGHT-30 and y>=HEIGHT-260) and deca==1:
                        if event.type == pygame.MOUSEBUTTONUP and cl==0:
                            hp_la['lagarto2']-=175
                            cl=1
                            cont=3

                if wave==3:
                    (x, y)= pygame.mouse.get_pos()
                    if (x >= WIDTH-1000 and x<=WIDTH-800) and (y <= HEIGHT-30 and y>=HEIGHT-130) and event.type == pygame.MOUSEBUTTONUP:
                            if event.type == pygame.MOUSEBUTTONUP and cl==0:                        
                                ag=1
                                cl=1
                                hit=0
                                cont=3

                    if (x >= WIDTH-750 and x<=WIDTH-550) and (y <= HEIGHT-30 and y>=HEIGHT-130) and event.type == pygame.MOUSEBUTTONUP:
                            if event.type == pygame.MOUSEBUTTONUP and cl==0:
                                ag=0
                                hp_e-=175
                                cl=1
                                deca=0
                                hit=0
                                cont=3
                                
                if cont==3 and ani==2:
                    tempo_a=pygame.time.get_ticks()
                    ani=3

                if cont==3:

                    agora=pygame.time.get_ticks()
                    all_sprites.remove(veronica)
                    all_sprites.add(veronica_ani)

                    if agora-tempo_a>520:

                        all_sprites.add(veronica)
                        all_sprites.remove(veronica_ani)
                        turno=3

            # Turno dos inimigos-------------------------------------------------------------------------------------------------------
            # Wave dos lobos--------------------------------------------------------------------------------------------------
            if wave ==1:
                if turno==3:

                    if hp_l['lobo1']<=0:
                        ani=3 
                        hit=1
                        turno=4


                    else:

                        if va and ra and ha:
                            tg=random.randint(1, 3)
                        if (va and ha) and not ra:
                            tg=random.randint(1,3,2)
                        if(va and ra) and not ha:
                            tg=random.randint(2,3)
                        if (ra and ha) and not va:
                            tg=random.randint(1,2)
                        if ra and not (ha and va):
                            tg=2
                        if ha and not (ra and va):
                            tg=1
                        if va and not (ra and ha):
                            tg=3

                        if va and ag==1 and hit==0:
                            hp_v-=50
                            hit=1
                            cont=4
                                
                        else:
                            if tg==1 and hit==0:
                                hp_h-=50
                                hit=1
                                cont=4

                            if tg==2 and hit==0:
                                hp_r-=50
                                hit=1
                                cont=4

                            if tg==3 and hit==0:
                                hp_v-=50
                                hit=1
                                cont=4

                        if cont==4 and ani==3:
                            tempo_a=pygame.time.get_ticks()
                            ani=4

                        if cont==4:
                            agora=pygame.time.get_ticks()

                            all_sprites.remove(lobo1)
                            all_sprites.add(lobo1_ani)

                            if agora-tempo_a>520:

                                all_sprites.add(lobo1)
                                all_sprites.remove(lobo1_ani)
                                turno=4
                if turno==4:
                    if hp_l['lobo2']<=0:
                        ani=5 
                        hit=2
                        turno=5

                    if hp_l['lobo2']>0:
                                
                        if va and ra and ha:
                            tg=random.randint(1, 3)
                        if (va and ha) and not ra:
                            tg=random.randint(1,3,2)
                        if(va and ra) and not ha:
                            tg=random.randint(2,3)
                        if (ra and ha) and not va:
                            tg=random.randint(1,2)
                        if ra and not (ha and va):
                            tg=2
                        if ha and not (ra and va):
                            tg=1
                        if va and not (ra and ha):
                            tg=3

                        if va and ag==1 and hit==1:
                            hp_v-=50
                            hit=2
                            cont=5

                        else:
                            if tg==1 and hit==1:
                                hp_h-=50
                                hit=2
                                cont=5

                            if tg==2 and hit==1:
                                hp_r-=50
                                hit=2
                                cont=5

                            if tg==3 and hit==1:
                                hp_v-=50
                                hit=2
                                cont=5   

                        if cont==5 and ani==4:
                            tempo_a=pygame.time.get_ticks()
                            ani=5

                        if cont==5:
                            agora=pygame.time.get_ticks()

                            all_sprites.remove(lobo2)
                            all_sprites.add(lobo2_ani)

                            if agora-tempo_a>520:

                                all_sprites.add(lobo2)
                                all_sprites.remove(lobo2_ani)
                                turno=5

                if turno==5:

                    if hp_l['lobo3']<=0:
                        ani=0 
                        hit=0
                        turno=0

                    if hp_l['lobo3']>0:
                                
                        if va and ra and ha:
                            tg=random.randint(1, 3)
                        if (va and ha) and not ra:
                            tg=random.randint(1,3,2)
                        if(va and ra) and not ha:
                            tg=random.randint(2,3)
                        if (ra and ha) and not va:
                            tg=random.randint(1,2)
                        if ra and not (ha and va):
                            tg=2
                        if ha and not (ra and va):
                            tg=1
                        if va and not (ra and ha):
                            tg=3

                        if va and ag==1 and hit==2:
                            hp_v-=50
                            hit=0
                            cont=6

                        else:
                            if tg==1 and hit==2:
                                hp_h-=50
                                hit=0
                                cont=6

                            if tg==2 and hit==2:
                                hp_r-=50
                                hit=0
                                cont=6

                            if tg==3 and hit==2:
                                hp_v-=50
                                hit=0
                                cont=6

                        if cont==6 and ani==5:
                            tempo_a=pygame.time.get_ticks()
                            ani=0

                        if cont==6:
                            agora=pygame.time.get_ticks()

                            all_sprites.remove(lobo3)
                            all_sprites.add(lobo3_ani)

                            if agora-tempo_a>520:

                                all_sprites.add(lobo3)
                                all_sprites.remove(lobo3_ani)
                                turno=0  
                         
            # Wave dos lagartos-----------------------------------------------------------------------------------------------------------------

            if wave ==2:
                if turno==3:
                    if hp_la['lagarto1']<=0:
                        ani=3 
                        hit=1
                        turno=4

                    if hp_la['lagarto1']>0:
                        if va and ra and ha:
                            tg=random.randint(1, 3)
                        if (va and ha) and not ra:
                            tg=random.randint(1,3,2)
                        if(va and ra) and not ha:
                            tg=random.randint(2,3)
                        if (ra and ha) and not va:
                            tg=random.randint(1,2)
                        if ra and not (ha and va):
                            tg=2
                        if ha and not (ra and va):
                            tg=1
                        if va and not (ra and ha):
                            tg=3

                        if va and ag==1 and hit==0:
                            hp_v-=100
                            hit=1
                            cont=4

                        else:
                            
                            if tg==1 and hit==0:
                                hp_h-=100
                                hit=1
                                cont=4

                            if tg==2 and hit==0:
                                hp_r-=100
                                hit=1
                                cont=4

                            if tg==3 and hit==0:
                                hp_v-=100
                                hit=1
                                cont=4


                        if cont==4 and ani==3:
                            tempo_a=pygame.time.get_ticks()
                            ani=4

                        if cont==4:

                            agora=pygame.time.get_ticks()
                            all_sprites.remove(lagarto1)
                            all_sprites.add(lagarto1_ani)

                            if agora-tempo_a>520:

                                all_sprites.add(lagarto1)
                                all_sprites.remove(lagarto1_ani)
                                turno=4

                if turno==4:
                    if hp_la['lagarto2']<=0:
                        ani=0 
                        hit=0
                        turno=0

                    if hp_la['lagarto2']>0:
                            
                        if va and ra and ha:
                            tg=random.randint(1, 3)
                        if (va and ha) and not ra:
                            tg=random.randint(1,3,2)
                        if(va and ra) and not ha:
                            tg=random.randint(2,3)
                        if (ra and ha) and not va:
                            tg=random.randint(1,2)
                        if ra and not (ha and va):
                            tg=2
                        if ha and not (ra and va):
                                tg=1
                        if va and not (ra and ha):
                            tg=3
                        if va and ag==1 and hit==1:
                            hp_v-=100
                            hit=0
                            cont=5
                        
                        else:
                            if tg==1 and hit==1:
                                hp_h-=100
                                hit=0
                                cont=5

                            if tg==2 and hit==1:
                                hp_r-=100
                                hit=0
                                cont=5

                            if tg==3 and hit==1:
                                hp_v-=100
                                hit=0
                                cont=5   

                        if cont==5 and ani==4:
                            tempo_a=pygame.time.get_ticks()
                            ani=0

                        if cont==5:

                            agora=pygame.time.get_ticks()
                            all_sprites.remove(lagarto2)
                            all_sprites.add(lagarto2_ani)

                            if agora-tempo_a>520:

                                all_sprites.add(lagarto2)
                                all_sprites.remove(lagarto2_ani)
                                turno=0


            # Wave do elefante boss------------------------------------------------------------------------------------------------------    
            if wave == 3:
                if turno==3:

                    if hp_e>0:

                        if va and ag==1 and hit==0:
                            hp_v-=225
                            hit=1
                            cont=4

                        else:
                            ae=random.randint(1,2)
                            if ae==1 and hit==0:
                                hp_v-=100
                                hp_r-=100
                                hp_h-=100
                                hit=1
                                cont=4

                            if ae==2:
                                if va and ra and ha:
                                    tg=random.randint(1, 3)
                                if (va and ha) and not ra:
                                    tg=random.randint(1,3,2)
                                if(va and ra) and not ha:
                                    tg=random.randint(2,3)
                                if (ra and ha) and not va:
                                    tg=random.randint(1,2)
                                if ra and not (ha and va):
                                    tg=2
                                if ha and not (ra and va):
                                    tg=1
                                if va and not (ra and ha):
                                    tg=3
                                if tg==1 and hit==0:
                                    hp_h-=175
                                    hit=1
                                    cont=4

                                if tg==2 and hit==0:
                                    hp_r-=175
                                    hit=1
                                    cont=4

                                if tg==3 and hit==0:
                                    hp_v-=175
                                    hit=1
                                    cont=4   

                        if cont==4 and ani==3:
                            tempo_a=pygame.time.get_ticks()
                            ani=0

                        if cont==4:

                            agora=pygame.time.get_ticks()
                            all_sprites.remove(elefante)
                            all_sprites.add(elefante_ani)

                            if agora-tempo_a>520:

                                all_sprites.add(elefante)
                                all_sprites.remove(elefante_ani)
                                turno=0        
        
        if state==end:
            background_end = pygame.transform.scale(gameover, (WIDTH, HEIGHT))
            window.blit(background_end, (0, 0))
            pygame.display.flip()
            pygame.time.delay(5000)
            break
        if hp_e<=0:
            background_vit = pygame.transform.scale(Win_stat, (WIDTH, HEIGHT))
            window.blit(background_vit, (0, 0))
            pygame.display.flip()
            pygame.time.delay(5000)
            break        
        pygame.display.flip()

# Inicialização do Pygame-----------------------------------------------------------------------------------------------
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption(TITULO)

# Imprime instruções
print('*' * len(TITULO))
print(TITULO.upper())
print('*' * len(TITULO))

# Comando para evitar travamentos.
try:
    game_screen(screen)
finally:
    pygame.quit()   
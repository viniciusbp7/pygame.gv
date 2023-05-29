import pygame
from os import path

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
start=pygame.image.load("imagens/Start!.png")
hinoekagura= pygame.image.load("imagens/Hinoekagura/Hinoekagura_Base.png")
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
        self.frame_ticks = 150

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

# Classes dos inimigos---------------------------------------------------------------------------------------------

class Lobo(pygame.sprite.Sprite):
    
    # Construtor da classe. O argumento player_sheet é uma imagem contendo um spritesheet.
    def __init__(self, lobo_sheet):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Aumenta o tamanho do spritesheet para ficar mais fácil de ver
        lobo_sheet = pygame.transform.scale(lobo_sheet, (860, 230))

        # Define sequências de sprites de cada animação
        spritesheet_L = load_spritesheet(lobo_sheet, 1, 4)
        self.animations = {
            STILL: spritesheet_L[0:3]
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
            self.rect.centery = HEIGHT-395

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

    # Cria Sprite do jogador------------------------------------------------------------------------------------------------

    veronica = Veronica(veronica_sheet)
    ritsu = Ristu(ritsu_sheet)
    hinoekagura=Hinoekagura(hinoekagura_sheet)
    elefante= Elefante(elefane_sheet)
    lobo = Lobo(lobo_sheet)

    # Cria um grupo de todos os sprites do jogador-------------------------------------------------------------------------

    all_sprites = pygame.sprite.Group()
    all_sprites.add(veronica)
    all_sprites.add(ritsu)
    all_sprites.add(hinoekagura)

    
    # Inicia o loop principal do jogo------------------------------------------------------------------------------------------

    PLAYING = 0
    DONE = 1
    init = 2 
    
    hp_r=(300)
    hp_v=(450)
    hp_h=(150)
    hp_l={'lobo1':300, 'lobo2':300, 'lobo3':300}
    hp_la=(800)
    hp_e=(3000)
    pygame.mixer.music.play(loops=-1)
    state = init
    while state != DONE:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    state = DONE

        # Escreve o hp----------------------------------------------------------------------------------------------------

        font = pygame.font.SysFont(None, 48)

        # HP  dos personagens-----------------------------------------------------------------------------------------------

        HP_r= font.render(f'HP {hp_r} / 300', True, (46, 255, 0 ))
        HP_v= font.render(f'HP {hp_v} / 450' , True, (46, 255, 0 ))
        HP_h = font.render(f'HP {hp_h} / 150', True, (46, 255, 0 ))

        wave=1
        dano=1
        if state==init:
            window.blit(start,(WIDTH-540, HEIGHT-640))
            call=font.render(f'Press space!', True, (255, 255, 255 ))
            call = pygame.transform.scale(call, (600, 150))
            window.blit(call,(WIDTH-540, HEIGHT-640))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                state = PLAYING
        if state==PLAYING:
            if wave==1:

                all_sprites.add(lobo)

                # HP dos lobos (WAVE 1)---------------------------------------------------------------------------------------------

                

                HP_ene= font.render(f'HP {hp_l["lobo1"]} / 300', True, (239, 3, 3 ))
                #HP_l2= font.render(f'HP {hp_l["lobo2"]} / 300', True, (239, 3, 3 ))
                #HP_l3= font.render(f'HP {hp_l["lobo3"]} / 300', True, (239, 3, 3 ))

                hp_l["lobo1"]-=1
                

            
                window.blit(HP_ene,(WIDTH-540, HEIGHT-640))

                if hp_l['lobo1']<=0:
                    all_sprites.remove(lobo)
                    wave = 2

            # HP dos lagartos (WAVE 2)-----------------------------------------------------------------------------------------

            HP_la1= font.render(f'HP {hp_la} / 800' , True, (239, 3, 3 ))
            HP_la2= font.render(f'HP {hp_la} / 800' , True, (239, 3, 3 ))

            # HP do elefante (BOSS WAVE 3)-----------------------------------------------------------------------------------------
            if wave ==2:
                all_sprites.add(elefante)
                
                HP_ene = font.render(f'HP {hp_e} / 3000', True, (239, 3, 3 ))

                hp_e-=1

                if hp_e>0:
                    window.blit(HP_ene,(WIDTH-540, HEIGHT-640))

                if hp_e<=0:
                    all_sprites.remove(elefante)
                    

        # Atualiza a acao de cada sprite------------------------------------------------------------------------------------
        all_sprites.update()
            
            
        window.blit(background, (0, 0))
        
        if state==init:
            window.blit(start,(WIDTH-1555, HEIGHT-850))
            window.blit(call,(WIDTH-1050, HEIGHT-200))
        if state==PLAYING:
            all_sprites.draw(screen)
            window.blit(HP_r,(360, HEIGHT-460))
            window.blit(HP_v,(110, HEIGHT-380))
            window.blit(HP_h,(130, HEIGHT-730))
            window.blit(HP_ene,(WIDTH-540, HEIGHT-640))

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
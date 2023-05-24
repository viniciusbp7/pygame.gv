import pygame
from os import path

# Estabelece a pasta que contem as figuras e sons.

img_dir = path.join(path.dirname(__file__), 'imagens')

# Importa os sprites de personagens e mobs------------------------------------------------------------------------
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
STILL = 0
TITULO = 'Exemplo de Sprite Sheets e Animações'
WIDTH = window.get_width()
HEIGHT = window.get_height()
FPS = 60 # Frames por segundo
BLACK = (0, 0, 0)
background = pygame.image.load('imagens/base.webp')
hinoekagura= pygame.image.load("imagens/Hinoekagura/Hinoekagura_Base.png")
pygame.display.set_caption('Hello World!')

game=True

background = pygame.transform.scale(background, (WIDTH, HEIGHT))

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
        
        self.rect.centerx = 410
        self.rect.centery = HEIGHT-370


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

            self.rect.centerx = 400
            self.rect.centery = HEIGHT-350

class Hinoekagura(pygame.sprite.Sprite):
    
    # Construtor da classe. O argumento player_sheet é uma imagem contendo um spritesheet.
    def __init__(self, hinoekagura_sheet):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Aumenta o tamanho do spritesheet para ficar mais fácil de ver
        hinoekagura_sheet = pygame.transform.scale(hinoekagura_sheet, (860, 225))

        # Define sequências de sprites de cada animação
        spritesheet_H = load_spritesheet(hinoekagura_sheet, 1, 3)
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
        
        self.rect.centerx = 210
        self.rect.centery = HEIGHT-670


        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 280

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

            self.rect.centerx = 210
            self.rect.centery = HEIGHT-670

def game_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega spritesheet
    veronica_sheet = pygame.image.load(path.join(img_dir, 'Veronica/Veronica_spritesheet_regular.png')).convert_alpha()
    ritsu_sheet = pygame.image.load(path.join(img_dir, "Ritsu/General_Ritsu_spritesheet_regular.png")).convert_alpha()
    hinoekagura_sheet = pygame.image.load(path.join(img_dir, "Hinoekagura/Hinoekagura_spritesheet_regular.png")).convert_alpha()
    # Cria Sprite do jogador

    veronica = Veronica(veronica_sheet)
    ritsu = Ristu(ritsu_sheet)
    hinoekagura=Hinoekagura(hinoekagura_sheet)

    # Cria um grupo de todos os sprites e adiciona o jogador.

    all_sprites = pygame.sprite.Group()
    all_sprites.add(veronica)
    all_sprites.add(ritsu)
    all_sprites.add(hinoekagura)

    PLAYING = 0
    DONE = 1

    state = PLAYING
    while state != DONE:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        for event in pygame.event.get():
        # Processa os eventos (mouse, teclado, botão, etc).
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    state = DONE
    
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite. O grupo chama o método update() de cada Sprite dentre dele.
        all_sprites.update()
        
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        window.blit(background, (0, 0))
        all_sprites.draw(screen)

        # Depois de desenhar tudo, inverte o display.

        pygame.display.flip()

# Inicialização do Pygame.
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
import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange, choice

pygame.init()
pygame.mixer.init()

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagensdino')
diretorio_sons = os.path.join(diretorio_principal, 'audiodino')
#diretorio_background = os.path.join(diretorio_principal, 'dinobackground')

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
screen = pygame.image.load('imagensdino/Pixel-Art-640x480.png')
pygame.display.set_caption('DinoGame')

sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'dinoSpritesheet.png')).convert_alpha()
# convert_alpha, se a imagem possui transparencia ele vai ignorar o fundo da imagen

som_colisao = pygame.mixer.Sound(os.path.join(diretorio_sons, 'death_sound.wav'))
som_colisao.set_volume(1)

som_pontuaçao = pygame.mixer.Sound(os.path.join(diretorio_sons, 'score_sound.wav'))
som_pontuaçao.set_volume(1)

colidiu = False

escolha_obstaculo = choice([0, 1])

pontos = 0
velocidade_jogo = 10

def exibe_mensagem(msg, tamanho, cor):
    fonte = pygame.font.SysFont('Ink Free', tamanho, False, False)
    mensagem = f'{msg}'
    texto_formatado = fonte.render(mensagem, True, VERMELHO)
    return texto_formatado
class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.som_pulo = pygame.mixer.Sound(os.path.join(diretorio_sons, 'jump_sound.wav'))
        self.som_pulo.set_volume(1)
        self.imagens_dino = []
        for i in range(3):
            img = sprite_sheet.subsurface((i * 32, 0), (32, 32))  # posiçao X e Y, colocando as sprites
            img = pygame.transform.scale(img, (32 * 3, 32 * 3))  # linha para aumentar o tamanho da sprite
            self.imagens_dino.append(img)

        self.index_lista = 0
        self.image = self.imagens_dino[self.index_lista]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.pos_y_inicial = altura - 64 - 96 // 2
        self.rect.center = [100, altura - 64]  # posiçao do personagem
        self.pulo = False

    def pular(self):
        self.pulo = True
        self.som_pulo.play()

    def update(self):
        if self.pulo == True:
            if self.rect.y <= 200:
                self.pulo = False
            self.rect.y -= 20
        else:
            if self.rect.y < self.pos_y_inicial:
                self.rect.y += 20
            else:
                self.rect.y = self.pos_y_inicial

        if self.index_lista > 2:  # 2 e o indice do ultimo elemento  da pasta 'imagensdino'
            self.index_lista = 0
        self.index_lista += 0.25  # velocidade da mudança das sprites
        self.image = self.imagens_dino[int(self.index_lista)]


class Nuvens(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7 * 32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))
        self.rect = self.image.get_rect()
        self.rect.y = randrange(50, 200, 50)
        self.rect.x = largura - randrange(30, 300, 90)

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = largura
            self.rect.y = randrange(50, 200, 50)
        self.rect.x -= velocidade_jogo


class Chao(pygame.sprite.Sprite):
    def __init__(self, pos_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((6 * 32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))
        self.rect = self.image.get_rect()
        self.rect.y = altura - 64  # altura para subir colocar 90
        self.rect.x = pos_x * 64

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = largura
        self.rect.x -= 10


class Cacto(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((5 * 32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        self.rect.center = (largura, altura - 64)
        self.rect.x = largura

    def update(self):
        if self.escolha == 0:
            if self.rect.topright[0] < 0:
                self.rect.x = largura
            self.rect.x -= velocidade_jogo


class DinoVoador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_dino = []
        for i in range(3, 5):
            img = sprite_sheet.subsurface((i * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (32 * 3, 32 * 3))
            self.imagens_dino.append(img)

        self.index_lista = 0
        self.image = self.imagens_dino[self.index_lista]  ## imagens_dino
        self.mask = pygame.mask.from_surface(self.image)
        self.escolha = escolha_obstaculo
        self.rect = self.image.get_rect()
        self.rect.center = (largura, 300)
        self.rect.x = largura

    def update(self):
        if self.escolha == 1:
            if self.rect.topright[0] < 0:
                self.rect.x = largura
            self.rect.x -= velocidade_jogo

        if self.index_lista > 1:  # 2 e o indice do ultimo elemento  da pasta 'imagensdino'
            self.index_lista = 0
        self.index_lista += 0.25  # velocidade da mudança das sprites
        self.image = self.imagens_dino[int(self.index_lista)]


todas_as_sprites = pygame.sprite.Group()
dino = Dino()
todas_as_sprites.add(dino)

for i in range(0, 3):
    nuvem = Nuvens()
    todas_as_sprites.add(nuvem)

for i in range(largura * 2 // 64):
    chao = Chao(i)
    todas_as_sprites.add(chao)

cacto = Cacto()
todas_as_sprites.add(cacto)

dino_voador = DinoVoador()
todas_as_sprites.add(dino_voador)

grupo_obstaculos = pygame.sprite.Group()
grupo_obstaculos.add(cacto)
grupo_obstaculos.add(dino_voador)

relogio = pygame.time.Clock()

while True:  # parte de eventos
    tela.fill(BRANCO)
    relogio.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if dino.rect.y != dino.pos_y_inicial:
                    pass  # pass significa, nao faça nada
                else:
                    dino.pular()
    tela.blit(screen, (0, 0))

    colisoes = pygame.sprite.spritecollide(dino, grupo_obstaculos, False, pygame.sprite.collide_mask)

    todas_as_sprites.draw(tela)

    if cacto.rect.topright[0] <= 0 or dino_voador.rect.topright[0] <= 0:
        escolha_obstaculo = choice([0, 1])
        cacto.rect.x = largura
        dino_voador.rect.x = largura
        cacto.escolha = escolha_obstaculo
        dino_voador.escolha = escolha_obstaculo

    if colisoes and colidiu == False:
        som_colisao.play()
        colidiu = True

    if colidiu == True:
        if pontos % 100 == 0:
            pontos += 1
        pass
    else:
        pontos += 1
        todas_as_sprites.update()
        texto_pontos = exibe_mensagem(pontos, 30, VERMELHO)

    if pontos % 100 == 0:
        som_pontuaçao.play()
        if velocidade_jogo == 23:
            velocidade_jogo += 0
        else:
            velocidade_jogo += 1

    tela.blit(texto_pontos, (520, 30))

    pygame.display.flip()


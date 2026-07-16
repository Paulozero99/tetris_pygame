import pygame
import random
from configuracoes import *

tela_logica = pygame.Surface((LARGURA, ALTURA))
tela_janela = pygame.display.set_mode((LARGURA_JANELA, LARGURA_JANELA))

clock = pygame.time.Clock()

tempo_movimento = 0
intervalo_movimento = 800

rodando = True

while rodando:
    delta = clock.tick(60)
    tempo_movimento += delta

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()

    if tempo_movimento >= intervalo_movimento:
        tempo_movimento -= intervalo_movimento

        nova_coluna, nova_linha = bloco

        nova_linha += 1

        nova_posicao_bloco = (nova_coluna, nova_linha)
        bloco = nova_posicao_bloco

    coluna_bloco, linha_bloco = bloco

    tela_logica.fill((255, 255, 255))

    pygame.draw.rect(
        tela_logica,
        (255, 0, 0),
        (coluna_bloco * TAMANHO, linha_bloco * TAMANHO, TAMANHO, TAMANHO)
    )

    tela_redimensionada = pygame.transform.scale(tela_logica, (LARGURA_JANELA, ALTURA_JANELA))
    tela_janela.blit(tela_redimensionada, (0, 0))

    pygame.display.flip()

pygame.quit()
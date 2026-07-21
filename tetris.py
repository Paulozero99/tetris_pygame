import pygame
import random
from configuracoes import *
from desenhar_fundo import desenhar_fundo

tela_logica = pygame.Surface((LARGURA, ALTURA))
tela_janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))

clock = pygame.time.Clock()

tempo_queda = 0
intervalo_queda = 500

tempo_movimento = 0
intervalo_movimento = 150

fundo = pygame.Surface((LARGURA, ALTURA))
desenhar_fundo(fundo, limite_colunas, limite_linhas, TAMANHO)

def criar_novo_bloco():
    formatos_blocos = [
        {
            "forma": [(1, 0), (2, 0), (3, 1), (2, 1)],
            "cor": (255, 0, 0)
        },
        {
            "forma": [(0, 0), (1, 0), (0, 1), (1, 1)],
            "cor": (0, 255, 0)
        },
        {
            "forma": [(0, 0), (0, 1), (0, 2), (1, 2)],
            "cor": (0, 0, 255)
        }
    ]

    nova_peca = formatos_blocos[random.randrange(len(formatos_blocos))]

    return nova_peca

def pode_descer(bloco):
    for x, y in bloco:
        if y >= limite_linhas - 1:
            return False
        
        if tabuleiro[y + 1][x] != 0:
            return False
        
    return True

def descer(bloco):
    for i, (x, y) in enumerate(bloco):
        bloco[i] = (x, y + 1)

def pode_mover_lado(bloco, direcao):
    nova_posicao_x = x + direcao

    for x, y in bloco:
        if nova_posicao_x < 0 or nova_posicao_x >= limite_colunas - 1:
            return False
        if y >= limite_linhas - 1:
            return False
        if tabuleiro[y][nova_posicao_x] != 0:
            return False
        
    return True

def mover_lado(bloco, direcao):
    for i, (x, y) in enumerate(bloco):
        bloco[i] = (x + direcao, y)

rodando = True

while rodando:
    delta = clock.tick(60)

    tempo_queda += delta
    tempo_movimento += delta

    if jogo_comecando:
        bloco = criar_novo_bloco()
        
        tabuleiro.clear()
        tabuleiro = [[0] * 10 for _ in range(LINHAS)]

        jogo_comecando = False

    if not pode_descer(bloco["forma"]):
        for x, y in bloco["forma"]:
            tabuleiro[y][x] = bloco["cor"]

        bloco = criar_novo_bloco()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                while pode_descer(bloco["forma"]):
                    descer(bloco["forma"])
            elif event.key == pygame.K_r:
                jogo_comecando = True

    teclas = pygame.key.get_pressed()

    if tempo_movimento >= intervalo_movimento:
        tempo_movimento -= intervalo_movimento

        direcao = teclas[pygame.K_d] - teclas[pygame.K_a]

        if pode_mover_lado(bloco["forma"],direcao) and direcao != 0:
            mover_lado(bloco["forma"], direcao)

        if teclas[pygame.K_s]:
            if pode_descer(bloco["forma"]):
                descer(bloco["forma"])

    if tempo_queda >= intervalo_queda:
        tempo_queda -= intervalo_queda

        if pode_descer(bloco["forma"]):
            descer(bloco["forma"])

    tela_logica.blit(fundo, (0, 0))
    

    for y, linha in enumerate(tabuleiro):
        for x, valor in enumerate(linha):
            if valor != 0:
                pygame.draw.rect(
                    tela_logica,
                    (valor),
                    (
                        x * TAMANHO,
                        y * TAMANHO, 
                        TAMANHO, 
                        TAMANHO
                    )
                )

    for x, y in bloco["forma"]:
        pygame.draw.rect(
            tela_logica,
            (bloco["cor"]),
            (
                x * TAMANHO,
                y * TAMANHO, 
                TAMANHO, 
                TAMANHO
            )
        )

    tela_redimensionada = pygame.transform.scale(tela_logica, (LARGURA_JANELA, ALTURA_JANELA))
    tela_janela.blit(tela_redimensionada, (0, 0))

    pygame.display.flip()

pygame.quit()
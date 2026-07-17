import pygame
import random
from configuracoes import *
from desenhar_fundo import desenhar_fundo

tela_logica = pygame.Surface((LARGURA, ALTURA))
tela_janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))

clock = pygame.time.Clock()

tempo_queda = 0
intervalo_queda = 800

tempo_movimento = 0
intervalo_movimento = 300

fundo = pygame.Surface((LARGURA, ALTURA))
desenhar_fundo(fundo, limite_culunas, limite_linhas, TAMANHO)

rodando = True

while rodando:
    delta = clock.tick(60)

    tempo_queda += delta
    tempo_movimento += delta

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pode_hard_drop = True

                for x, y in bloco:
                    if y >= limite_linhas:
                        pode_hard_drop = False
                    
                if pode_hard_drop:
                    for i, (x, y) in enumerate(bloco):
                        bloco[i] = (x, limite_linhas - 1)



    teclas = pygame.key.get_pressed()

    if tempo_movimento >= intervalo_movimento:
        tempo_movimento -= intervalo_movimento
        
        nova_coluna, nova_linha = bloco[0]

        if teclas[pygame.K_a]:
            #nova_coluna -= 1
            pode_esquerda = True
            
            for x, y in bloco:
                if x - 1 < 0:
                    pode_esquerda = False
                    break
            
            if pode_esquerda:
                for i, (x, y) in enumerate(bloco):
                    bloco[i] = (x - 1, y)

        if teclas[pygame.K_d]:
            # nova_coluna += 1
            pode_direta = True
            
            for x, y in bloco:
                if x + 1 >= limite_culunas:
                    pode_direta = False
                    break

            if pode_direta:
                for i, (x, y) in enumerate(bloco):
                    bloco[i] = (x + 1, y)

        if teclas[pygame.K_s] and nova_linha < limite_linhas - 1:
            pode_descer = True
            
            for x, y in bloco:
                if y >= limite_linhas - 1:
                    pode_descer = False
                    break

            if pode_descer:
                for i, (x, y) in enumerate(bloco):
                    bloco[i] = (x, y + 1)

    if tempo_queda >= intervalo_queda:
        tempo_queda -= intervalo_queda

        pode_queda = True

        for x, y in bloco:
            if y >= limite_linhas - 1:
                pode_queda = False
                break

        if pode_queda:
            for i, (x, y) in enumerate(bloco):
                bloco[i] = (x, y + 1)

    # coluna_bloco, linha_bloco = bloco[0]

    #tela_logica.fill((100, 0, 0))
    tela_logica.blit(fundo, (0, 0))
    

    for x, y in bloco:
        pygame.draw.rect(
            tela_logica,
            (255, 0, 0),
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
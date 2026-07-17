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
                nova_coluna, nova_linha = bloco[0]

                nova_posicao_bloco = (nova_coluna, limite_linhas - 1)
                bloco[0] = nova_posicao_bloco


    teclas = pygame.key.get_pressed()

    if tempo_movimento >= intervalo_movimento:
        tempo_movimento -= intervalo_movimento
        
        nova_coluna, nova_linha = bloco[0]

        if teclas[pygame.K_a] and nova_coluna > 0:
            #nova_coluna -= 1

            i = 0

            for posicao_direita in bloco:
                if posicao_direita[0] < limite_culunas - 1:
                    bloco[i] = (posicao_direita[0] + 1, posicao_direita[1])
                
                i += 1

        if teclas[pygame.K_d]:
            # nova_coluna += 1
            i = 0

            for posicao_direita in bloco:
                if posicao_direita[0] < limite_culunas - 1:
                    bloco[i] = (posicao_direita[0] + 1, posicao_direita[1])
                
                i += 1

        if teclas[pygame.K_s] and nova_linha < limite_linhas - 1:
            # nova_linha += 1
            i = 0

            for posicao_queda in bloco:
                if posicao_queda[1] < limite_linhas - 1:
                    bloco[i] = (posicao_queda[0], posicao_queda[1] + 1)
                
                i += 1

        # nova_posicao_bloco = (nova_coluna, nova_linha)
        # bloco[0] = nova_posicao_bloco

    if tempo_queda >= intervalo_queda:
        tempo_queda -= intervalo_queda

        #nova_coluna, nova_linha = bloco[0]

        #if parte < limite_linhas - 1:
            # nova_linha += 1

        # nova_posicao_bloco = (nova_coluna, nova_linha)
        # bloco[0] = nova_posicao_bloco
        i = 0

        for posicao_queda in bloco:
            if posicao_queda[1] < limite_linhas - 1:
                bloco[i] = (posicao_queda[0], posicao_queda[1] + 1)
            
            i += 1

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
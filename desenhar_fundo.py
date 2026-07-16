import pygame

def desenhar_fundo(fundo, limite_eixo_x, limite_eixo_y, tamanho):
    for eixo_y in range(limite_eixo_y):
        for eixo_x in range(limite_eixo_x):
            if (eixo_x + eixo_y) % 2 == 0:
                pygame.draw.rect(
                    fundo,
                    (255, 255, 255),
                    (
                        eixo_x * tamanho,
                        eixo_y * tamanho,
                        tamanho,
                        tamanho
                    )
                )
            else:
                pygame.draw.rect(
                    fundo,
                    (211, 211, 211),
                    (
                        eixo_x * tamanho,
                        eixo_y * tamanho,
                        tamanho,
                        tamanho
                    )
                )

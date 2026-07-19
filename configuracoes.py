#ajuste temporario depois volta para 320 por 180
LARGURA, ALTURA = 80, 160

ESCALA = 4
LARGURA_JANELA, ALTURA_JANELA = LARGURA * ESCALA, ALTURA * ESCALA

TAMANHO = 8

limite_linhas = ALTURA // TAMANHO
limite_colunas = LARGURA // TAMANHO

bloco = [
    (4, 0),
    (5, 0),
    (6, 1),
    (5, 1)
]

tabuleiro = []

COLUNAS = 10
LINHAS = 20

for _ in range(LINHAS):
    linha = [0] * COLUNAS
    tabuleiro.append(linha)
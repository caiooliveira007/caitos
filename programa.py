import random

from funcoes import (
    preenche_frota,
    posicao_valida,
    posiciona_frota,
    monta_tabuleiros,
    faz_jogada,
    afundados
)

frota = {}

embarcacoes = [
    ["porta-aviões", 4, 1],
    ["navio-tanque", 3, 2],
    ["contratorpedeiro", 2, 3],
    ["submarino", 1, 4]
]

for embarcacao in embarcacoes:
    nome_navio = embarcacao[0]
    tamanho = embarcacao[1]
    quantidade = embarcacao[2]

    for i in range(quantidade):
        valido = False

        while not valido:
            print(
                f"Insira as informações referentes ao navio {nome_navio} "
                f"que possui tamanho {tamanho}"
            )

            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))

            if tamanho == 1:
                orientacao = "vertical"
            else:
                escolha = int(
                    input("Orientação: [1] Vertical [2] Horizontal ")
                )

                if escolha == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"

            valido = posicao_valida(
                frota, linha, coluna, orientacao, tamanho
            )

            if valido:
                frota = preenche_frota(
                    frota, nome_navio, linha, coluna, orientacao, tamanho
                )
            else:
                print("Esta posição não está válida!")

frota_oponente = {
    "porta-aviões": [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    "navio-tanque": [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    "contratorpedeiro": [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    "submarino": [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)

jogando = True

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    jogada_valida = False

    while not jogada_valida:
        linha = int(input("Jogador, qual linha deseja atacar? "))

        while linha < 0 or linha > 9:
            print("Linha inválida!")
            linha = int(input("Jogador, qual linha deseja atacar? "))

        coluna = int(input("Jogador, qual coluna deseja atacar? "))

        while coluna < 0 or coluna > 9:
            print("Coluna inválida!")
            coluna = int(input("Jogador, qual coluna deseja atacar? "))

        if tabuleiro_oponente[linha][coluna] in ["X", "-"]:
            print(
                f"A posição linha {linha} e coluna {coluna} "
                "já foi informada anteriormente!"
            )
        else:
            jogada_valida = True

    tabuleiro_oponente = faz_jogada(
        tabuleiro_oponente, linha, coluna
    )

    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False
    else:
        linha_oponente = random.randint(0, 9)
        coluna_oponente = random.randint(0, 9)

        while tabuleiro_jogador[linha_oponente][coluna_oponente] in ["X", "-"]:
            linha_oponente = random.randint(0, 9)
            coluna_oponente = random.randint(0, 9)

        print(
            f"Seu oponente está atacando na linha {linha_oponente} "
            f"e coluna {coluna_oponente}"
        )

        tabuleiro_jogador = faz_jogada(
            tabuleiro_jogador, linha_oponente, coluna_oponente
        )

        if afundados(frota, tabuleiro_jogador) == 10:
            print("Xi! O oponente derrubou toda a sua frota =(")
            jogando = False
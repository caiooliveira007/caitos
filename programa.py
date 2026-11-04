from funcoes import preenche_frota, posicao_valida

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
                escolha = int(input("[1] Vertical [2] Horizontal >"))

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

print(frota)
import os

matriz = ['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']
vitoria_Player_1 = False
vitoria_Player_2 = False


def Principal():
    global matriz
    num_max_jogada = 9
    num_jogadas_atual = 0
    rodada_jogador1 = True

    while num_jogadas_atual < num_max_jogada and vitoria_Player_1 == False and vitoria_Player_2 == False:

        PrintJogo()

        linha = int(input("Digite a linha da sua jogada: "))
        coluna = int(input("Digite a coluna da sua jogada: "))

        if matriz[linha][coluna] == 'L':
            if rodada_jogador1:
                matriz[linha][coluna] = "X"
                VerificarJogador1()
                rodada_jogador1 = False
            else:
                matriz[linha][coluna] = "O"
                rodada_jogador1 = True
                VerificarJogador2()
            num_jogadas_atual += 1

        else:
            print("Digite uma nova linha e coluna")

        CleanCode()

        if num_jogadas_atual == (num_max_jogada - 1):
            print("Jogo encerrado")

    if vitoria_Player_1:
        print("Jogador 1 venceu")
    if vitoria_Player_2:
        print("Jogador 2 venceu")

    input("Pressione para encerrar")


def PrintJogo():
    for l in range(len(matriz)):
        for c in range(len(matriz)):
            print(f"|{matriz[l][c]}|", end="")
        print()


def VerificarJogador1():
    global vitoria_Player_1
    verificarColuna = 0
    verificarLinha = 0

    if vitoria_Player_1 == False:
        for l in range(3):
            if (matriz[l][verificarColuna] == matriz[l][verificarColuna + 1] and matriz[l][verificarColuna] ==
                    matriz[l][
                        verificarColuna + 2] and matriz[l][verificarColuna] != 'L'):
                vitoria_Player_1 = True

        for c in range(3):
            if (matriz[verificarLinha][c] == matriz[verificarLinha + 1][c] and matriz[verificarLinha][c] ==matriz[verificarLinha+2][c] and matriz[verificarLinha][c] != 'L'):
                vitoria_Player_1 = True

        if matriz[verificarLinha][verificarColuna] == "X" and matriz[verificarLinha + 1][verificarColuna + 1] == "X" and \
                matriz[verificarLinha + 2][verificarColuna + 2] != 'L':
            vitoria_Player_1 = True
        if matriz[verificarLinha][verificarColuna + 2] == "X" and matriz[verificarLinha + 1][
            verificarColuna + 1] == "X" and matriz[verificarLinha + 2][
            verificarColuna] != 'L':
            vitoria_Player_1 = True


def VerificarJogador2():
    global vitoria_Player_2
    verificarColuna = 0
    verificarLinha = 0

    if vitoria_Player_2==False:
        for l in range(3):
            if matriz[l][verificarColuna] == matriz[l][verificarColuna + 1] and matriz[l][verificarColuna] == matriz[l][
            verificarColuna + 2] and matriz[l][verificarColuna] != 'L':
                vitoria_Player_2 = True

        for c in range(3):
            if (matriz[verificarLinha][c] == matriz[verificarLinha + 1][c] and matriz[verificarLinha][c] ==matriz[verificarLinha+2][c] and matriz[verificarLinha][c] != 'L'):
                vitoria_Player_2 = True

        if (matriz[verificarLinha][verificarColuna] == "O" and matriz[verificarLinha + 1][verificarColuna + 1] == "O" and matriz[verificarLinha + 2][verificarColuna + 2] != 'L'):
            vitoria_Player_2 = True

        if (matriz[verificarLinha][verificarColuna + 2] == "O" and matriz[verificarLinha + 1][verificarColuna + 1] == "O" and matriz[verificarLinha + 2][verificarColuna] != 'L'):
            vitoria_Player_2 = True


def CleanCode():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


Principal()

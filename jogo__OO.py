from Player import Player, Carta


def main():
    euro_truco()


def euro_truco():
    pontuacao_jogo = [0, 0]  # pontuacao do jogo time 1 e 2, ganha quem chegar a 12
    players = []

    quant_j = 0
    carta_virada = Carta()

    while quant_j not in (2, 4):
        quant_j = int(input("Bem vindo ao Euro Truco simulator®\n\n"
                            "A partida poderá ter 2 ou 4 jogadores no total."
                            "Antes de começar, informe a quantidade de participantes (2 ou 4): "))
        if quant_j not in (2, 4):
            print("Entrada inválida, a quantidade deve ser de 2 ou 4.\n")

    if quant_j == 2:
        print("Os jogadores 1 e 2 se enfrentarão.")
        while len(players) < 2:
            players.append(Player(input(f"\nInforme o nome do jogador(a) número {len(players) + 1}: ")))
        Player.player1.append(players[0])
        Player.player2.append(players[1])
    else:
        print("Os jogadores 1 e 2 enfrentarão os jogadores 3 e 4.")
        while len(players) < 4:
            players.append(Player(input(f"\nInforme o nome do jogador(a) número {len(players) + 1}: ")))
        players = players.insert(2, players.pop(1))  #  Ajeita na ordem de jogadores utilizado no jogo
        Player.player1.append(players[:2])
        Player.player2.append(players[2:])



    print("A partida vai começar, peguem suas CARtas e prepare-se para a batalha!")

    iniciar_jogo(players, quant_j)


def iniciar_jogo(players: list, quant_j: int, pontuacao_jogo=None, prox_jogador=[0]):
    if pontuacao_jogo is None:
        pontuacao_jogo = [0, 0]
        if quant_j == 4:
            prox_jogador = [0, 0]
    pontuacao_rodada = [0, 0]  # ganha quem chegar a 3 primeiro
    carta_virada = Carta.da_carta
    mao_de_11 = False  # com a mãe de onze True, as cartas não são mostradas nem no arquivo .txt nem no terminal.
    cont = 0

    print("\n<|##################################################################|>\n")
    while True:
        jogador_atual = ""
        # colocar quem fez a primeira na hora de marcar os pontos.
        print(f"\nPontuação da rodada: Time 1 {pontuacao_rodada[0]} x "
              f"{pontuacao_rodada[1]} Time 2")
        print("Comandos disponíveis para cada jogador:")
        mostrar_cartas_disponiveis()
        print(f"\nA carta virada é: {carta_virada}")
        cont += 1

        prox_jogador = who_play(prox_jogador)

        if True:  # mudar condição mais tarde
            print("\n<|##################################################################|>\n")
            break

    print(f"\nPontuação da partida: Time 1 {pontuacao_jogo[0]} x "
          f"{pontuacao_jogo[1]} Time 2")

    if max(pontuacao_jogo) < 12:
        if pontuacao_jogo[0] == 11 and pontuacao_jogo[1] == 11:
            mao_de_11 = True
        else:
            iniciar_jogo(players, quant_j, pontuacao_jogo)
        pass
    else:
        answer = input('Gostaria de jogar outra partida? ("S" para sim ou "N" para não): ')
        while answer.upper() not in ("S", "N"):
            answer = input('Entrada incorreta, por favor digite apenas "S" para sim ou "N" para não: ')
        print()
        main()


def congratualation(game_score: list) -> None:
    players = Player.players_name
    if game_score[0] == 12:
        if len(players) == 2:
            print(f"Parabéns {players[0]} você foi o(a) grande vencedor(a)!!!")
        else:
            print(f"Parabéns {players[0]} e {players[1]}, você venceram!")
    else:
        if len(players) == 2:
            print(f"Parabéns {players[1]} você foi o(a) grande vencedor(a)!!!")
        else:
            print(f"Parabéns {players[1][0]} e {players[1][1]}, você venceram!")


def full_round():
    pass


def jogar_carta():
    pass


def who_play(prox_jogador: list) -> list:
    pass


def verificar_quem_venceu():
    pass


def verifica_regras():
    pass


def mostrar_cartas_disponiveis():
    pass


# passar algums fuções para cá, como a de criação de baralho.

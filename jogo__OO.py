from Player import Player, Carta


def main() -> None:
    euro_truco()


def euro_truco() -> None:
    players: list = []
    quant_j: int = 0

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
        players = players.insert(2, players.pop(1))  # Ajeita na ordem de jogadores utilizado no jogo
        Player.player1.append(players[:2])
        Player.player2.append(players[2:])

    print("A partida vai começar, peguem suas CARtas e prepare-se para a batalha!")

    iniciar_jogo(players)  # termina quando alguém chegar a 12 pontos


def iniciar_jogo(players: list, prox_jogador: int = 0) -> None:
    game_score: tuple = (Player.score1, Player.score2)
    turn_card: Carta = Carta.da_carta
    mao_de_11: bool = False  # com a mãe de onze True, as cartas não são mostradas antes de jogar

    print("\n<|##################################################################|>\n")
    # colocar a parte seguinte em uma função quando terminada
    while True:
        round_score: list = [0, 0]  # ganha quem chegar a 3 primeiro
        cont: int = 0
        jogador_atual: str = ""
        # colocar quem fez a primeira na hora de marcar os pontos.
        print(f"\nPontuação da rodada: Time 1 {round_score[0]} x "
              f"{round_score[1]} Time 2")
        print("Comandos disponíveis para cada jogador:")
        mostrar_cartas_disponiveis()
        print(f"\nA carta virada é: {turn_card}")
        print("Comandos disponíveis para cada jogador:")
        [print(f"{player.name}: {player.available_cards()}") for player in players]
        print(f"\nA carta virada é: {turn_card}")





        cont += 1

        if max(round_score) == 2:  # mudar condição mais tarde

            break
    print("\n<|##################################################################|>\n")

    print(f"\nPontuação da partida: Time 1 {Player.score1} x "
          f"{game_score[1]} Time 2")

    if max(game_score) < 12:
        if game_score[0] == 11 and game_score[1] == 11:
            mao_de_11 = True
        else:
            iniciar_jogo(players, prox_jogador)
        pass
    else:
        answer: str = input('Gostaria de jogar outra partida? ("S" para sim ou "N" para não): ')
        while answer.upper() not in ("S", "N"):
            answer = input('Entrada incorreta, por favor digite apenas "S" para sim ou "N" para não: ')
        print()
        main()


def congratualation(game_score: list) -> None:
    n_players: int = len(Player.player1)
    if game_score[0] == 12:
        if n_players == 2:
            print(f"Parabéns {Player.player1[0]} você foi o(a) grande vencedor(a)!!!")
        else:
            print(f"Parabéns {Player.player1[0]} e {Player.player1[1]}, você venceram!")
    else:
        if n_players == 2:
            print(f"Parabéns {Player.player2[0]} você foi o(a) grande vencedor(a)!!!")
        else:
            print(f"Parabéns {Player.player2[0]} e {Player.player1[1]}, você venceram!")


def full_round():
    pass


def draw(scores: list) -> list:
    if sum(scores) == 0:
        return [1, 1]
    elif scores[0] == 1:
        return [2, scores[1]]
    elif scores[1] == 1:
        return [scores[0], 2]
    else:
        return [1, 1]



def jogar_carta():
    pass


def verificar_quem_venceu():
    pass


def verifica_regras():
    pass


def mostrar_cartas_disponiveis():
    pass

# passar algums fuções para cá, como a de criação de baralho.

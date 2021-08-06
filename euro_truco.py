from Player import Player
from carta import Carta


def main() -> None:
    euro_truco()


def euro_truco() -> None:
    players: list = []
    quant_j = 0
    print("============= Seja bem vindo ao =============\n"
          "=========== Euro Truco simulator® ===========\n\n")

    while quant_j not in (2, 4):
        quant_j = int(input("A partida poderá ter 2 ou 4 jogadores no total. "
                            "Antes de começar, informe a quantidade de participantes (2 ou 4): "))
        if quant_j not in (2, 4):
            print("Entrada inválida, a quantidade deve ser de 2 ou 4.\n")

    if quant_j == 2:
        print("\nOs jogadores 1 e 2 se enfrentarão.")
        while len(players) < 2:
            players.append(Player(input(f"Informe o nome do jogador(a) número {len(players) + 1}: ")))
        Player.player1.append(players[0])
        Player.player2.append(players[1])
    else:
        print("Os jogadores 1 e 2 enfrentarão os jogadores 3 e 4.")
        while len(players) < 4:
            players.append(Player(input(f"\nInforme o nome do jogador(a) número {len(players) + 1}: ")))
        players.insert(2, players.pop(1))  # Ajeita na ordem de jogadores utilizado no jogo
        Player.player1.extend(players[:2])
        Player.player2.extend(players[2:])

    print("A partida vai começar, peguem suas CARtas e prepare-se para a batalha!")

    iniciar_jogo(players)  # termina quando alguém chegar a 12 pontos


def iniciar_jogo(players: list, prox_jogador: int = 0) -> None:
    card_force = (4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, "Moles", "Espadas", "Copas", "Paus")
    manilha: int = Carta().numero   # manilha do jogo é o número da carta virada + 1

    cont_play: int = 0

    mao_de_11: bool = False  # com a mãe de onze True, as cartas não são mostradas antes de jogar

    print("\n<|##################################################################|>\n")

    # colocar a parte seguinte em uma função quando terminada
    print(f"A carta virada é: {manilha}")
    while True:  # fazer função recursiva
        winning_card: list = [0, 0]
        round_score: list = [0, 0]  # ganha quem chegar a 3 primeiro
        playing: object = ""
        cont: int = 0
        jogador_atual: str = ""
        # colocar quem fez a primeira na hora de marcar os pontos.
        # print(f"\nPontuação da rodada: Time 1 {round_score[0]} x "
        #      f"{round_score[1]} Time 2")
        # print("Comandos disponíveis para cada jogador:")
        #  cont_play

        # "while sai quanto todos jogarem da rodada de um ponto"
        index_card: int = 0 if cont_play in (0, 2) else 1
        print(cont_play)
        command: str = input(f"É a sua vez {players[cont_play].name}, "
                             f"seus comandos disponíveis são: {players[cont_play].available_cards}.\n"
                             f"Insira o comando da carta que você quer jogar: ")
        x: Carta = players[cont_play].throw_card(command)
        force = card_force.index(x.numero)
        if force > winning_card[index_card]:  # não leva em conta manilha ainda
            winning_card[index_card] = force

        if winning_card[0] > winning_card[1]:
            round_score[0] += 1
        elif winning_card[1] > winning_card[0]:
            round_score[1] += 1

        print(round_score)

        print()

        cont_play += 1
        if cont_play == len(players):
            cont_play = 0

        if max(round_score) == 2:

            break
    reset_baralho()

    print("\n<|##################################################################|>\n")

    print(f"\nPontuação da partida: Time 1 {Player.score1} x "
          f"{Player.score2} Time 2")

    if max(Player.score1, Player.score2) < 12:
        if Player.score1 == 11 and Player.score2 == 11:
            mao_de_11 = True
        else:
            iniciar_jogo(players, prox_jogador)
        pass
    else:
        if congratulation() == "S":
            main()


def congratulation() -> str:
    n_players: int = len(Player.player1)
    if Player.score1 >= 12:
        if n_players == 2:
            print(f"Parabéns {Player.player1[0]} você foi o(a) grande vencedor(a)!!!")
        else:
            print(f"Parabéns {Player.player1[0]} e {Player.player1[1]}, você venceram!")
    else:
        if n_players == 2:
            print(f"Parabéns {Player.player2[0]} você foi o(a) grande vencedor(a)!!!")
        else:
            print(f"Parabéns {Player.player2[0]} e {Player.player1[1]}, você venceram!")

    answer: str = input('Gostaria de jogar outra partida? ("S" para sim ou "N" para não): ')
    while answer.upper() not in ("S", "N"):
        answer = input('Entrada incorreta, por favor digite apenas "S" para sim ou "N" para não: ')
    print("\n\n")

    return answer


def full_round() -> None:
    """Termina quando alguém chega a 2 pontos sem empate."""
    pass


def throw_cards_complete():
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


def reset_baralho() -> None:
    Carta.baralho = [{}.fromkeys(range(1, 13), "moles"),
                       {}.fromkeys(range(1, 13), "espadas"),
                       {}.fromkeys(range(1, 13), "copas"),
                       {}.fromkeys(range(1, 13), "paus")]


def verificar_quem_venceu():
    pass


def verifica_regras():
    pass

# passar algums fuções para cá, como a de criação de baralho.


if __name__ == "__main__":
    main()

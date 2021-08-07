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
    else:
        print("Os jogadores 1 e 2 enfrentarão os jogadores 3 e 4.")
        while len(players) < 4:
            players.append(Player(input(f"\nInforme o nome do jogador(a) número {len(players) + 1}: ")))
        players.insert(2, players.pop(1))  # Ajeita na ordem de jogadores utilizado no jogo
        print()

    print("A partida vai começar, peguem suas CARtas e prepare-se para a batalha!")

    iniciar_jogo(players)  # termina quando alguém chegar a 12 pontos


def iniciar_jogo(players: list) -> None:
    manilha: int = Carta().numero  # manilha do jogo é o número da carta virada + 1

    mao_de_11: bool = False  # com a mãe de onze True, as cartas não são mostradas antes de jogar

    print("\n<|##################################################################|>\n")

    print(f"A carta virada é o: {manilha}")

    full_round(players)
    reset_baralho_and_cards(players)

    print("\n<|##################################################################|>\n")

    print(f"\nPontuação da partida: Time_1 {Player.score1} x "
          f"{Player.score2} Time_2\n")

    if max(Player.score1, Player.score2) < 12:
        if Player.score1 == 11 and Player.score2 == 11:
            mao_de_11 = True
        else:
            iniciar_jogo(players)
        pass
    else:
        if congratulation() == "S":
            main()


def full_round(players: list, cont=0, winning_card=0, round_score=0) -> int:
    """Termina quando alguém chega a 2 pontos sem empate."""
    if cont == 0:
        winning_card: list = [0, 0]
        round_score: list = [0, 0]  # ganha quem chegar a 3 pontos primeiro

    cont_play = Player.cont_play

    # "while sai quanto todos jogarem da rodada de um ponto"
    index_card: int = 0 if cont_play in (0, 2) else 1
    # print(cont_play)  # debug
    # print(players)
    command: str = input(f"É a sua vez {players[cont_play].name}, "
                         f"seus comandos disponíveis são: {players[cont_play].available_cards}.\n"
                         f"Insira o comando da carta que você quer jogar: ")
    x: Carta = players[cont_play].throw_card(command)
    force = Carta.card_force.index(x.numero)
    if force > winning_card[index_card]:  # não leva em conta manilha ainda
        winning_card[index_card] = force

    if cont % 2 == 1:
        round_score = round_winner(winning_card, round_score)

    # print(round_score)  # debug

    print()

    cont_play += 1
    cont += 1

    if cont_play == len(players):
        cont_play = 0

    if max(round_score) >= 2:  # sem truco ainda
        if round_score[0] >= 2:
            Player.score1 += 1
        else:
            Player.score2 += 1
        return cont_play
    Player.cont_play = cont_play
    full_round(players, cont, winning_card, round_score)


def round_winner(winning_card: list, round_score: list) -> list:
    if winning_card[0] > winning_card[1]:
        round_score[0] += 1
        x: int = len(Player.players)
        name: str = Player.players[0] if x == 2 else " e ".join(Player.players)
        print(f"{name} ganh{'ou' if x == 2 else 'aram'} 1 ponto")
    elif winning_card[1] > winning_card[0]:
        round_score[1] += 1
        x: int = len(Player.players)
        name: str = Player.players[1] if x == 2 else " e ".join(Player.players)
        print(f"{name} ganh{'ou' if x == 2 else 'aram'} 1 ponto!\n")
    return round_score


def congratulation() -> str:
    if len(Player.players) == 2:
        p1 = Player.players[0] if Player.score1 >= 12 else Player.players[1]
        print(f"Parabéns {p1} você foi o(a) grande vencedor(a)!!!")
    else:
        p1 = Player.players[0] if Player.score1 >= 12 else Player.players[2]
        p2 = Player.players[1] if Player.score1 >= 12 else Player.players[3]
        print(f"Parabéns {p1} e {p2}, você venceram!!!")

    answer: str = input('Gostaria de jogar outra partida? ("S" para sim ou "N" para não): ')
    while answer.upper() not in ("S", "N"):
        answer = input('Entrada incorreta, por favor digite apenas "S" para sim ou "N" para não: ')
    print("\n\n")

    return answer


def draw(scores: list) -> list:
    if sum(scores) == 0:
        return [1, 1]
    elif scores[0] == 1:
        return [2, scores[1]]
    elif scores[1] == 1:
        return [scores[0], 2]
    else:
        return [1, 1]


def reset_baralho_and_cards(players) -> None:
    Carta.baralho = [{}.fromkeys(range(1, 13), "moles"),
                     {}.fromkeys(range(1, 13), "espadas"),
                     {}.fromkeys(range(1, 13), "copas"),
                     {}.fromkeys(range(1, 13), "paus")]
    for player in players:
        player.carta_a = Carta()
        player.carta_b = Carta()
        player.carta_c = Carta()
        player.available_cards = ["A", "B", "C"]


def verificar_quem_venceu():
    pass


def verifica_regras():
    pass


# passar algums fuções para cá, como a de criação de baralho.


if __name__ == "__main__":
    main()

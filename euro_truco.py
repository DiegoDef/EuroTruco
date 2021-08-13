from Player import Player
from carta import Carta


def main() -> None:
    import platform

    os = platform.system()
    if os not in ("Linux", "Windows"):
        print("\nO Euro truco não é compatível com o seu sistema operacional.")
        exit()

    euro_truco()


def euro_truco() -> None:
    players: list = []
    quant_j = 0
    print("============= Seja bem vindo ao =============\n"
          "=========== Euro Truco simulator® ===========\n\n")

    """while quant_j not in (2, 4):
        quant_j = int(input("A partida poderá ter 2 ou 4 jogadores no total. "
                            "Antes de começar, informe a quantidade de participantes (2 ou 4): "))
        if quant_j not in (2, 4):
            print("Entrada inválida, a quantidade deve ser de 2 ou 4.\n")
"""
    quant_j = 2  # remover mais tarde
    if quant_j == 2:
        """print("\nOs jogadores 1 e 2 se enfrentarão.")"""
        while len(players) < 2:
            players.append(Player(input(f"Informe o nome do jogador(a) número {len(players) + 1}: ")))
    else:
        print("Os jogadores 1 e 2 enfrentarão os jogadores 3 e 4.")
        while len(players) < 4:
            players.append(Player(input(f"\nInforme o nome do jogador(a) número {len(players) + 1}: ")))
        players.insert(2, players.pop(1))  # Ajeita na ordem de jogadores utilizado no jogo
        print()
    write_cards(players)

    print("\nA partida vai começar, peguem suas CARtas e prepare-se para a batalha!")
    start_round(players)  # termina quando alguém chegar a 12 pontos


def start_round(players: list) -> None:
    manilha: int = Carta().numero  # manilha do jogo é o número da carta virada + 1

    mao_de_11: bool = False  # com a mãe de onze True, as cartas não são mostradas antes de jogar

    print("\n|##################################################################|>\n")

    print(f"A carta virada é: {manilha}\n")
    full_round_up_to_2_points(players)
    reset_baralho_and_cards(players)

    print(f"\nPontuação total da partida: Time_1 {Player.score1} x "
          f"{Player.score2} Time_2\n")

    if max(Player.score1, Player.score2) < 12:
        if Player.score1 == 11 and Player.score2 == 11:
            mao_de_11 = True
        else:
            start_round(players)
    else:
        if congratulation() == "S":
            main()


def full_round_up_to_2_points(players: list, count: int = 0, winning_card: int = 0,
                              round_score: int = 0, next_player: int = 0):
    """Termina quando alguém chega a 2 pontos ou mais quando em truco"""
    count_play = Player.count_play
    if count == 0:
        winning_card: list = [0, 0]
        round_score: list = [0, 0]  # ganha quem chegar a 3 pontos primeiro
        next_player: list = [[0, 0], [0, 0]]

    # "while sai quanto todos jogarem da rodada de um ponto"

    # print(count_play)  # debug
    # print(players)
    command: str = input(f"É a sua vez {players[count_play].name}, "
                         f"seus comandos disponíveis são: {players[count_play].available_cards}.\n"
                         f"Insira o comando da carta que você quer jogar: ")
    x: Carta = players[count_play].throw_card(command)
    index_card: int = 0 if count_play in (0, 2) else 1
    force: int = Carta.card_force.index(x.numero)
    if force > winning_card[index_card]:  # não leva em conta manilha ainda
        winning_card[index_card] = force
        next_player[index_card] = [count_play, count]  # index do 1º player da proxima rodada
        if count == 1:
            Player.first_score = winning_card

    print(winning_card, round_score, next_player)
    if count % 2 == 1 and len(players) == 2:
        winning_card, round_score = round_winner(winning_card, round_score)
    elif count % 4 == 1 and len(players) == 4:
        winning_card, round_score = round_winner(winning_card, round_score)

    print(round_score)  # debug

    print()

    count_play += 1
    count += 1

    if count_play == len(players):
        count_play = 0

    if max(round_score) >= 2:  # sem truco ainda
        if round_score[0] >= 2:
            Player.score1 += 1
        else:
            Player.score2 += 1
        Player.count_play = next_player_index(next_player, round_score)
    else:
        Player.count_play = count_play
        full_round_up_to_2_points(players, count, winning_card, round_score, next_player)


def round_winner(winning_card: list, round_score: list) -> tuple:
    if sum(round_score) == 0:
        Player.first_score = round_score
    if winning_card[0] > winning_card[1]:
        round_score[0] += 1
        x: int = len(Player.players)
        name: str = Player.players[0] if x == 2 else " e ".join(Player.players[:2])
        print(f"{name} ganh{'ou' if x == 2 else 'aram'} 1 ponto")
    elif winning_card[1] > winning_card[0]:
        round_score[1] += 1
        x: int = len(Player.players)
        name: str = Player.players[1] if x == 2 else " e ".join(Player.players[2:])
        print(f"{name} ganh{'ou' if x == 2 else 'aram'} 1 ponto!\n")
    else:
        print("empate")  # debug
        round_score = draw(round_score)
    winning_card = [0, 0]
    return winning_card, round_score


def draw(scores: list) -> list:  # draw completo sem testes profundos e truco
    if sum(scores) == 0:
        print("Deu empate! Quem ganhar a próxima será o vencedor.\n")
        return [1, 1]
    elif scores[0] == 1 and scores[1] == 0:
        return [2, scores[1]]
    elif scores[1] == 1 and scores[0] == 0:
        return [scores[0], 2]
    else:
        n = Player.first_score
        if n[0] == n[1]:
            print("Deu empate! Quem ganhar a próxima será o vencedor.\n")
            return [1, 1]
        else:
            if n[0] > n[1]:
                scores[0] += 1
                x: int = len(Player.players)
                name: str = Player.players[0] if x == 2 else " e ".join(Player.players[:2])
                print(f"{name} ganh{'ou' if x == 2 else 'aram'} 1 ponto")
                return scores
            scores[1] += 1
            x: int = len(Player.players)
            name: str = Player.players[1] if x == 2 else " e ".join(Player.players[2:])
            print(f"{name} ganh{'ou' if x == 2 else 'aram'} 1 ponto!\n")
            return scores


def next_player_index(next_player: list, round_score) -> list:
    if round_score[0] > round_score[1]:
        return next_player[0][0]
    elif round_score[1] > round_score[0]:
        return next_player[1][0]
    next1 = next_player[0][0]
    next2 = next_player[1][0]
    return next1 if next_player[0][1] > next_player[1][1] else next2


def congratulation() -> str:
    print("\n<|##################################################################|>\n")

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


def reset_baralho_and_cards(players) -> None:
    truco_numbers = list(range(1, 8)) + list(range(10, 13))
    Carta.baralho = [{}.fromkeys(truco_numbers, "moles"),
                     {}.fromkeys(truco_numbers, "espadas"),
                     {}.fromkeys(truco_numbers, "copas"),
                     {}.fromkeys(truco_numbers, "paus")]
    for player in players:
        player.carta_a = Carta()
        player.carta_b = Carta()
        player.carta_c = Carta()
        player.available_cards = ["A", "B", "C"]
    write_cards(players)


def write_cards(players):
    import platform

    os = platform.system()
    if os == "Linux":
        path = "cartas/"
    else:
        path = "cartas\\"
    print(path)

    for player in players:
        with open(path + f"{player.name}.txt", "w") as p:
            p.write(f"Olá {player.name}! Suas cartas estão logo abaixo. Boa sorte!\n\n"
                    f"A: {player.carta_a.numero} de {player.carta_a.naipe}\n"
                    f"B: {player.carta_b.numero} de {player.carta_b.naipe}\n"
                    f"C: {player.carta_c.numero} de {player.carta_c.naipe}\n")
        print(player)  # debug


def verificar_quem_venceu():
    pass


def verifica_regras():
    pass


# passar algums fuções para cá, como a de criação de baralho.


if __name__ == "__main__":
    main()

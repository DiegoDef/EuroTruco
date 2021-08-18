from models.player import Player
from models.carta import Carta


def main() -> None:
    import platform
    os = platform.system()
    if os not in ("Linux", "Windows"):
        print("\nO Euro truco não é compatível com o seu sistema operacional.")
        exit()
    euro_truco()


def euro_truco() -> None:
    players: list = []
    print("============= Seja bem vindo ao =============\n"
          "=========== Euro Truco simulator® ===========\n\n")

    num_players: str = input("A partida poderá ter 2 ou 4 jogadores no total. "
                             "Antes de começar, informe a quantidade de participantes (2 ou 4): ")
    if num_players.upper() != "Q":
        num_players = int(num_players)
        while num_players not in (2, 4):
            if num_players not in (2, 4):
                print("Entrada inválida, a quantidade deve ser de 2 ou 4.\n")
                num_players

        if num_players == 2:
            print("\nOs jogadores 1 e 2 se enfrentarão.")
            while len(players) < 2:
                players.append(Player(input(f"Informe o nome do jogador(a) número {len(players) + 1}: ")))
        else:
            print("Os jogadores 1 e 2 enfrentarão os jogadores 3 e 4.")
            while len(players) < 4:
                players.append(Player(input(f"\nInforme o nome do jogador(a) número {len(players) + 1}: ")))
            players.insert(2, players.pop(1))  # Ajeita na ordem de jogadores utilizado no jogo
            print()
    else:
        #  inicio de ações de desenvolvedor
        print("Informe o nome do jogador(a) número 1: Diego\n"
              "Informe o nome do jogador(a) número 2: Michele")
        players.append(Player("Diego"))
        players.append(Player("michele"))
        if input().upper() == "Q":
            print("Apenas números:")
            for p in players:
                developer(p, *(input("Carta 1: "), input("Carta 2: "), input("Carta 3: ")))
            Player.score1 = int(input("Score 1: "))
            Player.score2 = int(input("Score 1: "))
            print()

        #  final
    write_cards(players)
    print("As CARtas de todos os jogadores foram gravadas em .txt "
          "na pasta 'cartas' com o nome de cada um dos jogadores.\n"
          "Cada jogador deve ter acesso apenas ao seu arquivo.\n"
          "A cada rodada o arquivo é atualizado com as novas CARtas.")

    print("\nA partida vai começar, peguem suas CARtas e prepare-se para a batalha!")
    start_round(players)  # termina quando alguém chegar a 12 pontos


def developer(player, *args) -> None:
    player.carta_a.numero = args[0]
    player.carta_b.numero = args[1]
    player.carta_c.numero = args[2]


def start_round(players: list, mao_de_11: bool = False) -> None:
    print("\n|##################################################################|>\n")

    print(f"A carta virada é: {Player.manilha.numero}\n")
    full_round_up_to_2_points(players, mao_de_11)
    reset_all(players)

    print(f"\nPontuação total da partida: Time_1 {Player.score1} x "
          f"{Player.score2} Time_2\n")

    if max(Player.score1, Player.score2) < 12:
        if Player.score1 == 11 and Player.score2 == 11:
            mao_de_11 = True  # com a mãe de onze True, as cartas não são mostradas antes de jogar
            start_round(players, mao_de_11)
        else:
            start_round(players)
    else:
        if congratulations() == "S":
            main()


def full_round_up_to_2_points(players: list, mao_de_11: bool = False, round_score=None) -> None:
    """Termina quando alguém chega a 2 pontos ou mais quando em truco"""
    if round_score is None:
        round_score = [0, 0]
        Player.count_play_round = Player.count_play_start
        Player.count_play_start += 1
    num_players: int = len(players)
    count_play: int = Player.count_play_round
    winning_card: list = [[-1, 0, 0], [-1, 0, 0]]  # [forca_carta, forca_naipe, count
    count = 0

    #  round_score: list = [0, 0]  # ganha quem chegar a 2 pontos primeiro
    #  next_player: list = [[0, 0], [0, 0]]

    # "while sai quanto todos jogarem da rodada de um ponto"
    while count < num_players:
        #  print(count, len(players))  # debug
        # print(players)
        index_p = count_play % num_players
        player: Player = players[index_p]
        command: str = input(f"É a sua vez {player.name}, "
                             f"seus comandos disponíveis são: {player.available_cards}.\n"
                             f"Insira o comando da sua carta ou peça truco: ").upper()
        x, command = player.play_card(command, mao_de_11)
        index_card: int = 0 if index_p in (0, 2) else 1
        Player.played_cards[index_p].append(command)
        force: tuple = card_force(x, count_play)
        if force[0] > winning_card[index_card][0]:
            winning_card[index_card] = force

        print(winning_card, round_score)

        print()

        count += 1
        count_play += 1
        Player.count_play_round = count_play
    #if True:
    #    mao_de_onze(cards, players)

    winning_card, round_score = round_winner(winning_card, round_score)  # tirar winning card

    print(round_score)

    if max(round_score) >= 2:
        if mao_de_11 is True:
            mao_de_onze(players)
        give_points(round_score)
    else:
        Player.count_play = count_play
        full_round_up_to_2_points(players, mao_de_11, round_score)


def give_points(round_score) -> None:
    points = Player.truco_points[1]
    if round_score[0] >= 2:
        Player.score1 += points
    else:
        Player.score2 += points


def mao_de_onze(players: list):
    count = 0
    cards: list = Player.played_cards
    for player in players:
        print(f"O(A) jogador(a) {player.name} jogou as seguintes cartas, em ordem de jogada: ")
        card_commands: dict = {"A": player.carta_a, "B": player.carta_b, "C": player.carta_c}
        print("C", count)
        for c, y in zip(cards[count], range(len(cards[count]))):
            card = card_commands[c]
            print(f"CARta {y+1}: {card.numero} de {card.naipe}")
        print()
        count += 1


def card_force(card: Carta, count_play: int) -> tuple:
    manilha: Carta = Player.manilha
    num = manilha.numero
    if num not in (7, 12):  # numero da manilha é + 1 que a carta virada com exceção em 12 e 7
        manilha: int = num + 1
    else:
        manilha: int = 10 if num == 7 else 1

    force = Carta.card_force
    if card.numero != manilha:
        print(card.numero, card.naipe)
        return force.index(card.numero), force.index(card.naipe), count_play
    else:
        print("Você jogou o coringa!!!\n")
        return 10, force.index(card.naipe), count_play


def round_winner(winning_card: list, round_score: list) -> tuple:
    card_1: int = winning_card[0][0]
    card_2: int = winning_card[1][0]
    if card_1 == 10 and card_2 == 10:  # se os dois tem força 10 então é manilha e devem ser decididos por naipe
        force_1 = winning_card[0][1]
        force_2 = winning_card[1][1]
        card_1 = 11 if force_1 > force_2 else 9

    if card_1 > card_2:
        if not any(round_score):
            Player.first_score = [1, 0]
        round_score[0] += 1
        x: int = len(Player.players)
        name: str = Player.players[0] if x == 2 else " e ".join(Player.players[:2])
        print(f"{name} ganh{'ou' if x == 2 else 'aram'} 1 ponto")
        Player.count_play_round = winning_card[0][2]
    elif card_2 > card_1:
        if not any(round_score):
            Player.first_score = [0, 1]
        round_score[1] += 1
        x: int = len(Player.players)
        name: str = Player.players[1] if x == 2 else " e ".join(Player.players[2:])
        print(f"{name} ganh{'ou' if x == 2 else 'aram'} 1 ponto!\n")
        Player.count_play_round = winning_card[1][2]
    else:
        index1: int = winning_card[0][2]
        index2: int = winning_card[1][2]
        Player.count_play_round = index1 if index1 > index2 else index2  # quem empachou começa o próximo round
        round_score = draw(round_score)
    winning_card = [[-1, 0, 0], [-1, 0, 0]]
    return winning_card, round_score


def draw(scores: list) -> list:  # draw completo sem testes profundos e truco
    if not any(scores):
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
                plural = ('ou' if x == 2 else 'aram', "s" if Player.truco_points > 1 else "")
                print(f"%s ganh%s 1 ponto%s" % (name, plural[0], plural[1]))
                return scores
            scores[1] += 1
            x: int = len(Player.players)
            name: str = Player.players[1] if x == 2 else " e ".join(Player.players[2:])
            print(f"{name} ganh{'ou' if x == 2 else 'aram'} 1 ponto!\n")
            return scores


def congratulations() -> str:
    print("\n<|##################################################################|>\n")

    if len(Player.players) == 2:
        p1 = Player.players[0] if Player.score1 >= 12 else Player.players[1]
        print(f"Parabéns {p1} você foi o(a) grande vencedor(a)!!!\n")
    else:
        p1 = Player.players[0] if Player.score1 >= 12 else Player.players[2]
        p2 = Player.players[1] if Player.score1 >= 12 else Player.players[3]
        print(f"Parabéns {p1} e {p2}, você venceram!!!\n")

    answer: str = input('Gostaria de jogar outra partida? ("S" para sim ou "N" para não): ').upper()
    while answer.upper() not in ("S", "N"):
        answer = input('Entrada incorreta, por favor digite apenas "S" para sim ou "N" para não: ').upper()
    print("\n\n")

    return answer


def reset_all(players) -> None:
    truco_numbers = list(range(1, 8)) + list(range(10, 13))
    Carta.baralho = [{}.fromkeys(truco_numbers, "moles"),
                     {}.fromkeys(truco_numbers, "espadas"),
                     {}.fromkeys(truco_numbers, "copas"),
                     {}.fromkeys(truco_numbers, "paus")]
    Player.manilha = Carta()  # reseta manilha da partida
    for player in players:
        player.carta_a = Carta()
        player.carta_b = Carta()
        player.carta_c = Carta()
        player.available_cards = ["A", "B", "C"]
    write_cards(players)
    Player.truco_points = [-1, 1]


def write_cards(players) -> None:
    import platform

    os = platform.system()
    if os == "Linux":
        path = "cartas/"
    else:
        path = "cartas\\"

    for player in players:
        with open(path + f"{player.name}.txt", "w") as p:
            p.write(f"Olá {player.name}! Suas cartas estão logo abaixo. Boa sorte!\n\n"
                    f"A: {player.carta_a.numero} de {player.carta_a.naipe}\n"
                    f"B: {player.carta_b.numero} de {player.carta_b.naipe}\n"
                    f"C: {player.carta_c.numero} de {player.carta_c.naipe}\n")
        print(player)  # debug


if __name__ == "__main__":
    main()

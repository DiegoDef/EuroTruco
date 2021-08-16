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
    mao_de_11: bool = False  # com a mãe de onze True, as cartas não são mostradas antes de jogar

    print("\n|##################################################################|>\n")

    print(f"A carta virada é: {Player.manilha.numero}\n")
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


def full_round_up_to_2_points(players: list, round_score=None):
    """Termina quando alguém chega a 2 pontos ou mais quando em truco"""
    if round_score is None:
        round_score = [0, 0]
        Player.count_play_round = Player.count_play_start
        Player.count_play_start += 1
    count_play: int = Player.count_play_round
    winning_card: list = [[-1, 0, 0], [-1, 0, 0]]  #  [forca_carta, forca_naipe,
    count = 0
    #  round_score: list = [0, 0]  # ganha quem chegar a 2 pontos primeiro
    #  next_player: list = [[0, 0], [0, 0]]
    num_players: int = len(players)

    # "while sai quanto todos jogarem da rodada de um ponto"
    while count < len(players):
        print(count, len(players))  # debug
        # print(players)
        index_p = count_play % num_players
        player: Player = players[index_p]
        command: str = input(f"É a sua vez {player.name}, "
                             f"seus comandos disponíveis são: {player.available_cards}.\n"
                             f"Insira o comando da carta que você quer jogar: ")

        x: Carta = player.throw_card(command)
        index_card: int = 0 if index_p in (0, 2) else 1
        force: tuple = card_force(x, count_play)
        print("forceW: ", force, winning_card, "\n")
        if force[0] > winning_card[index_card][0]:
            winning_card[index_card] = force
            #  next_player[index_card] = [count_play, count]  # index do 1º player da proxima rodada, acho que está errado

        print(winning_card, round_score)

        print()

        count += 1
        count_play += 1
        Player.count_play_round = count_play

    winning_card, round_score = round_winner(winning_card, round_score)  # tirar winning card

    print(round_score)

    if max(round_score) >= 2:  # sem truco ainda
        if round_score[0] >= 2:
            Player.score1 += 1
        else:
            Player.score2 += 1
        #Player.count_play = next_player_index(next_player, round_score)
    else:
        Player.count_play = count_play
        full_round_up_to_2_points(players, round_score)

    '''    # problema esta aqui %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        if count % 2 == 0 and num_players == 2:  # verificar a precisão desses dois
            winning_card, round_score = round_winner(winning_card, round_score)
        elif count % 4 == 0 and num_players == 4:
            winning_card, round_score = round_winner(winning_card, round_score)

        print(round_score)  # debug
    '''


def card_force(card: Carta, count_play: int):
    manilha: Carta = Player.manilha
    num = manilha.numero
    if num not in (7, 12):  # numero da manilha é + 1 que a carta virada com exceção em 12 e 7
        manilha: int = num + 1
    else:
        manilha: int = 10 if num == 7 else 1

    force = Carta.card_force
    if card.numero != manilha:
        return force.index(card.numero), force.index(card.naipe), count_play
    else:
        print("Você jogou o coringa!!!\n")
        return 10, force.index(card.naipe), count_play


def round_winner(winning_card: list, round_score: list) -> tuple:
    card_1 = winning_card[0][0]
    card_2 = winning_card[1][0]
    if card_1 == 10 and card_2 == 10:  # se os dois tem força 10 então é manilha e devem ser decididos por naipe
        force_1 = winning_card[0][1]
        force_2 = winning_card[1][1]
        card_1 = 11 if force_1 > force_2 else 0

    if card_1 > card_2:
        if not any(round_score):  # n resolveu o problema ###########################################################################################
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
        print("empate")  # debug
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
                print(f"{name} ganh{'ou' if x == 2 else 'aram'} 1 ponto")
                return scores
            scores[1] += 1
            x: int = len(Player.players)
            name: str = Player.players[1] if x == 2 else " e ".join(Player.players[2:])
            print(f"{name} ganh{'ou' if x == 2 else 'aram'} 1 ponto!\n")
            return scores


def next_player_index(next_player: list, round_score) -> list:  # verificar se funciona com 4  REMOVER
    next1 = next_player[0][0] + 1  # +1 pois
    next2 = next_player[1][0] + 1
    r1 = round_score[0]
    r2 = round_score[1]
    if r1 != r2:
        return next1 if r1 > r2 else next2
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
    Player.manilha = Carta()  # reseta manilha da partida
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

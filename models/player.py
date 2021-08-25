from models.carta import Carta


class Player:
    players: list = []
    score1: int = 0  # pontuacao do jogo time 1 e 2, ganha quem chegar a 12
    score2: int = 0
    count_play_start: int = 0  # index do próximo jogador no inicio da rodada
    count_play_round: int = 0  # index do próximo jogador ao decorrer da rodada
    truco_points: list = [-1, 1]  # [who asked to truco=0 or 1, points=[1, 3 or 6 or 9 or 12]
    played_cards: list = [[], [], [], []]

    first_score = [0, 0]
    manilha: Carta = Carta()

    def __init__(self, player_name: str) -> None:
        self.__name: str = player_name
        self.__carta_a: Carta = Carta()
        self.__carta_b: Carta = Carta()
        self.__carta_c: Carta = Carta()
        self.__available_cards: list = ["A", "B", "C"]
        Player.players.append(player_name)

    def throw_card(self, id_carta: str = "", mao_de_onze: bool = False) -> tuple:
        if id_carta == "":
            id_carta = input("Insira o comando da sua carta: ")
        cartas: dict = {"A": self.__carta_a, "B": self.__carta_b, "C": self.__carta_c}
        id_carta = id_carta.upper()

        while id_carta not in self.__available_cards:
            if id_carta.upper() in ("TRUCO", "6", "9", "12"):
                self.ask_truco(id_carta)
                id_carta = input("Insira o comando da sua carta ou peça truco: ").upper()
            else:
                id_carta = input(f"CARta não disponível para uso, peça truco ou escolha uma CARta entre "
                                 f"as seguintes opções: {', '.join(self.__available_cards)}: ").upper()
            print()
        self.__available_cards.remove(id_carta)
        card: Carta = cartas[id_carta]
        if not mao_de_onze:
            print(f"Você jogou a CARta {card.numero} de {card.naipe}\n")
        return card, id_carta

    def ask_truco(self, ask: str) -> None:
        truco_points = Player.truco_points[1]
        ask = ask.upper()
        players = Player.players
        index = players.index(self.name)
        if len(players) == 2:
            if index == Player.truco_points[0]:
                print("Apenas o outro time pode pedir truco.")
                return None
        else:
            index = 0 if index == 0 or index == 1 else 1
            if index == Player.truco_points[0]:
                print("Apenas o outro time pode pedir truco.")
                return None

        if ask == "TRUCO":
            if truco_points == 1:
                Player.truco_points = [index, 3]
                print("Agora a partida está valendo 3 pontos!\n")
            else:
                has_s = "s" if truco_points > 1 else ""
                print("Impossível pedir truco, a partida está valendo %s ponto%s." % (truco_points, has_s))
        elif int(ask) - 3 == truco_points:
            Player.truco_points = [index, int(ask)]
            print(f"Agora a partida está valendo {ask} pontos!\n")
        else:
            has_s = "s" if truco_points > 1 else ""
            print("Impossível pedir truco, a partida está valendo %s ponto%s." % (truco_points, has_s))

    @property
    def available_cards(self):
        return ', '.join(self.__available_cards)

    @property
    def name(self):
        return self.__name

    @property
    def carta_a(self):
        return self.__carta_a

    @property
    def carta_b(self):
        return self.__carta_b

    @property
    def carta_c(self):
        return self.__carta_c

    @available_cards.setter
    def available_cards(self, value: list):
        self.__available_cards = value

    @carta_a.setter
    def carta_a(self, value):
        self.__carta_a = value

    @carta_b.setter
    def carta_b(self, value):
        self.__carta_b = value

    @carta_c.setter
    def carta_c(self, value):
        self.__carta_c = value

    def __str__(self):
        return f"Nome: {self.__name}\nCARtas: {self.carta_a.numero} de {self.carta_a.naipe}, " \
               f"{self.carta_b.numero} de {self.carta_b.naipe} e {self.carta_c.numero} de {self.carta_c.naipe}"

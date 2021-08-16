from carta import Carta


class Player:
    players = []
    score1 = 0  # pontuacao do jogo time 1 e 2, ganha quem chegar a 12
    score2 = 0
    count_play_start = 0  # index do próximo jogador no inicio da rodada
    count_play_round = 0  # index do próximo jogador ao decorrer da rodada

    first_score = [0, 0]
    manilha: Carta = Carta()

    def __init__(self: object, player_name: str):
        self.__name: str = player_name
        self.__carta_a: Carta = Carta()
        self.__carta_b: Carta = Carta()
        self.__carta_c: Carta = Carta()
        self.__available_cards: list = ["A", "B", "C"]
        Player.players.append(player_name)

    def throw_card(self, id_carta):
        cartas = {"A": self.__carta_a, "B": self.__carta_b, "C": self.__carta_c}
        id_carta = id_carta.upper()

        while id_carta not in self.__available_cards:
            id_carta = input(f"CARta {id_carta} não disponível para uso, escolha uma CARta entre "
                             f"as seguintes opções: {', '.join(self.__available_cards)}: ").upper()
            print()
        self.__available_cards.remove(id_carta)
        card: Carta = cartas[id_carta]
        print(f"Você jogou a CARta {card.numero} de {card.naipe}\n")
        return card

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


if __name__ == "__main__":
    pessoa = Player("Rodrigo")
    print(pessoa.available_cards)
    Player.player1 = "Alan"
    s = Player.count_play_start
    s += 1
    Player.count_play_start += 1
    print(Player.count_play_start)
    # print(manilha)
    # print(Baralho.baralho)

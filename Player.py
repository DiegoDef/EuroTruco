from carta import Carta


class Player:
    players = []
    score1 = 0  # pontuacao do jogo time 1 e 2, ganha quem chegar a 12
    score2 = 0
    count_play = 0  # index do próximo jogador
    first_score = []

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
        self.__carta_b = value

    def __str__(self):
        return f"Nome: {self.__name}\nCARtas: {self.carta_a.numero} de {self.carta_a.naipe}, " \
               f"{self.carta_b.numero} de {self.carta_b.naipe} e {self.carta_c.numero} de {self.carta_c.naipe}"

    """def gravar_cartas(self):
        if len(nomes_jogadores) == 2:
            j1_c = {"A": (list(c[0][0])[0], list(c[0][0].values())[0].title()),
                    "B": (list(c[0][1])[0], list(c[0][1].values())[0].title()),
                    "C": (list(c[0][2])[0], list(c[0][2].values())[0].title())}
            print(j1_c)
            j2_c = {"A": (list(c[1][0])[0], list(c[1][0].values())[0].title()),
                    "B": (list(c[1][1])[0], list(c[1][1].values())[0].title()),
                    "C": (list(c[1][2])[0], list(c[1][2].values())[0].title())}
            print(j2_c)"""


if __name__ == "__main__":
    pessoa = Player("Rodrigo")
    print(pessoa.available_cards)
    Player.player1 = "Alan"
    manilha: int = Carta().numero
    print(Player.player1)
    # print(manilha)
    # print(Baralho.baralho)


"""pessoa = Player("Rodrigo")
print(pessoa.carta_a.naipe)
print(pessoa.carta_b.numero_naipe)
print(pessoa.carta_c.numero_naipe)
print(pessoa.carta_a.get_baralho)
print(Carta.baralho)
Carta.reset_baralho()
print(pessoa.carta_a.get_baralho)
#print("carta1", pessoa.carta1)"""

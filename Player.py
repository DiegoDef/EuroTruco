class Deck:
    """Deck de 3 cartas que todo jogador possui"""
    def __init__(self, carta1={}, carta2={}, carta3={}):
        self._Deck__carta1 = carta1
        self.__carta2 = carta2
        self.__carta3 = carta3

    def get_carta1(self, naipe=False):
        """Por padrão retorna o número da carta"""
        if naipe:
            return list(self._Deck__carta1.values())[0]
        else:
            return list(self._Deck__carta1)[0]

    def get_carta2(self, naipe=False):
        """Por padrão retorna o número da carta"""
        if naipe:
            return list(self.__carta2.values())[0]
        else:
            return list(self.__carta2)[0]

    def get_carta3(self, naipe=False):
        """Por padrão retorna o número da carta"""
        if naipe:
            return list(self.__carta3.values())[0]
        else:
            return list(self.__carta3)[0]

    def set_carta1(self, carta1):
        self._Deck__carta1 = carta1

    def set_carta2(self, carta2):
        self.__carta2 = carta2

    def set_carta3(self, carta3):
        self.__carta3 = carta3


class Player(Deck):
    cartas_restantes = []
    remove = [8, 9]

    def __init__(self, nome_do_jogador, carta1={}, carta2={}, carta3={}):
        super().__init__(carta1, carta2, carta3)
        self.__nome = nome_do_jogador

    def get_cartas(self):
        return self._Deck__carta1, self._Deck__carta2, self._Deck__carta3

    def get_baralho(self):
        return self.cartas_restantes

    def gerar_baralho_completo(self):
        """Gera um baralho de truco"""
        self.cartas_restantes = [{}.fromkeys(range(1, 13), "moles"),
                                 {}.fromkeys(range(1, 13), "espadas"),
                                 {}.fromkeys(range(1, 13), "copas"),
                                 {}.fromkeys(range(1, 13), "paus")]

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

    def da_carta(self, n=1):
        from random import randint, choice, shuffle

        cartas = []
        if len(self.cartas_restantes) == 0:
            self.gerar_baralho_completo()

        while len(cartas) < n:
            numero = self.remove[0]
            naipe = 0
            list1 = []
            list2 = []
            while numero in self.remove:
                for _ in range(24):
                    list1.append(randint(0, 3))
                    list2.append(randint(1, 12))
                shuffle(list1)
                shuffle(list2)
                naipe = choice(list1)
                numero = choice(list2)
            if self.cartas_restantes[naipe][numero] is not None:
                carta = {list(self.cartas_restantes[naipe].keys())[numero - 1]: self.cartas_restantes[naipe][numero]}
                cartas.append(carta)
                self.cartas_restantes[naipe][numero] = None
        if n == 3:
            self._Deck__carta1 = cartas[0]
            self._Deck__carta2 = cartas[1]
            self._Deck__carta3 = cartas[2]
            with open(f"cartas\\{self.__nome}.txt", "w") as j1:
                j1.write(f"Olá {self.__nome}! Suas cartas estão logo abaixo. Boa sorte!\n\n"
                         f"A: {super().get_carta1()} de {super().get_carta1(True)}\n"
                         f"B: {super().get_carta2()} de {super().get_carta1(True)}\n"
                         f"C: {super().get_carta3()} de {super().get_carta1(True)}\n")
        else:
            return carta


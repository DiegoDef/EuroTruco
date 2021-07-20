class Baralho:
    baralho = [{}.fromkeys(range(1, 13), "moles"),
               {}.fromkeys(range(1, 13), "espadas"),
               {}.fromkeys(range(1, 13), "copas"),
               {}.fromkeys(range(1, 13), "paus")]
    remove = (8, 9)

    @staticmethod
    def reset_baralho():
        """Gera um baralho de truco"""
        Baralho.baralho = [{}.fromkeys(range(1, 13), "moles"),
                           {}.fromkeys(range(1, 13), "espadas"),
                           {}.fromkeys(range(1, 13), "copas"),
                           {}.fromkeys(range(1, 13), "paus")]

    def da_carta(self):
        """Retornar uma carta para o jogador garantindo a aleatoriedade"""
        from random import randint, choice, shuffle

        carta = 0
        #  if len(self.baralho) == 0:  não deve precisar, retirar no futuro
        #  self.baralho()

        while carta == 0:
            numero = self.remove[0]
            naipe = 0
            while numero in self.remove:
                list1 = []
                list2 = []
                for _ in range(24):
                    list1.append(randint(0, 3))
                    num_random = randint(1, 12)
                    while num_random in self.remove:
                        num_random = randint(1, 12)
                    list2.append(num_random)
                shuffle(list1)
                shuffle(list2)
                naipe = choice(list1)
                numero = choice(list2)
                #print("naipe", naipe, "numero", numero)
            if self.baralho[naipe][numero] != 0:
                carta = {list(self.baralho[naipe].keys())[numero - 1]: self.baralho[naipe][numero]}
                # cartas.append(carta)
                self.baralho[naipe][numero] = 0  # 0 para indicar que a carta foi usada
        return carta

    @property
    def get_baralho(self):
        return self.baralho


class Carta(Baralho):

    def __init__(self):
        x = self.da_carta().items()
        self.__numero = list(x)[0][0]
        self.__naipe = list(x)[0][1]

    @property
    def numero(self):
        """Retorna o numero da carta"""
        return self.__numero

    @property
    def naipe(self):
        """Retorna o naipe da carta"""
        return self.__naipe

    @property
    def numero_naipe(self):
        """Retorna o numero e naipe da carta"""
        return f"Número: {self.__numero}\nNaipe: {self.__naipe}"

    def set_numero(self, numero):
        """Muda o numero da carta para fins de testes"""
        if numero in range(13) and numero not in self.remove:
            self.__numero = numero
        else:
            print("Entrada não disponível para servir como número da carta, tente novamente.")

    def set_naipe(self, naipe):
        """Muda o naipe da carta para fins de testes"""
        if naipe in ("moles", "espadas", "copas", "paus"):
            self.__naipe = naipe
        else:
            print("Entrada não disponível para servir como naipe da carta, tente novamente.")


class Player:
    nomes_dos_jogadores = []

    def __init__(self, nome_do_jogador):
        self.__nome = nome_do_jogador
        self.__carta_a = Carta()
        self.__carta_b = Carta()
        self.__carta_c = Carta()
        Player.nomes_dos_jogadores.append(nome_do_jogador)

    def jogar_carta(self, id_carta):
        cartas = {"A": self.__carta_a, "B": self.__carta_b, "C": self.__carta_c}
        while id_carta.upper not in ("A", "B", "C"):
            id_carta = input(f"Carta {id_carta.upper} não disponível para uso, escolha outra carta: ").upper()
        return cartas[id_carta]

    def pedir_truco(self):
        pass

    def mostrar_cartas_disponiveis(self):
        id_carta = {0: "A", 1: "B", 2: "C"}
        print(f"As cartas disponíveis de {self.nome} são: ", end=" ")
        for i, j in zip((self.carta_a, self.carta_b, self.carta_c), range(3)):
            if i.naipe:
                if j < 2:
                    print(id_carta[j], end=", ")
                else:
                    print(id_carta[j])

    @property
    def nome(self):
        return self.__nome


    @property
    def carta_a(self):
        return self.__carta_a

    @property
    def carta_b(self):
        return self.__carta_b

    @property
    def carta_c(self):
        return self.__carta_c

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
        return f"Nome: {self.__nome}\nCartas: {self.carta_a.numero} de {self.carta_a.naipe}, " \
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


pessoa = Player("Rodrigo")
pessoa.mostrar_cartas_disponiveis()

"""pessoa = Player("Rodrigo")
print(pessoa.carta_a.naipe)
print(pessoa.carta_b.numero_naipe)
print(pessoa.carta_c.numero_naipe)
print(pessoa.carta_a.get_baralho)
print(Carta.baralho)
Carta.reset_baralho()
print(pessoa.carta_a.get_baralho)
#print("carta1", pessoa.carta1)"""

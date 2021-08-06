class Carta:
    baralho: list = [{}.fromkeys(range(1, 13), "moles"),
                     {}.fromkeys(range(1, 13), "espadas"),
                     {}.fromkeys(range(1, 13), "copas"),
                     {}.fromkeys(range(1, 13), "paus")]
    card_force = (4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, "Moles", "Espadas", "Copas", "Paus")
    remove: tuple = (8, 9)

    def __init__(self):
        x = self.get_card().items()
        self.__numero = list(x)[0][0]
        self.__naipe = list(x)[0][1]

    def get_card(self) -> dict:
        """Retornar uma carta para o jogador garantindo a aleatoriedade"""
        from random import randint, choice, shuffle
        carta: dict = {}
        #  if len(self.baralho) == 0:  não deve precisar, retirar no futuro
        #  self.baralho()
        # refazer aleatoriedade das cartas
        while carta == {}:
            numero: int = self.remove[0]
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
                # print("naipe", naipe, "numero", numero)
            if self.baralho[naipe][numero] != 0:
                carta = {list(self.baralho[naipe].keys())[numero - 1]: self.baralho[naipe][numero]}
                # cartas.append(carta)
                self.baralho[naipe][numero] = 0  # 0 para indicar que a carta foi usada
        return carta

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
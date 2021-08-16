truco_numbers = list(range(1, 8)) + list(range(10, 13))


class Carta:
    baralho: list = [{}.fromkeys(truco_numbers, "Moles"),
                     {}.fromkeys(truco_numbers, "Espadas"),
                     {}.fromkeys(truco_numbers, "Copas"),
                     {}.fromkeys(truco_numbers, "Paus")]
    card_force = (4, 5, 6, 7, 10, 11, 12, 1, 2, 3, "Moles", "Espadas", "Copas", "Paus")
    remove: tuple = (8, 9)

    def __init__(self):
        x = self.get_card().items()
        self.__numero = list(x)[0][0]
        self.__naipe = list(x)[0][1]

    def get_card(self) -> dict:
        """Retornar uma carta para o jogador garantindo a aleatoriedade"""
        def random_number(num) -> int:
            import random
            numbers = []
            for i in range(30):
                numbers.append(random.randint(0, num))
            return numbers[random.randint(0, len(numbers)-1)]
        from random import randint, choice, shuffle
        card: dict = {}
        while card == {}:
            number = random_number(9)
            naipe = random_number(3)
            cards = self.baralho[naipe]
            number = list(cards.keys())[number]
            if cards[number] != 0:
                n = {0: "Moles", 1: "Espadas", 2: "Copas", 3: "Paus"}
                card = {number: n[naipe]}
                self.baralho[naipe][number] = 0  # 0 para indicar que a carta foi usada
        return card

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
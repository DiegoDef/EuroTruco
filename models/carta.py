truco_numbers = list(range(1, 8)) + list(range(10, 13))


class Carta:
    baralho: list = [{}.fromkeys(truco_numbers, "Moles"),
                     {}.fromkeys(truco_numbers, "Espadas"),
                     {}.fromkeys(truco_numbers, "Copas"),
                     {}.fromkeys(truco_numbers, "Paus")]
    card_force: tuple = (4, 5, 6, 7, 10, 11, 12, 1, 2, 3, "Moles", "Espadas", "Copas", "Paus")
    remove: tuple = (8, 9)

    def __init__(self) -> None:
        x = self.get_card().items()
        self.__numero: int = list(x)[0][0]
        self.__naipe: int = list(x)[0][1]

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
    def numero(self) -> int:
        """Retorna o numero da carta"""
        return self.__numero

    @property
    def naipe(self) -> str:
        """Retorna o naipe da carta"""
        return self.__naipe

    @numero.setter
    def numero(self, numero: int) -> None:
        """Muda o numero da carta para fins de testes"""
        self.__numero = numero

    @naipe.setter
    def naipe(self, naipe: int) -> None:
        """Muda o naipe da carta para fins de testes"""
        if naipe in ("Moles", "Espadas", "Copas", "Paus"):
            self.__naipe = naipe
        else:
            print("Entrada não disponível para servir como naipe da carta, tente novamente.")

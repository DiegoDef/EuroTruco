def new_baralho() -> list:
    naipes = ("Moles", "Espadas", "Copas", "Paus")
    num = (4, 5, 6, 7, 10, 11, 12, 1, 2, 3)
    baralho = [(c, n) for c in num for n in naipes]
    return baralho


def get_card() -> tuple:
    from random import randint

    numbers: list = []
    baralho: list = Carta.baralho
    n_cards = len(baralho)
    for i in range(n_cards):
        numbers.append(randint(0, n_cards - 1))
    index: int = numbers[randint(0, n_cards - 1)]
    card: tuple = baralho[index]
    Carta.baralho.remove(card)
    return card


class Carta:
    baralho: list = new_baralho()
    card_force: tuple = (4, 5, 6, 7, 10, 11, 12, 1, 2, 3, "Moles", "Espadas", "Copas", "Paus")

    def __init__(self) -> None:
        x = get_card()
        self.__numero: int = x[0]
        self.__naipe: str = x[1]

    @property
    def numero(self) -> int:
        """Retorna o numero da carta"""
        return self.__numero

    @property
    def naipe(self) -> str:
        """Retorna o naipe da carta"""
        return self.__naipe

    @numero.setter
    def numero(self, numero: int) -> None:  # para fins de testes
        """Muda o numero da carta para fins de testes"""
        self.__numero = numero

    @naipe.setter
    def naipe(self, naipe: int) -> None:  # para fins de testes
        """Muda o naipe da carta para fins de testes"""
        if naipe in ("Moles", "Espadas", "Copas", "Paus"):
            self.__naipe = naipe
        else:
            print("Entrada não disponível para servir como naipe da carta, tente novamente.")

    def __str__(self):
        return f"{self.numero} de {self.naipe}"

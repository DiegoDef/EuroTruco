class Cartas:
    cartas_restantes = []
    remove = [8, 9]

    def __init__(self, naipe, numero):
        self._naipe = naipe
        self._numero = numero

    def gerar_baralho_completo(self):
        """Gera um baralho de truco"""
        self.cartas_restantes = [{}.fromkeys(range(1, 13), "moles"),
                                 {}.fromkeys(range(1, 13), "espadas"),
                                 {}.fromkeys(range(1, 13), "copas"),
                                 {}.fromkeys(range(1, 13), "paus")]

    def da_uma_carta(self):
        from random import randint

        carta = {}
        if len(self.cartas_restantes) != 0:
            while len(carta) == 0:
                numero = self.remove[0]
                naipe = 0
                while numero in self.remove:
                    naipe = randint(0, 3)
                    numero = randint(1, len(self.cartas_restantes[naipe]))
                if self.cartas_restantes[naipe][numero] is not None:
                    carta = {list(self.cartas_restantes[naipe].keys())[numero - 1]: self.cartas_restantes[naipe][numero]}
                    self.cartas_restantes[naipe][numero] = None
            return carta
        else:
            print("Impossível dar cartas sem um baralho.")



class Players(Cartas):

    def __init__(self, nome, naipe, numero):
        super().__init__(naipe, numero)
        self._nome = nome

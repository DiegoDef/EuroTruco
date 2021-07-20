from Player import Player, Carta


def main():
    euro_truco()


def euro_truco():
    pontuacao_time1_jogo = 0  # pontuacao do jogo, ganha quem chegar a 12
    pontuacao_time2_jogo = 0
    pontuacao_time1_rodada = 0  # pontuacao da rodada que vai até 3, ao chegar a 3 ganha um ponto no jogo.
    pontuacao_time2_rodada = 0  # pontuacao da rodada talvez deva ser removidoe colocado direto no def.
    jogadores = []
    prox_jogador = 0
    quant_j = 0
    carta_virada = Carta()


    while quant_j not in (2, 4):
        quant_j = int(input("Bem vindo ao Euro Truco simulator®\n\n"
                            "A partida poderá ter 2 ou 4 jogadores no total."
                            "Antes de começar, informe a quantidade de participantes (2 ou 4): "))
        if quant_j not in (2, 4):
            print("Entrada inválida, a quantidade deve ser de 2 ou 4.\n")

    if quant_j == 2:
        print("Os jogadores 1 e 2 se enfrentarão.")
        while len(jogadores) < 2:
            jogadores.append(Player(input(f"\nInforme o nome do jogador(a) número {len(jogadores) + 1}: ")))
    else:
        print("Os jogadores 1 e 2 enfrentarão os jogadores 3 e 4.")
        while len(jogadores) < 4:
            jogadores.append(Player(input(f"\nInforme o nome do jogador(a) número {len(jogadores) + 1}: ")))

    if len(jogadores) == 4:
        jogadores.insert(2, jogadores.pop(1))  # ajeita ordem usada no programa para manipulaçao de jogadores
# remodelar daqui pra baixo e colocado no github


def iniciar_jogo(self):  # dividir iniciar o jogo em métodos menores
    cont = 0

    while True:
        # colocar quem fez a primeira na hora de marcar os pontos.
        print(f"\nPontuação da rodada: Time 1 {EuroTruco.pontuacao_time1_rodada} x "
              f"{EuroTruco.pontuacao_time2_rodada} Time 2")

        print("Comandos disponíveis para cada jogador:")
        for nome in self.jogadores:
            print(nome.mostrar_cartas_disponiveis())

        print(f"\nA carta virada é: {EuroTruco.carta_virada}")

        cont += 1

    jogar_carta()


def jogar_carta():
    pass


def verificar_quem_venceu():
    pass


def verifica_regras():
    pass


def mostrar_cartas():
    pass


# passar algums fuções para cá, como a de criação de baralho.

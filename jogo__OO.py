from Player import Player, Carta

def main():
    euro_truco()

def euro_truco():
    pontuacao_time1_jogo = 0  # pontuacao do jogo, ganha quem chegar a 12
    pontuacao_time2_jogo = 0
    pontuacao_time1_rodada = 0  # pontuacao da rodada que vai até 3, ao chegar a 3 ganha um ponto no jogo.
    pontuacao_time2_rodada = 0  # pontuacao da rodada talvez deva ser removidoe colocado direto no def.
    prox_jogador = 0
    carta_virada = Carta()
# remodelar daqui pra baixo e colocar no github

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

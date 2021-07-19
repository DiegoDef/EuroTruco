"""
Jogo de truco, dá 3 cartas para cada oponente (2 ou 4 jogadores) e 1 para manilha.
Segue a maioria das regras oficiais.
Código montado sem o uso de classes (versão com classes mais pra frente)
"""

from Gerador import gera_cartas
from jogo import iniciar_jogo
from grava_cartas import grava_cartas

quant_j = 2
ult_jogador = -1
j1 = 0
j2 = 0
nomes = ["Diego", "Michele", "Diego2", "Michele2"]
pontua = [0, 0]
quant_j = int(input("Bem vindo ao Euro Truco simulator®\n\n"
                    "Antes de começar, informe a quantidade de participantes (2 ou 4): "))
while quant_j != 2 and quant_j != 4:
    quant_j = int(input("Quantidade incorreta, por favor informe 2 ou 4 jogadores: "))

nomes = []
while len(nomes) < quant_j:
    nomes.append(input(f"Informe o nome do {len(nomes) + 1}° jogador(a): "))

print(f"A partida começou!\n")

if len(nomes) == 2:
    print(f"{nomes[0]} VS {nomes[1]}\n")
else:
    print(f"{nomes[0]} e {nomes[2]} VS {nomes[1]} e {nomes[3]}\n")

while j1 < 12 and j2 < 12:
    cartas, baralho_restante = gera_cartas(*nomes)
    comandos_j = grava_cartas(cartas, nomes)
    
    print(comandos_j)
    n1, n2, ult_jogador = iniciar_jogo(comandos_j, nomes, baralho_restante, pontua, ult_jogador)
    j1 += n1 + pontua[0]
    j2 += n2 + pontua[1]

    if ult_jogador == 3:
        ult_jogador = -1
    if len(nomes) == 2:
        print(f"\nA pontuação do jogo atual é: {nomes[0]} {j1} X {j2} {nomes[1]}")
        if j1 < 12 and j2 != 12:
            input("Quem chegar a 12 pontos primeiro será o vencedor! Aperte Enter para continuar a partida.\n")
    else:
        print(f"\nA pontuação do jogo atual é: {nomes[0]} e {nomes[2]} {j1} X {j2} {nomes[1]} e {nomes[3]}\n")
        if j1 < 12 and j2 != 12:
            input("Quem chegar a 12 pontos primeiro será o vencedor! Aperte Enter para continuar a partida.\n")

    if j1 == 11 and j2 < 11:
        print("A equipe 2 jogará a partida valendo 3 pontos por rodada. A equipe 1 poderá escolher se deseja "
              "seguir com a partida analisando todas as cartas de sua(s) mão(s).\n"
              "Desistindo, a outra equipe leva um ponto. ")
        pontua[1] = 2
    elif j2 == 11 and j1 < 11:
        print("A equipe 1 jogará a partida valendo 3 pontos por rodada. A equipe 2 poderá escolher se deseja "
              "seguir com a partida analisando todas as cartas de sua(s) mão(s).\n"
              "Desistindo, a outra equipe leva um ponto. ")
        pontua[0] = 2
    elif j1 == 11 and j2 == 11:
        print("Como a partida está empatada em 11x11, o próximo jogo será as cegas.\n"
              "Os arquivos com suas cartas serão gerados apenas para avaliação posterior, "
              "não podendo ser lidos até o final da partida.")
        pontua = [0, 0]

if j1 == 12:
    if len(nomes) == 2:
        print(f"Parabéns {nomes[0]} você foi o(a) grande vencedor(a)!!!")
    else:
        print(f"Parabéns {nomes[0]} e {nomes[2]}, você venceram!")
elif j2 == 12:
    if len(nomes) == 2:
        print(f"Parabéns {nomes[1]} você foi o(a) grande vencedor(a)!!!")
    else:
        print(f"Parabéns {nomes[1]} e {nomes[3]}, você venceram!")
else:
    print("Tem algo errado aí!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

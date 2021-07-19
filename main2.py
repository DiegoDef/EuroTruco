from Player import *
# -*- coding: utf-8 -*-


def nomes_versus(jogadores):
    """Retona os nomes dos jogadores versus adequando-se a quantidade"""
    if len(jogadores) == 2:
        return f"{jogadores[0].nome} VS {jogadores[1].nome}"
    else:
        return f"{jogadores[0].nome} e {jogadores[2].nome} VS {jogadores[1].nome} e {jogadores[3].nome}"


jogadores = []
quant_j = int(input("Bem vindo ao Euro Truco simulator®\n\n"
                    "A partida poderá ter 2 ou 4 jogadores no total. Caso tenha um time, "
                    "os jogadores 1 e 2 enfrentarão o 3 e 4.\n"
                    "Antes de começar, informe a quantidade de participantes (2 ou 4): "))

while len(jogadores) < quant_j:
    jogadores.append(Player(input(f"\nInforme o nome do jogador(a) número {len(jogadores)+1}: ")))

if len(jogadores) == 4:
    jogadores.insert(2, jogadores.pop(1))  # ajeita ordem usada no programa para manipulaçao de jogadores

print(nomes_versus(jogadores), "\n")

print(jogadores[0].cartas)
print(jogadores[1].cartas)




"""print()
for j in jogadores:
    j.da_carta(3)
    print(j)"""


"""p1 = Player("Diego")

n = p1.da_carta(3)

print(n)

print(p1.cartas)
print(p1.carta1)
print(p1.carta2)
print(p1.carta3)
print(p1.baralho)"""

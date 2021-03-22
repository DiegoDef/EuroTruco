def grava_cartas(c, nomes_jogadores):
    """Pega as cartas dos jogadores já embaralhadas e grava em arquivo .txt com o nome do jogador. Deve ser passado
    como parâmetro as cartas dadas e os nomes dos jogadores. No final retorna dicionarios com key="comando pra jogar a
    carta" e um dado com uma tupla referente ao número e manilha da carta do jogador."""

    if len(nomes_jogadores) == 2:
        j1_c = {"A": (list(c[0][0])[0], list(c[0][0].values())[0].title()),
                "B": (list(c[0][1])[0], list(c[0][1].values())[0].title()),
                "C": (list(c[0][2])[0], list(c[0][2].values())[0].title())}
        print(j1_c)
        j2_c = {"A": (list(c[1][0])[0], list(c[1][0].values())[0].title()),
                "B": (list(c[1][1])[0], list(c[1][1].values())[0].title()),
                "C": (list(c[1][2])[0], list(c[1][2].values())[0].title())}
        print(j2_c)

        with open(f"cartas\\{nomes_jogadores[0]}.txt", "w") as j1, open(f"cartas\\{nomes_jogadores[1]}.txt", "w") as j2:
            j1.write(f"Olá {nomes_jogadores[0]}! Suas cartas estão logo abaixo. Boa sorte!\n\n"
                     f"A: {list(c[0][0])[0]} de {list(c[0][0].values())[0].title()}\n"
                     f"B: {list(c[0][1])[0]} de {list(c[0][1].values())[0].title()}\n"
                     f"C: {list(c[0][2])[0]} de {list(c[0][2].values())[0].title()}\n")
            j2.write(f"Olá {nomes_jogadores[1]}! Suas cartas estão logo abaixo. Boa sorte!\n\n"
                     f"A: {list(c[1][0])[0]} de {list(c[1][0].values())[0].title()}\n"
                     f"B: {list(c[1][1])[0]} de {list(c[1][1].values())[0].title()}\n"
                     f"C: {list(c[1][2])[0]} de {list(c[1][2].values())[0].title()}\n")
        return j1_c, j2_c

    else:
        j1_c = {"A": (list(c[0][0])[0], list(c[0][0].values())[0].title()),
                "B": (list(c[0][1])[0], list(c[0][1].values())[0].title()),
                "C": (list(c[0][2])[0], list(c[0][2].values())[0].title())}
        print(j1_c)
        j2_c = {"A": (list(c[1][0])[0], list(c[1][0].values())[0].title()),
                "B": (list(c[1][1])[0], list(c[1][1].values())[0].title()),
                "C": (list(c[1][2])[0], list(c[1][2].values())[0].title())}
        print(j2_c)
        j3_c = {"A": (list(c[2][0])[0], list(c[2][0].values())[0].title()),
                "B": (list(c[2][1])[0], list(c[2][1].values())[0].title()),
                "C": (list(c[2][2])[0], list(c[2][2].values())[0].title())}
        print(j3_c)
        j4_c = {"A": (list(c[3][0])[0], list(c[3][0].values())[0].title()),
                "B": (list(c[3][1])[0], list(c[3][1].values())[0].title()),
                "C": (list(c[3][2])[0], list(c[3][2].values())[0].title())}
        print(j4_c)

        with open(f"cartas\\{nomes_jogadores[0]}.txt", "w") as j1, open(f"cartas\\{nomes_jogadores[1]}.txt", "w") as j2:
            j1.write(f"Olá {nomes_jogadores[0]}! Suas cartas estão logo abaixo. Boa sorte!\n\n"
                     f"A: {list(c[0][0])[0]} de {list(c[0][0].values())[0].title()}\n"
                     f"B: {list(c[0][1])[0]} de {list(c[0][1].values())[0].title()}\n"
                     f"C: {list(c[0][2])[0]} de {list(c[0][2].values())[0].title()}\n")
            j2.write(f"Olá {nomes_jogadores[1]}! Suas cartas estão logo abaixo. Boa sorte!\n\n"
                     f"A: {list(c[1][0])[0]} de {list(c[1][0].values())[0].title()}\n"
                     f"B: {list(c[1][1])[0]} de {list(c[1][1].values())[0].title()}\n"
                     f"C: {list(c[1][2])[0]} de {list(c[1][2].values())[0].title()}\n")
        with open(f"cartas\\{nomes_jogadores[2]}.txt", "w") as j3, open(f"cartas\\{nomes_jogadores[3]}.txt", "w") as j4:
            j3.write(f"Olá {nomes_jogadores[2]}! Suas cartas estão logo abaixo. Boa sorte!\n\n"
                     f"A: {list(c[2][0])[0]} de {list(c[2][0].values())[0].title()}\n"
                     f"B: {list(c[2][1])[0]} de {list(c[2][1].values())[0].title()}\n"
                     f"C: {list(c[2][2])[0]} de {list(c[2][2].values())[0].title()}\n")
            j4.write(f"Olá {nomes_jogadores[3]}! Suas cartas estão logo abaixo. Boa sorte!\n\n"
                     f"A: {list(c[3][0])[0]} de {list(c[3][0].values())[0].title()}\n"
                     f"B: {list(c[3][1])[0]} de {list(c[3][1].values())[0].title()}\n"
                     f"C: {list(c[3][2])[0]} de {list(c[3][2].values())[0].title()}\n")
        return j1_c, j2_c, j3_c, j4_c

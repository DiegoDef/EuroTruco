def iniciar_jogo(comandos, nomes, baralho, pontua, ultimo_jogador=0):
    """Inicia uma partida única de truco com 2 ou 4 pessoas. Retorna 1 ou 0 para cada jogador conforme quem ganhar (1)
    ou perder (0), com ordem jogador 1, jogador 2 e retorna o índice do jogador que começou a jogar para que cada um
    inicie a partida de forma alternada."""

    from random import randint, choice

    ultimo_jogador += 1
    ordem_forca = (4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, "Moles", "Espadas", "Copas", "Paus")
    emp = False
    cont1 = 0
    cont2 = 0
    n_carta1 = 0
    n_carta2 = 0
    nova = []
    outro_nomes = nomes.copy()
    outro_nomes.append(None)
    truco = 0
    ped_truco = []
    j1_n = 0
    j2_n = 0
    cont1_pri = False
    cont2_pri = False
    cont = 0
    primeira = True

    if pontua[0] == 2:
        resp = ""
        while resp != "S" and resp != "N":
            resp = input("A equipe 2, após analisar suas cartas, deseja continuar? S - SIM, N - NÃO").upper
        if resp == "N":
            print("A equipe 1 ganhou 1 ponto por desistência.")
            return 1, 0, ultimo_jogador
        else:
            print("A partida vai continuar!")
    elif pontua[1] == 2:
        resp = ""
        while resp != "S" and resp != "N":
            resp = input("A equipe 1, após analisar suas cartas, deseja continuar? S - SIM, N - NÃO").upper
        if resp == "N":
            print("A equipe 2 ganhou 1 ponto por desistência.")
            return 0, 1, ultimo_jogador
        else:
            print("A partida vai continuar!")

    while len(nova) != 4:
        if outro_nomes[ultimo_jogador] is not None:
            nova.append(outro_nomes[ultimo_jogador])
            outro_nomes.remove(nova[-1])
        else:
            ultimo_jogador = 0

    c_virada = choice(tuple(baralho[randint(0, 3)]))  # Retorna apenas o número da carta sem o naipe
    while True:
        if cont == 1:
            if cont1 == 1:
                cont1_pri = True
            elif cont2 == 1:
                cont2_pri = True
        cont += 1

        if len(nomes) == 2 and not emp:
            print(f"\nPontuação da rodada: {nomes[0]} {cont1} x {cont2} {nomes[1]}")
        elif not emp:
            print(f"\nPontuação da rodada: {nomes[0]} e {nomes[2]} {cont1} x {cont2} {nomes[1]} e {nomes[3]}\n")
        print("Comandos disponíveis para cada jogador:")
        [print(f"{nome}: {list(comandos[nomes.index(nome)])}") for nome in nomes]
        print(f"\nA carta virada é: {c_virada}")

        for nome in nova:
            c_escondida = False
            if nomes.index(nome) == 0 or nomes.index(nome) == 2:
                carta_j1 = "0"
                while carta_j1 not in ("A", "B", "C", "6", "9", "12", "E", "TRUCO"):
                    carta_j1 = input(f'\nÉ sua vez {nome}, jogue sua carta, digite "Truco" para aumentar '
                                     f'a pontuação da partida '
                                     f'ou digite "E" para esconder sua carta: ').upper()
                if carta_j1 == "TRUCO" or carta_j1 in ("6", "9", "12", "E"):
                    if truco == 11:
                        print("Impossível aumentar a pontuação da partida, ela já está valendo 11.")
                    elif nomes.index(nome) in ped_truco:
                        print("Impossível pedir truco, somente o time rival pode pedir.")
                    elif carta_j1 == "E":
                        if primeira:
                            print("Não é possível esconder a carta na primeira jogada.")
                        else:
                            print("Você escondeu sua carta!")
                            c_escondida = True
                    else:
                        carta_j1 = input("Você pediu truco, o time rival aceita aumentar a pontuação da partida? "
                                         "S - Sim e N - Não: ").upper()
                        while carta_j1 != "S" and carta_j1 != "N":
                            carta_j1 = input("Comando inválido. Informe S - Sim ou N - Não: ").upper()
                        if carta_j1 == "N":
                            if len(nomes) == 2:
                                print(f"{nomes[0]} ganhou a partida por desistência.")
                                return 1 + truco, 0, ultimo_jogador
                            else:
                                print(f"{nomes[0]} e {nomes[2]} ganharam a partida por desistência.")
                                return 1 + truco, 0, ultimo_jogador
                        else:
                            if truco == 0:
                                truco = 2
                            else:
                                truco += 3
                            ped_truco = [0, 2]
                            print(f"A partida agora vale {truco + 1} pontos.")
                            carta_j1 = input(f'\nJogue sua carta {nome}: ').upper()

                while carta_j1 not in list(comandos[nomes.index(nome)]):
                    carta_j1 = input(f"\nInsira um comando de carta entre as opções: "
                                     f"{list(comandos[nomes.index(nome)])}: ").upper()
                if not c_escondida:
                    print(f"Você jogou: {comandos[nomes.index(nome)][carta_j1][0]} de "
                          f"{comandos[nomes.index(nome)][carta_j1][1]}")

                    comando = comandos[nomes.index(nome)][carta_j1]  # Carta do comando do jogador.
                    ordem_forca.index(c_virada)
                    if ordem_forca.index(comando[0]) == ordem_forca.index(c_virada) + 1:
                        n_carta1 = 12
                        j1_n = ordem_forca.index(comando[1])
                    elif c_virada == 7 and comando[0] == 10:
                        n_carta1 = 12
                        j1_n = ordem_forca.index(comando[1])
                    elif ordem_forca.index(comando[0]) > n_carta1:
                        n_carta1 = ordem_forca.index(comando[0])
                del comandos[nomes.index(nome)][carta_j1]
                print(f"carta maior {n_carta1}")
            else:
                carta_j2 = "0"
                while carta_j2 not in ("A", "B", "C", "6", "9", "12", "E", "TRUCO"):
                    carta_j2 = input(f'\nÉ sua vez {nome}, jogue sua carta, digite "Truco" para aumentar '
                                     f'a pontuação da partida '
                                     f'ou digite "E" para esconder sua carta: ').upper()
                if carta_j2 == "TRUCO" or carta_j2 in ("6", "9", "12", "E"):
                    if truco == 11:
                        print("Impossível aumentar a pontuação da partida, ela já está valendo 11.")
                    elif nomes.index(nome) in ped_truco:
                        print("Impossível pedir truco, somente o time rival pode pedir.")
                    elif carta_j2 == "E":
                        if primeira:
                            print("Não é possível esconder a carta na primeira jogada.")
                        else:
                            print("Você vai esconder sua carta!")
                            c_escondida = True
                    else:
                        carta_j2 = input("Você pediu truco, o time rival aceita aumentar a pontuação da partida? "
                                         "S - Sim e N - Não: ").upper()
                        while carta_j2 != "S" and carta_j2 != "N":
                            carta_j2 = input("Comando inválido. Informe S - Sim ou N - Não: ").upper()
                        if carta_j2 == "N":
                            if len(nomes) == 2:
                                print(f"{nomes[1]} ganhou a partida por desistência.")
                                return 0, 1 + truco, ultimo_jogador
                            else:
                                print(f"{nomes[1]} e {nomes[3]} ganharam a partida por desistência.")
                                return 0, 1 + truco, ultimo_jogador
                        else:
                            if truco == 0:
                                truco = 2
                            else:
                                truco += 3
                            ped_truco = [1, 3]
                            print(f"A partida agora vale {truco + 1} pontos.")
                            carta_j2 = input(f'\nJogue sua carta {nome}: ').upper()

                while carta_j2 not in list(comandos[nomes.index(nome)]):
                    carta_j2 = input(f"Insira um comando de carta entre as opções: "
                                     f"{list(comandos[nomes.index(nome)])}: ").upper()
                if not c_escondida:
                    print(f"Você jogou: {comandos[nomes.index(nome)][carta_j2][0]} de "
                          f"{comandos[nomes.index(nome)][carta_j2][1]}")

                    comando = comandos[nomes.index(nome)][carta_j2]  # Carta do comando do jogador.
                    if ordem_forca.index(comando[0]) == ordem_forca.index(c_virada) + 1:
                        n_carta2 = 12
                        j2_n = ordem_forca.index(comando[1])
                    elif c_virada == 7 and comando[0] == 10:
                        n_carta2 = 12
                        j2_n = ordem_forca.index(comando[1])
                    elif ordem_forca.index(comando[0]) > n_carta2:
                        n_carta2 = ordem_forca.index(comando[0])
                del comandos[nomes.index(nome)][carta_j2]
                print(f"carta maior {n_carta2}")
        if n_carta1 > n_carta2:
            if len(nomes) == 2:
                cont1 += 1
                if emp or cont1 > 1:
                    print(f"\n{nomes[0]} ganhou a partida!")
                    return 1 + truco, 0, ultimo_jogador
                print(f"\n{nomes[0]} ganhou essa rodada!")
            else:
                cont1 += 1
                if emp or cont1 > 1:
                    print(f"\n{nomes[0]} e {nomes[2]} ganharam a partida!")
                    return 1 + truco, 0, ultimo_jogador
                print(f"\n{nomes[0]} e {nomes[2]} ganharam essa rodada!")
        elif n_carta1 < n_carta2:
            if len(nomes) == 2:
                cont2 += 1
                if emp or cont2 > 1:
                    print(f"\n{nomes[1]} ganhou a partida!")
                    return 0, 1 + truco, ultimo_jogador
                print(f"\n{nomes[1]} ganhou essa rodada!")
            else:
                cont2 += 1
                if emp or cont2 > 1:
                    print(f"\n{nomes[1]} e {nomes[3]} ganharam a partida!")
                    return 0, 1 + truco, ultimo_jogador
                print(f"\n{nomes[1]} e {nomes[3]} ganharam essa rodada!")
        elif n_carta1 == n_carta2:
            if n_carta1 == 12:
                if j1_n > j2_n:
                    if len(nomes) == 2:
                        cont1 += 1
                        if emp or cont1 > 1:
                            print(f"\n{nomes[0]} ganhou a partida!")
                            return 1 + truco, 0, ultimo_jogador
                        print(f"\n{nomes[0]} ganhou essa rodada!")
                    else:
                        cont1 += 1
                        if emp or cont1 > 1:
                            print(f"\n{nomes[0]} e {nomes[2]} ganharam a partida!")
                            return 1 + truco, 0, ultimo_jogador
                        print(f"\n{nomes[0]} e {nomes[2]} ganharam essa rodada!")
                else:
                    if len(nomes) == 2:
                        cont2 += 1
                        if emp or cont2 > 1:
                            print(f"\n{nomes[1]} ganhou a partida!")
                            return 0, 1 + truco, ultimo_jogador
                        print(f"\n{nomes[1]} ganhou essa rodada!")
                    else:
                        cont2 += 1
                        if emp or cont2 > 1:
                            print(f"\n{nomes[1]} e {nomes[3]} ganharam a partida!")
                            return 0, 1 + truco, ultimo_jogador
                        print(f"\n{nomes[1]} e {nomes[3]} ganharam essa rodada!")
            if cont1_pri:
                if len(nomes) == 2:
                    print(f"\n{nomes[0]} ganhou a partida!")
                    return 1 + truco, 0, ultimo_jogador
                else:
                    print(f"\n{nomes[0]} e {nomes[2]} ganharam a partida!")
                    return 1 + truco, 0, ultimo_jogador
            elif cont2_pri:
                if len(nomes) == 2:
                    print(f"\n{nomes[1]} ganhou a partida!")
                    return 0, 1 + truco, ultimo_jogador
                else:
                    print(f"\n{nomes[1]} e {nomes[3]} ganharam a partida!")
                    return 0, 1 + truco, ultimo_jogador
            elif n_carta1 != 12:  # Verifica se é manilha. Se for, não existe empate.
                print("\nDeu empate, o próximo a ganhar uma jogada levará o(s) ponto(os).")
                emp = True
        n_carta1 = 0
        n_carta2 = 0
        primeira = False
        input()  # Trava partida para esperar jogadores se recomporem. Enter para iniciar novamente.

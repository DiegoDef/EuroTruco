def da_cartas(l, *args):
    from random import randint, shuffle

    remove = (8, 9)
    carta = []
    while len(carta) < (len(args) * 3):
        numero = remove[0]
        manilha = 0
        while numero in remove or numero == remove:
            numero = randint(1, 12)
            manilha = randint(0, 3)
        try:
            carta.append({numero: l[manilha][numero]})
            del l[manilha][numero]
        except KeyError:
            pass
    shuffle(carta)
    shuffle(carta)
    if len(args) == 2:
        return (carta[0:3], carta[3:6]), l
    else:
        return (carta[0:3], carta[3:6], carta[6:9], carta[9:12]), l

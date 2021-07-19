# esse sistema não vai mais ser usado após o uso de orientação e objetos

def gera_cartas(*args):
    """Deve ser passado como parâmetro os nomes dos jogadores. Gera um baralho e retorna o baralho restante,
    retira as cartas 8 e 9, retorna as cartas dadas aos 2 ou 4 jogadores (a depender da quantidade de nomes passados)
    e também vira uma carta.
    Deve ser passado o nome dos jogadores.
    No final retorna embaralha e dá as cartas para 2 ou 4 jogadores"""

    from random import randint, shuffle

    remove = (8, 9)
    l = [{}.fromkeys(filter(lambda x: x not in remove, range(1, 13)), "moles"),
         {}.fromkeys(filter(lambda x: x not in remove, range(1, 13)), "espadas"),
         {}.fromkeys(filter(lambda x: x not in remove, range(1, 13)), "copas"),
         {}.fromkeys(filter(lambda x: x not in remove, range(1, 13)), "paus")]
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

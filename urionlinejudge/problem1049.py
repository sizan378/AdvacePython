A = str(input())
B = str(input())
C = str(input())


if A == 'vertebrado':
    if B == 'mamifero':
        if C == 'onivoro':
            print('homem')
        elif C == 'herbivoro':
            print('vaca')
    elif B == 'ave':
        if C == 'carnivoro':
            print('aguia')
        elif C == 'onivoro':
            print('pomba')

if A == 'invertebrado':
    if B == 'inseto':
        if C == 'hematofago':
            print('pulga')
        elif C == 'herbivoro':
            print('lagarta')
    elif B == 'anelideo':
        if C == 'hematofago':
            print('sanguessuga')
        elif C == 'onivoro':
            print('minhoca')
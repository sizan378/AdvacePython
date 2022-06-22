while True:
    a = 0
    b = 0
    while(a < 2):
        N = float(input())
        if N >= 0 and N <= 10:
            a += 1
            b = b + N
        else:
            print('nota invalida')

    c = b /2
    print(f'media = {c:.2f}')
    v = 0
    while True:
        v = int(input())
        print('novo calculo (1-sim 2-nao)')
        if (v == 1 or v == 2):
            break
    if v == 2:
        break
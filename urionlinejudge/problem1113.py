while(True):
    try:
        X, Y = list(map(int,input().split()))
        if X == Y:
            break
        elif X > Y:
            print('Decrescente')
        else:
            print('Crescente')
    except:
        break
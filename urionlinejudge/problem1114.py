while(True):
    try:
        X = int(input())
        if X == 2002:
            print('Acesso Permitido')
            break
        else:
            print('Senha Invalida')
    except:
        break
ST, ET = list(map(int, input().split(' ')))

if ST < 24 and ET <= 24:
    if ST > ET:
        A = ET + 24
        D = A - ST
        print(f"O JOGO DUROU {D} HORA(S)")
    elif ST < ET:
        D = ET - ST
        print(f"O JOGO DUROU {D} HORA(S)")
    elif ST == ET:
        print('O JOGO DUROU 24 HORA(S)')

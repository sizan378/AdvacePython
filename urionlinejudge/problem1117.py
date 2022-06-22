a = 0
b = 0
while(True):
    try:
        if a == 2:
            break
        N = float(input())
        if N > 0 and N <= 10:
            a += 1
            b = b + N
        else:
            print('nota invalida')
    except:
        break
c = b /2.00
print(f'media = {c}')
A, B, C = list(map(float,input().split(' ')))

p = B * B - 4*A*C
r = pow(p,  0.5)
if (p < 0 or A == 0):
    print('Impossivel calcular')
else:
    R1 = (-B + r) / (2*A)
    R2 = (-B - r )/ (2*A)

    print(f'R1 = {R1:.5f}')
    print(f'R2 = {R2:.5f}')
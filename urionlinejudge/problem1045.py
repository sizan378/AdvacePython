A, B, C = sorted(list(map(float,input().split(' '))),reverse=True)


if (0<A) and (0<B) and (0<C):
    if (A >= (B + C)):
        print(f'NAO FORMA TRIANGULO')
    elif (A*A == (B*B + C*C)):
        print(f'TRIANGULO RETANGULO')
    elif (A*A > (B*B+C*C)):
        print(f'TRIANGULO OBTUSANGULO')
    elif (A*A < (B*B+C*C)):
        print(f'TRIANGULO ACUTANGULO')

if A == B == C:
    print(f'TRIANGULO EQUILATERO')
elif A == B or B == C or C == A:
    print(f'TRIANGULO ISOSCELES')
        
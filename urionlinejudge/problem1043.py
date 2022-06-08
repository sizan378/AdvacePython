A, B, C = list(map(float,input().split(' ')))

if (A + B) > C and (B+C) > A and (C+A) > B:
    peri = A + B + C
    print(f'Perimetro = {peri}')
else:
    area = (A+B)/2*C
    print(f'Area = {area}')
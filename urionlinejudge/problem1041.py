X, Y = list(map(float, input().split(' ')))

if X > 0 and Y > 0:
    print(f"Q1")
elif X < 0 and Y > 0:
    print(f'Q2')
elif X < 0 and Y < 0:
    print(f'Q3')
elif X > 0 and Y < 0:
    print(f'Q4')
elif X > 0 or X < 0 and Y == 0:
    print(f'Eixo X')
elif Y > 0 or Y < 0 and X == 0:
    print(f'Eixo Y')
else:
    print(f'Origem')
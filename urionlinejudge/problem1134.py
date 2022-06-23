Alcool = 0
Gasolina = 0
Diesel = 0

while True:
    X = int(input())
    if X >=0:
        if X == 1:
            Alcool += 1
        elif X == 2:
            Gasolina +=1
        elif X == 3:
            Diesel += 1
        elif X == 4:
            break
print('MUITO OBRIGADO')
print(f'Alcool: {Alcool}')
print(f'Gasolina: {Gasolina}')
print(f'Diesel: {Diesel}')


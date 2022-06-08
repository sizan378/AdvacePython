Taxe = float(input())-2000.00

if Taxe <= 0:
    print('Isento')
elif  Taxe <= 1000.00:
    tax = (Taxe * 8)/100
    print(f'R$ {tax:.2f}')
elif Taxe <= 2500:
    tax = ((1000 * 8)/100) + (((Taxe-1000) * 18)/100)
    print(f'R$ {tax:.2f}')
else:
    tax = ((1000 * 8)/100) + ((1500 * 18)/100) + ((Taxe-2500)* 28)/100
    print(f'R$ {tax:.2f}')
    
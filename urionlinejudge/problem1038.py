X, Y = list(map(int,input().split()))


if X == 1:
    price = float (4*Y)
elif X == 2:
    price = float (4.50*Y)
elif X == 3:
    price = float (5*Y)
elif X == 4:
    price = float (2*Y)
else:
    price = float (1.50*Y)

print(f'Total: R$ {price:.2f}')

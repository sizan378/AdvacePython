N = float(input())

print('NOTAS:')
for i in [100,50,20,10,5,2]:
    print(f'{int(N/i)} nota(s) de R$ {i}.00')
    N = float(f'{N%i:.2f}')


print('MOEDAS:')
for i in [1,0.50,0.25,0.10,0.05,0.01]:
    print(f'{int(N/i)} moeda(s) de R$ {i:.2f}')
    N = float(f'{N%i:.2f}')


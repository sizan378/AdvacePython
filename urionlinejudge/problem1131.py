Inter = 0
Gremio = 0
Empates = 0
Total = 0

while True:
    m, n = list(map(int,input().split(' ')))
    print('Novo grenal (1-sim 2-nao)')
    if m > n:
        Inter += 1
    elif m == n:
        Empates += 1
    else:
        Gremio += 1

    Total += 1
  
    I = int(input())
    if (I==1):
        continue
    if (I==2):
        break

print(f'{Total} grenais')
print(f'Inter:{Inter}')
print(f'Gremio:{Gremio}')
print(f'Empates:{Empates}')

if Inter > Gremio:
    print('Inter venceu mais')
elif Gremio > Inter:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')

    
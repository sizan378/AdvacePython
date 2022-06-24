N = int(input())
n = 1

for i in range(N):
    print(f'{n} {n**2} {n**3}')
    print(f'{n} {n**2+1} {n**3+1}')
    n += 1
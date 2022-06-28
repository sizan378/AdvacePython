T = int(input())
S = 0
for i in range(1000):
    print(f'N[{i}] = {S}')
    S += 1
    if S == T:
        S = 0
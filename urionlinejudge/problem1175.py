
A = []
for i in range(20):
    I = int(input())
    A.append(I)

N = 0
for l in A[::-1]:
    print(f'N[{N}] = {l}')
    N += 1
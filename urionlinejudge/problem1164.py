N = int(input())

for i in range(N):
    val = int(input())
    x = int(val/2)
    T = 0
    for j in range(1,x+1):
        if (val%j == 0):
            T = T+j
    if val == T:
        print(f'{val} eh perfeito')
    else:
        print(f'{val} nao eh perfeito')
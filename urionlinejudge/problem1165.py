N = int(input())

for i in range(N):
    X = int(input())
    c = 0
    for j in range(1,X+1):
        if (X%j==0):
            c = c+1
    if c == 2:
        print(f'{X} eh primo')
        
    else:
        print(f'{X} nao eh primo')
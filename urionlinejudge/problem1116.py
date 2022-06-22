N = int(input())


for i in range(N):
    X, Y = list(map(int,input().split(' ')))
    if Y == 0:
        print('divisao impossivel')
    else:
        r = X / Y
        print(r)

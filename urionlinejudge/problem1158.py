N = int(input())

for i in range(N):
    X, Y = list(map(int,input().split(' ')))
    if X % 2 != 0:
        Z = 0
        for i in range(1,Y+1):
            Z = Z+X
            X = X+2
        print(Z)
    else:
        X = X + 1
        Z = 0
        for j in range(1,Y+1):
            Z = Z + X
            X = X + 2
        print(Z)
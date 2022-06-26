while True:
    X = int(input())
    if X == 0:
        break
    elif X % 2 == 0:
        Z = 0
        for i in range(X,X+9):
            if i%2 == 0:
                Z = Z+i
        print(Z)
    elif X % 2 != 0:
        Z = 0
        for i in range(X,X+10):
            if i%2 == 0:
                Z = Z+i
        print(Z)
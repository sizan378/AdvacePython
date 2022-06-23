X = int(input())
Y = int(input())
t = X
if X > Y:
    X = Y
    Y = t

for i in range(X+1,Y):
    if i%5 == 2 or i%5 == 3:
        print(i)
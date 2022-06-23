v = 0
X = int(input())
Y = int(input())
t = X
if X > Y:
    X = Y
    Y = t
for i in range(X,Y+1):
    if (i%13 != 0):
        v = v + i
print(v)
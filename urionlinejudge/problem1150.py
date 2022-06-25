X = int(input())
Z = 0
while True:
    Z = int(input())
    if Z > X:
        break
sum = X
v = 1

while(sum < Z):
    sum += X + v
    v += 1

print(v)


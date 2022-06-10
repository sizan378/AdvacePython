X = int(input())
Y = int(input())

val = 0

for i in range(X-1,Y, -1):
    if i % 2 != 0:
        val = val + i
print(val)

    
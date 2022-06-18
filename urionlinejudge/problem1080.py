N = 0
A = 0

for i in range(0, 101):
    n = int(input())
    if n > N:
        N = n
        A = i
print(N)
print(A+1)

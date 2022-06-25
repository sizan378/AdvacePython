val = list(map(int,input().split(' ')))
N1 = 's'
N2 = 0
Total = 0

for i in val:
    if N1 == 's':
        N1 = i
    elif (i>0):
            N2 = i
            break
for i in range(N2):
    Total += N1
    N1 += 1

print(Total)
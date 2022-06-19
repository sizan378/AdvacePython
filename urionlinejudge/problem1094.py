N = int(input())
C = 0
R = 0
S = 0

for i in range(0, N):
    x, y = list(map(str,input().split(' ')))
    x = int(x)
    if y == "C":
        C = C + x
    elif y == "R":
        R = R + x
    else:
        S = S + x

Total = C + R + S
print(f'Total: {Total} cobaias')
print(f'Total de coelhos: {C}')
print(f'Total de ratos: {R}')
print(f'Total de sapos: {S}')
print(f'Percentual de coelhos: {(C*100)/Total:.2f} %')   
print(f'Percentual de ratos: {(R*100)/Total:.2f} %')  
print(f'Percentual de sapos: {(S*100)/Total:.2f} %')  


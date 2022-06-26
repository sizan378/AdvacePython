N = int(input())

for i in range(N):
    A,B,G1,G2 = input().split(' ')
    A = int(A)
    B = int(B)
    G1 = float(G1)
    G2 = float(G2)
    a = 0
    while(A<=B):
        CPA = int((A*(G1/100)))
        CPB = int((B*(G2/100)))
        a = a + 1
        A = A + CPA
        B = B + CPB
        if (a > 100):
            break
    if (a > 100):
          print('Mais de 1 seculo.')      
    else:
        print(f'{a} anos.')
A = int(input())

print(A)
for i in [100,50,20,10,5,2,1]:

    print(f'{A//i} nota(s) de R$ {i},00')
    A %= i
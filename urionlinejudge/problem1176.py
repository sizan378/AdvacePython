
N = int(input())

for i in range(N):
    I = int(input())
    f=[0,1]
    if I>1:
        for j in range(2,I+1):
           
            f.append(f[j-2]+f[j-1])
            
        print(f'Fib({I}) = {f[I]}')
    if I <=1:
        print(f'Fib({I}) = {f[I]}') 

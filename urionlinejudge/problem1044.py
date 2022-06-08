A, B = list(map(int, input().split()))

if B%A ==0 or A%B ==0:
    print(f'Sao Multiplos') 	
else:
    print(f'Nao sao Multiplos')
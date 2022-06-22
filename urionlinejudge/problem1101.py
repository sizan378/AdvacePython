
while(True):
    try:
        M, N = list(map(int,input().split(' ')))
        x = min(M, N)
        y = max(M, N)
        if M <= 0 or N <=0:
            break
        val = 0
        val_list = ''
        for i in range(x, y+1):
            val_list += str(i)+ ' '
            val = val + i
        print(f'{val_list} Sum={val}')
    except NameError:
        break
N = int(input())


for i in range(N):
    x, y = list(map(int,input().split(' ')))
    d = 0
    if x == y:
        print(0)
    else:
        z= 0
        if (x>y):
            z = x
            x = y
            y = z
        while( x < (y-1)):
            x +=1
            if(x%2!=0):
                d = d + x
        print(d)




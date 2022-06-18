N = int(input())

for i in range(0,N):
    a, b, c = list(map(float,input().split(' ')))[:3]
    avg = (a*2+b*3+c*5)/10
    print(f"{avg:.1f}")
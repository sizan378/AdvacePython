# x, y = list(map(int,input().split(' ')))

# for i in range(1, y+1):
#     print('%3d'%i, end='')
#     if (i+1) % x == 1:
#         print()

X,Y=input().split()
X=int(X)
Y=int(Y)
count=0
for i in range(1,Y+1):
    print(i,end=" ")
    count+=1
    if (count==X):
        print(" ")
        count=0
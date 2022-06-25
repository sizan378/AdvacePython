
N = int(input())

a = 0
b = 1

print(a,end=' ')
print(b,end=' ')
count = 2
while(1):
    c = a+b
    count+=1
    if(count==N):
        print(c)
        break
    else:
        print(c,end=' ')
        a=b
        b=c
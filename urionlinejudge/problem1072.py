A = 0
B = 0

for i in range(int(input())):
    n = int(input())
    if n>=10 and n<=20:
        A = A+1
    else:
        B = B+1
print(f'''{A} in
{B} out''')
A = 0

for i in range(int(input())):
    n = int(input())
    if n == 0:
        print("NULL")
    if n%2 == 0 and n > 0:
        print('EVEN POSITIVE')
    elif n%2 == 0 and n < 0:
        print('EVEN NEGATIVE')
    elif n%2 != 0 and n < 0:
        print('ODD NEGATIVE')
    elif n%2 != 0 and n > 0:
        print('ODD POSITIVE')

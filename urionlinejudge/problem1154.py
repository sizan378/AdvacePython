count = 0
val = 0
while True:
    num = int(input())
    if num>0:
        count += 1
        val = val + num
    elif num < 0:
        break

avg = val / count
print(f'{avg:.2f}')
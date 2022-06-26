
total = 0
val = 1
for j in range (1,40,2):
    sum = j/val
    total= total + sum
    val = val*2
print(f'{total:.2f}')


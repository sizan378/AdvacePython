
total = 0
val = 1
for j in range (1,40,2):
    sum = j/val
    total= total + sum
    val = val*2
print(f'{total:.2f}')

# b=1
# s=0
# for i in range(1,40,2):
#     m=i/b
#     s=s+m
#     b=b*2
#     print(b)
# print("%0.2f"%s)
pn = 0

avg = 0

for n in range(6):
    val = float(input())
    if val > 0:
        pn = pn + 1
        avg = avg + val

print(f'''{pn} valores positivos
{(avg/pn):.1f}''')
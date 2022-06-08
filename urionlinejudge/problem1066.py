even = 0
odd = 0
positiv = 0
neg = 0

for n in range(5):
    num = int(input())
    if num % 2 == 0:
        even = even +1
    elif num % 2 != 0:
        odd = odd + 1
    if num > 0:
        positiv = positiv + 1
    elif num < 0:
        neg = neg + 1
print(f'''{even} valor(es) par(es)
{odd} valor(es) impar(es)
{positiv} valor(es) positivo(s)
{neg} valor(es) negativo(s)''')
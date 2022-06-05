code1, proqun1, price1  = input().split(" ")
code2, proqun2, price2 = input().split(" ")

code1 = int(code1)
proqun1 = int(proqun1) 
price1 = float(price1)

code2 = int(code2)
proqun2 = int(proqun2) 
price2 = float(price2)

total = (int(proqun1) * float(price1)) + ( int(proqun2) * float(price2))
print(f'VALOR A PAGAR: R$ {total:.2f}')
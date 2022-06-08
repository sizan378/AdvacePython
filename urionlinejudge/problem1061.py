
# dia1 = int(input())
# h1, m1, s1 = list(map(int,input().split(' : ')))

# dia2 = int(input())
# h2, m2, s2 = list(map(int,input().split(' : ')))

# s = s2 -s1
# m = m2 - m1
# h = h2 - h1
# if dia2 == dia1:
#     print(f'0 dia(s)')
# else:
#     d = (dia2 - dia1)
#     print(f'{d} dia(s)')

# if h < 0:
#     h = h+ 24
#     print(f'{h} hora(s)')
# elif h == 0:
#     print(f'0 hora(s)')
# else:
#     print(f'{h} hora(s)')


# if m < 0:
#     m = m+60
#     print(f'{m} minuto(s)')
# elif m == 0:
#     print(f'0 minuto(s)')
# else:
#     print(f'{m} minuto(s)')



# if s < 0:
#     s = s+60
#     print(f'{s} segundo(s)')
# elif s == 0:
#     print(f'0 segundo(s)')
# else:
#     print(f'{s} segundo(s)')



dia,date1=input().split()
date1 = int(date1)
h1,m1,s1=map(int,input().split(":"))

dia,date2=input().split()
date2 = int(date2)
h2,m2,s2=map(int,input().split(":"))

s = s2 - s1
m = m2 - m1
h = h2 - h1
d = date2 - date1

if(s<0):
	s+=60
	m-=1


if(m<0):
	m+=60
	h-=1

if(h<0):
	h+=24
	d-=1

print(f"{d} dia(s)")
print(f"{h} hora(s)")
print(f"{m} minuto(s)")
print(f"{s} segundo(s)")
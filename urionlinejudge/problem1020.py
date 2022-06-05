days = int(input())

years = days // 365
month = days % 365
day = month % 30
month = month // 30

print(f'{years} ano(s)')
print(f'{month} mes(es)')
print(f'{day} dia(s)')
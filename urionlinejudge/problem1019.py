N = int(input())

minute = N // 60
hour = minute // 60
seconds = N % 60
minute = minute % 60
print(f'{hour}:{minute}:{seconds}')
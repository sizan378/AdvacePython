SH, SM, EH, EM = list(map(int,input().split(' ')))

Timecal = ((EH*60)+EM)-((SH*60)+SM)

if(Timecal<=0):
    Timecal = Timecal + (24*60)

time = Timecal//60
minute = Timecal%60
print(f'O JOGO DUROU {time} HORA(S) E {minute} MINUTO(S)')

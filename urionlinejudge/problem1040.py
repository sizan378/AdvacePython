N1, N2, N3, N4 = list(map(float,input().split()))

avg = (N1*2 + N2*3 + N3*4 + N4*1)/(2+3+4+1)

print(f'Media: {avg:.1f}')

if avg >= 7.0:
    print('Aluno aprovado.')
elif avg < 5.0:
    print('Aluno reprovado.')
elif avg >= 5.0 and avg <= 6.9:
    print('Aluno em exame.')
    N5 = float(input())
    print(f'Nota do exame: {N5:.1f}')
    avg2 = (avg+N5)/2
    if avg2 >= 5.0:
        print(f'Aluno aprovado.')
    elif avg2 <= 4.9:
        print(f'Aluno reprovado.')
    print(f'Media final: {avg2:.1f}')

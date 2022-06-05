A, B, C = input().split(' ')

A = float(A)
B = float(B)
C = float(C)

pi = 3.14159
radius = pi*C**2
t = (A * C)/2
trap = ((A + B)/2) * C
s = B**2
r = A * B

print(f'TRIANGULO: {t:.3f}')
print(f'CIRCULO: {radius:.3f}')
print(f'TRAPEZIO: {trap:.3f}')
print(f'QUADRADO: {s:.3f}')
print(f'RETANGULO: {r:.3f}')
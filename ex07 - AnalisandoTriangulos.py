'''Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''

a = float(input('Informe o comprimento do primeiro lado: '))

b = float(input('Informe o comprimento do segundo lado: '))

c = float(input('Informe o comprimento do terceiro lado: '))

if a < b + c and b < a + c and c < b + a:
    print('Os lados podem formar um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO.')
    elif a != b != c != a:
        print('ESCALENO.')
    else:
        print('ISÓCELES.')
else:
    print('Os lados não podem formar um triângulo.')
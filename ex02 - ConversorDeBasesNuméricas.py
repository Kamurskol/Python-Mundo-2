# -*- coding: utf-8 -*-

#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases de conversão:
[ 1 ] para binário;
[ 2 ] para octal;
[ 3 ] para hexadecimal. ''')
opçao = int(input('Sua opção: '))

if opçao == 1:
    print('O número {} convertido para binário é {}.'.format(num, bin(num)[2:]))
elif opçao == 2:
    print('O número {} convertido para decimal é {}.'.format(num, oct(num)[2:]))
elif opçao == 3:
    print('O número {} convertido para hexadecimal é {}.'.format(num, hex(num)[2:]))
else:
    print('VOCÊ TEM QUE ESCOLHER UM NÚMERO ENTRE 1, 2 E 3!')

''' Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segund número: '))

igual = n1 == n2

if n1 > n2:
    print('O PRIMEIRO número é maior.')
elif n2 > n1:
    print("O SEGUNDO número é maior.")
elif igual == True:
    print('Os dois números são IGUAIS.')

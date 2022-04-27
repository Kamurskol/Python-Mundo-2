#Crie um programa que faça o computador jogar Jokenpô com você.
from  random import randint
from  time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
cpu = randint(0, 2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')


escolha = int(input('Qual a sua jogada? '))

print('Pedra')
sleep(0.6)
print('Papel')
sleep(0.6)
print('Tesoura')
sleep(0.6)

print('\033[34m=-\033[m' * 14)
print('\033[32mO computador jogou {}.'.format(itens[cpu]))
print('\033[32mVocê jogou {}'.format(itens[escolha]))
print('\033[34m=-\033[m' * 14)

if cpu == 0:
    if escolha == 0:
        print('Empate.')

    elif escolha == 1:
        print('Jogador vence.')

    elif escolha == 2:
        print('Computador vence.')

    else:
        print('JOGADA INVÁLIDA.')
elif cpu == 1:
    if escolha == 0:
        print('Computador vence.')

    elif escolha == 1:
        print('Empate.')

    elif escolha == 2:
        print('Jogador vence.')

    else:
        print('JOGADA INVÁLIDA.')
if cpu == 2:
    if escolha == 0:
        print('Jogador vence.')

    elif escolha == 1:
        print('Computador vence.')

    elif escolha == 2:
        print('Empate.')

    else:
        print('JOGADA INVÁLIDA')
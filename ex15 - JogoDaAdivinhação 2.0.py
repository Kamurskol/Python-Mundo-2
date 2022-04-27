#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
from time import sleep

print('Sou seu computador...')
cpu = randint(0, 10)
print('Acabei de pensar em número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')

tentativas = 1

player = int(input('Qual o seu palpite? '))

sleep(0.7)

while player != cpu:

    if player > cpu:
        player = int(input('Menos... Tente mais uma vez. \n'))
        sleep(0.3)
        tentativas = tentativas + 1

    if player < cpu:
        player = int(input('Mais... Tente outra vez. \n'))
        sleep(0.3)
        tentativas = tentativas + 1

if player == cpu:
    print('Acertou com {} tentativas.'.format(tentativas))

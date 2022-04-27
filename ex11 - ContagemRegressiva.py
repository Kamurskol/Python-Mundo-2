#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep

pergunta = str(input('Iniciar contagem regressiva? (sim/nao) '))

if pergunta == 'sim':
    for contagem in range (10, 0-1, -1):
        print(contagem)
        sleep(1)
    print('bum.')
else:
    print('Então vá pra porra.')

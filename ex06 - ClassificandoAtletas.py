'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''
from datetime import date
atual = date.today().year

nasc = int(input('Digite seu ano de nascimento: '))

idade = (atual - nasc)

if idade <= 9:
    print('O atleta tem {} anos.\nClassificação: Mirim.'.format(idade))
elif 9 < idade < 15:
    print('O atleta tem {} anos.\nClassificação: Infantil.'.format(idade))
elif 15 < idade < 19:
    print('O atleta tem {} anos.\nClassificação: Júnor.'.format(idade))
elif 20 < idade < 25:
    print('O atleta tem {} anos.\nClassificação: Sênior.'.format(idade))
else:
    print('O atleta tem {} anos.\nClassificação: Master.'.format(idade))

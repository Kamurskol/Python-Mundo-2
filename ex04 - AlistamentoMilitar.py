from datetime import date

atual = date.today().year
nasc = int(input('Digite seu ano de nascimento: '))
idade = atual - nasc

print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if idade == 18:
    print('Você deve se alistar imediatamente.')
elif idade < 18:
    print('Ainda faltam {} ano(s) para você se alistar.'.format(18 - idade))
elif idade > 18:
    print('Você deveria ter se alistado há {} anos!\nSeu alistamento deveria ter acontecido em {}.'.format(idade - 18, nasc + 18))

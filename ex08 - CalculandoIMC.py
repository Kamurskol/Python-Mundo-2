'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''
peso = int(input('Digite seu peso (Kg):'))
alt = float(input('Digite sua altura (m): '))
imc = peso / (alt ** 2)

print(' O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc > 40:
    print('Essa pessoa tem OBESIDADE MÓRBIDA.')
elif 30 <= imc <= 40:
    print('Essa pessoa tem OBESIDADE.')
elif 25 <= imc <= 30:
    print('Essa pessoa tem SOBREPESO')
elif 18.5 <= imc <= 25:
    print('Essa pessoa está com uma faixa de peso SAUDÁVEL')

#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

sx = input('Informe seu sexo [M/F] ').strip().upper()[0]
while sx not in 'FfMm':
    sx = str(input('Dados inválidos. Informe seu sexo: '))
else:
    print('Sexo {} registrado com sucesso.'.format(sx.upper()))

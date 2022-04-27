#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Quantos anos de financiamento? '))

limite = salario * 0.30

meses = (anos * 12)

prst =(valor / meses)

print('Para pagar uma casa de R${} em {} anos, a prestação será de R${:.2f}'.format(valor, anos, prst))

if prst > limite:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo aprovado.')

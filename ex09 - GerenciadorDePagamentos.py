'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''
print(f'{"Lojas Gunabara":=^40}')

preco = float(input('Preço das compras: R$'))

print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista em dinheiro/cheque com 10% de desconto.')
print('[ 2 ] à vista no cartão com 5% de desconto.')
print('[ 3 ] 2x no cartão.')
print('[ 4 ] 3x ou mais no cartão com fodendos 20% de juros.')
opcao = int(input('Qual opção de pagamento você deseja? '))
opcao1 = 2

if opcao == 4:
    opcao1 = int(input('Quantas parcelas? '))


op1 = preco - (preco * 0.10)
op2 = preco - (preco * 0.05)
op3 = preco / 2
op4 = preco + (preco * 0.20)

#preco4 = op4  opcao1

if opcao == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, op1))
elif opcao == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, op2))
elif opcao == 3:
    print('Sua compra de R${:.2f} vai custar 2 parcelas de R${:.2f}'.format(preco, op3))
elif opcao == 4:
    print('Sua compra de R${:.2f} parcelada em {} vezes passa a custar fodendos R${:.2f}.'.format(preco, opcao1, op4))

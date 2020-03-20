#Elabre um programa que calcule o valor a ser pago por um produto,considerando o seu
#PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:
#á vista dinheiro/cheque: 10% de desconto
#a vista no cartão: 5% de desconto
#em até 2x no cartão: preço normal
#3x ou mais no cartão:20% de juros

print('===='*10)
print('Rodrigues Games')
print('===='*10)
produto = float(input('Digite o valor do produto R$'))

print('FORMAS DE PAGAMENTO')
opcao = print('''[1] á vista no Dinheiro/Cheque: 10% de desconto
         [2] á vista no cartão: 5% de desconto
         [3] Em até 2x no cartão: preço normal
         [4] 3x ou mais: 20% de juros''')
opcao = int(input('Escolha sua opção'))
if opcao == 1:
    desconto = produto - (produto*0.10)
    print('O pagamento á vista no Dinheiro ou cheque de {} ficará {} com 10% de desconto'.format(produto, desconto))
if opcao == 2:
    desconto = produto - (produto*0.05)
    print('O pagamento á vista no cartão de {} ficará {} com 5% de desconto'.format(produto,desconto))
if opcao == 3:
    desconto = produto
    parcela = produto / 2
    print('O pagamento ficára no preço normal mas com o pagamento parcelado {}'.format(produto))
elif opcao == 4:
    total = produto + (produto * 20 / 100)
    totparc = int(input('Quantas vezes?'))
    parcela = total / totparc
    print('O produto parcelado em {}x ficará R${:.2f} COM JUROS'.format(produto, total))
else:
    total = 0
    print('\033[31mOPÇÃO INVÁLIDA DE PAGAMENTO tente novamente')

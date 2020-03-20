#Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa.
#O programa vai perguntar o VALOR DA CASA, o SALARIO do comprador e em QUANTOS ANOS ele vai pagar.
#Calcule o valor da pretação mensal, sabendo que ela não pode excerder 30% do salário
#ou então o emprestimo será negado.
from time import sleep

casa = float(input('Digite o valor do empréstimo da casa! R$'))
sal = float(input('Digite seu salário! R$'))
fnc = int(input('Digite em quantos anos você irá pagar a casa!'))
prestacao=casa/(fnc * 12)
min = sal * (30/100)
print('O valor sera de {}' .format(casa, fnc), end='')
print(' A prestação é de R${:.2f}'.format(prestacao))

if prestacao <= min:
    print('\033[33m EMPRÉSTIMO CONCEDIDO!!!')
else:
    print('\033[31m EMPRESTIMO NEGADO não podemos pegar mais de 30% do seu salário!')
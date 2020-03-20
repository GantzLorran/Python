'''Crie um programa que leia Varios numeros inteiros pelo teclado. No final da execução
,mostre a média entre todos os valores e qual foi o maior e o menor valores lidos
O programa deve perguntar ao usuario se ele quer ou não continuar a digitar valores'''
n = 0
m = 0
s = ''
soma = qnt = m = 0 # se todas essas variaveis forem receber 0 pode colocar dessa maneira
maior = [] # os colchetes adiciona uma lista
while s in 'Ss':
    n = int(input('Digite um número: '))
    s = str(input('Deseja continuar [S/N]')).strip().upper()
    maior.append(n)# Faz uma lista de todos os números que estou digitando
    soma+=n
    if s == 'Nn':
        print('PROCESSANDO...')
m=soma/n
print('O media do número é {}'.format(m))# faz a média
print('O maior número digitado foi',max(maior))# Mostra o maior número
print('O menor número digitado foi',min(maior))# mostra o menor número


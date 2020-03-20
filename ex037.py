#escreva um programa que leia um numero inteiro qualquer
# e peça para o usuario escolher qual será a BASE DE CONVERSÂO
from time import sleep

numero = int(input('Digite um numero!'))

opcao = print('''
[ 1 ] Deseja converter seu número para binário 
[ 2 ] Deseja converter seu número para Octa 
[ 3 ] Deseja converter seu número para Hexadecimal''')
opcao = int(input('Sua escolha!'))
sleep(2)

if opcao == 1:
    print('O {} em binário é {}'.format(numero,bin(numero)))
elif opcao == 2:
    print('O número em Octa é {}' .format(numero, oct(numero)))
elif opcao == 3:
    print('O numero {} em hexadecimal é {}'.format(numero, hex(numero)))
else:
    print('Opção inválida! Tente novamente...')
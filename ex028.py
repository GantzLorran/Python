#Escreva um programa que faça o computador pensar
#em um numero entre 0 e 5 e peça para o usuario tentar
# descobrir qual foi o numero escolhido pelo computador

from random import randint
from time import sleep

numero = 0
#Faz o computador escolher um numero de 0 a 5
numero = randint(0,5)
print('O computador está pensando em um número de 0 a 5')
escolha = int(input('Qual número foi escolhido pelo computador? '))
print('PROCESSANDO...')
sleep(2)
if escolha == numero:
    print('Parabéns você acertou!')

else:
    print('Número errado! O número escolhido foi {}' .format(numero))

#Crie um programa que leia um numero inteiro
#e mostre se ele é par ou impar
from pip._vendor.distlib.compat import raw_input

numero = int(raw_input('Digite um numero!'))

if numero % 2 == 0:
    print('O numero {} é PAR!'.format(numero))
else:
    print('O numero {} é IMPAR'.format(numero))
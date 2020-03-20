'''Faça um programa que leia um numero qualquer e mostre o seu fatorial
ex: 5!= 5x4x3x2x1=120'''
from math import factorial
'''num = int(input('Digite um número e veja seu factorial: '))
f = factorial(num)
while num > f:
    f *= num
    num-= 1
print('O factorial do número {}!= {}'.format(num, f), end='')'''
num = int(input('Digite um número e veja seu factorial: '))
    #print('O factorial do número {} é {}'format(num, f))
c = num
f = 1
print('Calculando {}!'.format(c), end=' ')
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f*= c
    c-= 1
    print('{}'.format(f))
    #Lembrete tentar fazer com o comando FOR pedido do Gustavo Guanabara

'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma Tupla
Depois disso, mostre a listagem de números gerados e também indique o menor e o
maior valor que estão na tupla.'''

from random import sample

numero = tuple(sample(range(10), 5))
print(numero)
print(f'O menor é {min(numero)}')
print(f'O maior é {max(numero)}')
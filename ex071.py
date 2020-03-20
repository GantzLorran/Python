'''Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio,
pergunte ao usuário qual será o VALOR A SER CADASTRADO (número inteiro) e o
programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas: cédulas = [R$50, R$20, R$10 R$1]'''
from time import sleep

while True:
    saque = int(input('Digite o valor a ser sacado: Cédulas[R$50, R$20, R$10 R$1]: '))

    cem = int(saque/100)
    saque = saque % 100

    cinq = int(saque/50)
    saque = saque % 50

    vin = int(saque/20)
    saque = saque % 20

    dez = int(saque/10)
    saque = saque % 10

    cin = int(saque/5)
    saque = saque % 5

    um = int(saque/1)
    saque = saque % 1
    break
print('Fazendo contagem das notas')
sleep(2)
print('Notas R$: 100', cem)
print('Notas R$: 50', cinq)
print('Notas R$: 20', vin)
print('Notas R$: 10', dez)
print('Notas R$: 5', cin)
print('Notas R$: 1', um)
print('Obrigado por usar o banco RODRIGUES')


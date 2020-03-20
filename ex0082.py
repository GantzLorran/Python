'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os
valores impares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''
lista = []
listaPar = []
listaImpar = []
n =-1
print('O programa encerra quando você digitar 0')
while True:
    n = int(input('Digite números: '))
    lista.append(n)
    if n == 0:
        break
    if n % 2 == 0:
        listaPar.append(n)
    if n % 2 == 1:
        listaImpar.append(n)
print(f'Os números encontrados na lista foram {lista}')
print(f'Os números pares digitados foram {listaPar}')
print(f'Os números impares digitados na lista foram {listaImpar}')
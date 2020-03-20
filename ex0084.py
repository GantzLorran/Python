'''Faça um programa que leia o nome e o peso de várias pessoas, guardando tudo em uma lista.
No final mostre.
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais veles.'''
info = []
i = []
maiorPeso = 0
menorPeso = 0
while True:
    info.append(str(input('Digite o nome: ')))
    info.append(float(input('Digite o peso: ')))
    pergunta = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if len(i) == 0:
        maiorPeso = menorPeso = info[1]
    else:
        if info[1] > maiorPeso:
            maiorPeso = info[1]
        if info[1] < menorPeso:
            menorPeso = info[1]
    i.append(info[:])
    info.clear()
    if pergunta == 'N':
        break
print(f'Ao total foram cadastradas {len(i)} pessoas!')
print(f'O maior peso foi de {maiorPeso}Kg.', end='')
for c in info:
    if c[1] == maiorPeso:
        print(f'{c[0]}', end='')
print(f'O menor peso foi de {menorPeso}Kg.', end='')
for c in info:
    if c[1] == menorPeso:
        print(f'{c[0]}', end='')



'''Crie um programa aonde o usuario possa digitar sete valores numericos e cadastre-os
em uma LISTA UNICA saprados os valores pares e impares. No final mostre os valores
pares e impares em ordem crescente.'''

numeros = [[], []]

for c in range(0, 7):
    n = int(input(f'Digite um número: '))
    numeros.append(n)
    if n %2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print(f'Os números pares encontrados na lista foram {numeros[0]} e os impares foram {numeros[1]}')
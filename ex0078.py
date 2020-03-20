'''Faça um programa que leia 5 valores e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições
na lista.'''

lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
for c, v in enumerate(lista):
    break
print(f'Foram encontrados {lista} valores na lista')
print(f'O maior valor encontrado na lista foi {max(lista)} na posição {lista.index(max(lista))}')
print(f'O menor valor encontrado na lista foi {min(lista)} na posição {lista.index(min(lista))}')
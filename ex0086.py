'''Crie um programa que cria uma matriz de dimensão 3x3 e preencha com valores
lidos pelo teclado. No final mostre a matriz na tela com a formatação correta.
exemplo da MATRIZ
[ 1 ] [ 2 ] [ 3 ]
[ 4 ] [ 5 ] [ 6 ]
[ 7 ] [ 8 ] [ 9 ]'''
m = [[0,0,0], [0,0,0], [0,0,0]]

for c in range(3):
    for i in range(3):
        m[c][i] = int(input(f'DIgie um valor para [{c},{i}]: '))
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[{m[c][i]}]', end='')
    print()
#(:^5) centraliza o espaço
'''Faça um programa que tenha uma função chamada area()
,que receba as dimensões de um terreno retangular(largura e
comprimento) e mostra area do terreno.'''

def area(l, c):
    r = l * c
    print(f'A área de um terreno {l} x {c} é de {r}m²')
l = float(input('Largura: '))
c = float(input('Comprimento: '))
area(l, c)
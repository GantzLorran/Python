'''Crie um programa que tenha uma tupla totalmente preechida com uma contagem por extenso,
de zero até vinte.Seu programa deverá ler um número pelo teclado (ENTRE 0 e 20) e mostra-lo por extenso'''

numero = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
n = int(input('Digite um número de 0 a 20: '))

while n not in numero:
    n = int(input('Digite um número de 0 a 20: '))
    if n == numero:
       break
print(f'O {n} é um número por extenso!!!')

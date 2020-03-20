'''Faça um programa que mostre a tabuada de vários numeros, um de cada vez, para cada
valor digitado pelo usuário. O programa sera interrompido quando o número solicitado
for NEGATIVO'''
n = 0
#for count in range(1, 11):
while True:
    n = int(input('Digite um número para ver uma tabuada: '))

    if n > 0:
        for c in range(1, 11):
            print('{} X {} = {}'.format(n, c, n * c))
    if n < 0:
        break
print('Programa encerrado obrigado volte sempre!')
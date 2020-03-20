# Faça um programa que calcule a soma entre todos os numeros impares que são multiplos
# de três e que se encontram no intervalo de 1 até 500
s = 0
for count in range(1, 501, 2):
    if count % 3 == 0:
        s = s + count
        print('A soma é {}'.format(s), end='')

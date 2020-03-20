#if numero !=1 numeros impares(para ignorar os numeros impares)
#Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles
#que forem pares. Se o valor digitado for impar desconsidere-o.
s = 0
for c in range(1, 7):
    n1 = int(input('Digite um número: '.format(c)))
    if n1 % 2 == 0:
        s = s + n1
        c += 1
        print('O somatório de todos os números pares foram {}'.format(c,s))
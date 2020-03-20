'''Crie um programa que leia varios números inteiros pelo teclado o programa
só vai parar quando o usuario digitar o valor 999, que é a condição de parada.
No final mostre quantos números foram digitados e qual foi a soma entre eles
(DESCONSIDERANDO O FLAG)'''
n = s = 0
nm = -1
while True:
    nm +=1
    n = int(input('Digite um número (Digite 999 para imterromper o loop): '))
    if n == 999:
        break
    s += n
print(f'A soma é {s}')
print(f'A quantidade de números que você digitou foi {nm}')
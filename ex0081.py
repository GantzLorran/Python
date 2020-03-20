'''Crie um programa que vai ler vários números e colocar em uma lista.
depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

num = []
nmr = -1
print('Digite o número 0 para encerrar o programa')
while True:
    n = int(input('Digite um número: '))
    num.append(n)
    nmr += 1
    if n == 0:
        break
print(f'Foram digitados na lista {nmr} números na lista')
print(f'A ordem da lista é {sorted(num, reverse=True)}')
if 5 in num:
    num.append(5)
    print(f'O valor 5 foi encontrado na lista!')
else:
    print('O valor 5 não está na lista!')
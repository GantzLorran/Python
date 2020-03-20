'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostra:
A) Quantas vezes apareceu o valor 9. Usar length()
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''
par = 0
num = tuple(int(input('Digite um número: ').format(n+1))for n in range(4))
try:
    print(f'O valor 3 foi digitado na posição: {num.index(3)+1}ª')
except:
    print('O valor 3 não foi encontrado!')
print(f'O valor 9 foi digitado {num.count(9)} vezes!')
for n in num:
    if n % 2 == 0:
        par += 1
        print(f'Foram digitados {par} pares na telas!')

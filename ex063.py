'''Escreva um programa que leia um numero n inteiro e mostre na tela os n primeiros
elementos de uma sequencia de fibonacci:
ex 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8'''
n = int(input('Quantos termos da seqüencia de Fibonacci você quer ver?'))
f = 0
f2 = 1
print('{} -> {}'.format(f, f2), end='')
c = 3
while c <= n:
    f3 = f + f2
    print(' -> {} '.format(f3), end='')
    f = f2 #esse comnando faz o f mudar de linha com o f2 ex f vale 0 f2 vale 1
    # em seguida f vai valer 1 e f2 que valia 1, vai valer a soma do f com f2 ( f=0 f2=1 0+1=1
    f2 = f3
    c +=1
print('FIM!')
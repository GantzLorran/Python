#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
#mostre os 10 primeiros termos dessa progressão

n1 = int(input('Digite o termo PA Ex...(1 ou 2): '))
r = int(input('Informe a razão da PA Ex...(1 ou 2)'))
termo = n1 + (10-1)* r
for count in range(n1, termo+r, r):
    if r % 2 == 0:
        count +=0
        print('{} -> {}'.format(count, n1), end='')

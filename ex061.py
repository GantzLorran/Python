'''Rafaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10
primeiros termos da pregressão usando estrutura WHILE'''
n1 = int(input('Digite o termo PA Ex...(1 ou 2): '))
r = int(input('Informe a razão da PA Ex...(1 ou 2)'))
termo = n1 + (10-1) * r
c = n1
while c < termo:
    print('{}'.format(c))
    c = c + r
print('Terminou')
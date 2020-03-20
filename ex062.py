'''Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns
termos. O programa encerra quando ele disser que quer mostrar 0 termos.'''

n1 = int(input('Digite o termo PA Ex...(1 ou 2): '))
r = int(input('Informe a razão da PA Ex...(1 ou 2)'))
termo = n1 + (10-0) * r
n1 = n1
tot = 0
mais = 10
while mais != 0:
    tot = tot + mais
    while n1 < termo:
        print('{}'.format(n1),end=' -> ')
        n1 = n1 + r
        mais = int(input('Deseja mostrar mais algum termo?'))
print('FIM!!') # ainda não terminei esse exercicio o programa n esta fazendo
# o que o enunciado mandou
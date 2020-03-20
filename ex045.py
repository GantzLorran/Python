#Crie um programa que faça o computador jogar JOKENPÔ com você

from random import randint
from time import sleep
lista = ('PEDRA', 'PAPEL', 'TESOURA')
print('==='*4)
print('JOKENPÔ')
print('==='*4)
print('''Escolha uma opcão
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
input('Faça sua escolha!')
computador = randint(0,2)
jogador = 0
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('O computador escolheu {}'.format(lista[computador]))
print('O jogador escolheu {}'.format(lista[jogador]))

if computador == jogador:
    print('EMPATE!!!')
elif computador == 1 and jogador == 0:
    print('O Computador venceu')
elif computador == 0 and jogador == 1:
    print('O jogador venceu')
elif computador == 2 and jogador == 1:
    print('O computador venceu')
elif computador == 1 and jogador == 2:
    print('O jogador venceu')
elif computador == 0 and jogador == 2:
    print('O computador venceu')
elif computador == 2 and jogador == 0:
    print('O jogador venceu')

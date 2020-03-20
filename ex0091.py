'''Crie um programa onde 4 jogadores joguem um dado
e tenham resultados aletórios. Guarde esses resultados
em um dicionário. No final coloque esse dicionário
em ordem, sabendo que o vencedor tirou o maior número
no dado'''

from random import randint
from time import sleep
from operator import itemgetter
dado = {'jogador 1': randint(0, 6),
        'jogador 2': randint(0, 6),
        'jogador 3': randint(0, 6),
        'jogador 4': randint(0, 6)}
for k, v in dado.items():
    print(f'O jogador {k} sorteou {v}')
print('RANKING DOS JOGADORES')
ranking = list()
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
print(ranking)



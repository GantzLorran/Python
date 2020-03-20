'''Aprimore o desafio 0093 para que ele funcione com varios jogadores, incluindo
um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

jogador = {}
gol = []
tot = 0
jogador['nome'] = str(input('Digite o nome do jogador: '))
partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
for j in range(1, partidas):
    gol.append(int(input('Quantos gols na partida {}: '.format(j))))
for g in gol:
    tot+=g
print('-=-'*20)
print(f'{"cod. Nome":<4}{"Gols":>10}{"Total":>17}')
print(f'|Nome: {jogador["nome"]:<4}{tot:>17}|')
#parte 2
print('-=-'*20)
print(f'O campo nome tem o valor {jogador["nome"]}')
print(f'O campo gols tem o valor {gol}')
print(f'O total de gols tem o valor {tot}')
#parte 3
print('-=-'*20)
print(f'{jogador["nome"]} jogou {partidas} partidas')
for i in range(0, len(gol)):
    print(f'Na partida {i} ele fez {gol[i]} gols')




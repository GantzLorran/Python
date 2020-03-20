'''Crie um programa que gerencie o aproveitamento de um JOGADOR DE FUTEBOL.
O programa vai ler o nome do jogador e quantas partidas ele jogou. depois vai ler
a quantidade de gols feitos em cada partida.No final, tudo isso será guardado em um dicionário,
incluindo o total de gols durante o campeonato.'''
#parte 1
jogador = {}
gol = []
tot = 0
jogador['nome'] = str(input('Digite o nome do jogador: '))
partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
for j in range(1, partidas):
    gol.append(int(input('Quantos gols na partida {}: '.format(j))))
for g in gol:
    tot += g
print('-=-'*20)
print(f'|Nome: {jogador["nome"]}, gols: {gol}, total de gols: {tot}|')
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

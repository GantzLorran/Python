'''Faça um programa que tenha uma função receba dois
parametro opcionais: o nome de um jogador e quantos gols
ele marcou O programa deverá ser capaz de mostrar a
ficha do jogador, mesmo que algum dado não tenha sido informado corretamente
'''
def jgd(nome='<desconhecido>', gols=0):
    if nome == '<desconhecido>' and gols == 0:
        nome = '<desconhecido>'
        gols = 0
    if nome != '' and gols != 0:
        nome = nome
        gols = gols
    print(f'O jogador {nome} fez {gols} gols na partida!')
jogador = str(input('Digite o nome do jogador: ')).strip()
gol = int((input('Digite o número de gols: '))).strip()
print(jgd(jogador,gol))

'''if gol.isnumeric():
    gol = int(gol)
else:
    g = 0
if jogador.strip() == '':
    jgd(gols=g)
else:
    jgd(jogador, g)'''
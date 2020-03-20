'''Faça um programa que ajude um jogador de MEGA SENA a criar palpites. O programa
vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
para cada jogo, cadastrando tudo em uma lista composta.
ex... se o jogador quiser sortear 4 jogos ele deve gerar 4 listas'''
from random import sample
from time import sleep
print('-=-'*10)
print('         MEGA SENA')
print('-=-'*10)
escolha = int(input('Quantos jogos você deseja sortear? '))

#for c in range(1, escolha, 6):
for j in range(escolha):
    jogo = list()
    escolha = list()
    jogo.append(sample(range(1, 61), 6))
    print(f'Jogo: {j} = {jogo}')
    sleep(1)
    if escolha not in jogo:
        jogo.append(escolha)
    else:
        jogo.remove(escolha)
    jogo.sort()
print('-=-'*10)
print('BOA SORTE!!!')
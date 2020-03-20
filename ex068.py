'''Faça um programa que jogue par ou impar com o computador. O jogo só será imterrompido
quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou
no final do jogo'''
from random import randint
#if numero % 2 == 0:
v = 0
while True:
    jogador = int(input('Escolha um número: '))
    pc = randint(1, 10)
    tot = jogador + pc
    tipo = ''
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    print(f'Você {jogador} e o computador {pc}. Total de {tot}')
    if tipo == 'P':
        if tot % 2 == 0:
            print('Você VENCEU')
            v += 1
        else:
            print('Você PERDEU')
            break
    elif tipo == 'I':
        if tot % 2 == 1:
            print('Você VENCEU')
            v += 1
        else:
            print('Você PERDEU')
            break
    print('VAMOS JOGAR NOVAMENTE? ')
print(f'GAMER OVER! Seu número total de vitórias foram {v} vezes')
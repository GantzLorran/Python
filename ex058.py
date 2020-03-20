'''melhore o jogo do desafio 28 onde o computador vai 'pensar' em um número entre
0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no
final quantos palpites foram necessários para vencer. usar o Random(0, 10)'''

from random import randint
from time import sleep

numero = 0
escolha = 0
palpite = 0
#Faz o computador escolher um numero de 0 a 10
numero = randint(0,10)
print('O computador está pensando em um número de 0 a 10')
palpite+=1
while escolha != numero:
    escolha = int(input('escolha um número: '))
    if escolha == numero:
        print('Parabéns você acertou com {} tentativas'.format(palpite))


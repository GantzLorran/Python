'''Faça um programa que tenha uma função chamada maior(), que receba vários
parametros com valores inteiros. Seu programa tem que analisar todos os valores
e dizer qual deles é o maior.'''
from time import sleep
def maior(*num):
    print('-='*25)
    print('Analisando os valores passados')
    print('Foram encontrado {}'.format(len(num)))
    print('O maior valor encontrado foi {}'.format(max(num)))
    for elem in num:
        print(elem,end=' ',flush=True)
        sleep(0.5)

maior(9,7,5,2,1,10)
maior(4,7,0)
maior(6)
maior(0)

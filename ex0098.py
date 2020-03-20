'''Faça um programa que tenha uma função chamada contador()
qeu receba tres parametro: inicio, fim, passo e realize a contagem
seu programa tem que realizar tres contagens atraves da função
criada:
A) de 1 a 10 de 1 em 1
B) de 10 a 0, de 2 em 2
C) um contagem personalizada'''
from time import sleep
def contador(i,f,p):
    cont = i
    if p < 0:
        p*=-1
    if p == 0:
        p = 1
        print(f'Contagem: de {i} até {f} de {p} em {p}')

    while cont <= f:#Faz uma contagem normal
        print(f'{cont}',end=' ', flush=True)
        cont+=p
        sleep(0.5)
    while cont >= f:#Faz uma contagem de tras para frente
        print(f'{cont}', end=' ', flush=True)
        cont-=p
        sleep(0.5)
    return i,f,p
contador(1,10,1)
contador(10, 1, 2)
print('~'*10)
print('AGORA É SUA VEZ!!!')
print('~'*10)
ini = int(input('Número para início: '))
fim = int(input('Número para fim: '))
pas = int(input('Número para passo: '))
sleep(0.5)
contador(ini,fim,pas)
print('FIM!',end=' ')





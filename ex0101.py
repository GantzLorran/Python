'''Crie um programa que tenha uma função chamada voto()
que vai receber como parametro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto
NEGADO, OPICIONAL ou OBRIGATÓRIO nas eleições'''
from datetime import date
from time import sleep
def voto(nasc=0):
    ano = date.today().year#Esse comando calcula a idade da maneira correta ex 24 anos e não -24 anos
    r = (ano - nasc)
    print('Analisando idade...')
    sleep(1)
    if r >= 18:
        print(f'Você tem {r} anos e seu voto é OBRIGATÓRIO')
    elif r >= 16 and r < 18:
        print(f'Você tem {r} anos e seu voto é OPICIONAL')
    elif r > 65:
        print(f'Você tem {r} anos e seu voto é OPICIONAL')
    elif r <= 15:
        print(f'Você tem {r} anos e NÃO VOTA!')
print(voto(int(input('Em que ano você nasceu? '))))

'''nasc = int(input('EM que ano você nasceu? '))
print(voto(nasc))'''#Tambem posso fazer dessa forma
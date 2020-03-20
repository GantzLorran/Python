'''Faça um programa que tenha uma LISTA chamada números
e duas funções chamadas sorteia() e somarPar(). A primeira
função vai sortear 5 números e vai coloca-los dentro de uma lista
e a segunda função vai mostrar a soma entre todos os valores
PARES sorteados pela função anterior'''
from random import randint
from time import sleep
numeros = []
num = 0
def sorteia():
    while len(numeros) < 5:# Esse metodo faz uma lista com 5 numeros
        numeros.append(randint(1, 10))
        sleep(0.5)
    #numeros = random.sample(range(0,100), 5)
    print(numeros)
def somaPar():#Esse método pega os numeros que estão na lista numeros dentro do sorteia e soma os numeros pares
    sorteia()
    soma = 0
    num = 0
    for num in range (0, len(numeros)):
        if numeros[num] % 2 == 0:
            soma+=numeros[num]
    print(f'A soma de todos os valores pares foram {soma}')
#PROGRAMA PRINCIPAL
sorteia()
sleep(0.5)
print('Somando todos os valores pares')
sleep(0.5)
somaPar()

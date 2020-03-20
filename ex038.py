#enunciado
#escreva ou desenvolva um programa que leia dois numeros inteiros e compare-os, mostrando monstrando
#a seguinte mensagem
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

n1 = int(input('Digite um número!'))
n2 = int(input('Digite outro número!'))

if n1 > n2:
    print('O maior número é {}'.format(n1))
elif n2 > n1:
    print('O número maior é {}'.format(n2))
else:
    print('\033[33mNão existe valor maior, os dois são iguais!')
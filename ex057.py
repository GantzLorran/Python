'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
M ou F caso esteja errado, peça a digitação novamente até ter um valor correto'''

sexo = ''
sexo = str(input('Digite o sexo (M ou F):')).upper().strip()[0]#O zero é para pegar apenas a primeira letra
while sexo != 'M' and sexo != 'F':
    print('Você digitou errado tente novamente M ou F')
    sexo = str(input('Digite o seu sexo novamente (M ou F)')).upper().strip()
    if sexo == 'M' and 'F':
        print('You have been sucessfull')

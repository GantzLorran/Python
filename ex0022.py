#Crie um programa que leia o nome completo uma pessoa e mostre
# O nome com todas as letras maiusculas
# O nome com todas minusculas
# quantas letras aotodo(sem considerar espaços)
#quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo!')).strip()

print('Seu nome em maiusculo {}' .format(nome.upper()))
print('Seu nome em maiusculo {}' .format(nome.lower()))
print('Seu nome tem {}' .format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras' .format(nome.find(' ')))


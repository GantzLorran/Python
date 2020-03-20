#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente

#ex: Ana Maria de Souza
#primeiro = Ana
#ultimo = Souza

nome = str(input('Digite seu nome completo!')).strip().split()

print('É muito prazer em te conhecer!')
print('seu primeiro nome é {}' .format(nome[0]))
print('Seu último nome é {}' .format(nome[len(nome)-1]))

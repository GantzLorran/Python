# crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome

nome = str(input('Digite seu nome!')).split()

print('Seu nome tem Silva {}' .format('silva' in nome.lower()))
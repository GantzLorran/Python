#Crie um programa que leia uma FRASE qualquer e diga se ele é um PALINDROMO,desconsiderando os
# espaços
frase = str(input('Digite uma frase')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('A frase {} de trás para frente é {}'.format(junto, inverso))
if inverso == junto:
    print('Você fez um PALÍNDROMO')
else:
    print('A frase {} não é um PALÍNDROMO'.format(junto))

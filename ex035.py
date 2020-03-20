#Desenvolva um programa que leia o comprimento de tres
#retas e diga ao usuario se elas podem ou não formar um triangulo
from time import sleep

print('-=-' *20)
print('tente formar um triângulo')
print('-=-' *20)
r1 = float(input('Digite o primeiro segmento!'))
r2 = float(input('Digite o segundo segmento!'))
r3 = float(input('Digite o terceiro segmento!'))
print('Analisando...')
sleep(2)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os elementos podem formar um triângulo!')
else:
    print('Os elementos NÃO PODEM FORMAR um triângulo!')

# Refeça o Dsafio 0035 e explique qual tipo de triangulo ele pode formar
# Equilateros - todos os lados são iguais
# Isósceles - dois lados iguais
# Escaleno - Todos os lados diferentes
from time import sleep

print('====' * 10)
print('Forme um triângulo!!!')
print('====' * 10)
lado1 = float(input('Digite o primeiro segmento!'))
lado2 = float(input('Digite o segundo segmento!'))
lado3 = float(input('Digite o terceiro segmento!'))
print('PROCESSANDO...')
sleep(2)
if lado1 == lado2 > lado3:
    print('Os elementos {:.1f}, {:.1f}, {:.1f} formam o triângulo ISÓSCELES'.format(lado1, lado2, lado3))
if lado1 == lado2 == lado3:
    print('Os elementos {:.1f}, {:.1f}, {:.1f} formam o triângulo EQUILÁTEROS'.format(lado1, lado2, lado3))
if lado1 != lado2 > lado3 != lado1:
    print('Os elementos {:.1f}, {:.1f}, {:.1f} formam o triângulo ESCALENO '.format(lado1, lado2, lado3))
else:
    print('Esses elementos não formam um triângulo!')
# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:

#Escreva um que leia a velocidade de um carro
# se ele ultrapassar 80km por hora mostre uma mensagem dizendo
# que ele foi multado
#A multa vai custar R$7.00 por cada Km acima do limite

from time import sleep

km = 0
km = float(input('Digite a velocidade que você esta dirigindo! '))
multa = (km-80)*7
if km < 80:
    print('Tenha um bom dia! siga em frente! ')
else:
    print('Você foi multado por R${:.2f} a velocidade máxima nessa estrada é de 80km exato' .format(multa))
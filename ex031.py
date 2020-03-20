#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem cobrando R$0.50 por km para
#viagens de até 200km e R$ 0.45 para viagens mais longas.
import math

km = int(input('Digite a distancia em que você ira percorrer!'))

if km <= 200:
    print('O valor cobrado é de {}' .format(km*0.50))
else:
    print('Sua viagem passou de 200km o valor cobrado sera de {}' .format(km*0.45))

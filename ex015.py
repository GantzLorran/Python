d = int(input('Quantos dias você alugou o veículo '))

km = float(input('Quantos quilometros você percorreu com o seu veículo '))

pago = (d * 60.00) + (km * 0.15)
print('Você deve pagar {}R$ de aluguel '.format(pago))

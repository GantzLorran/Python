#Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre
#quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input('Digite seu ano de nascimento: '.format(c)))
    idade = ano - nasc #aqui fecha o comando for

    if idade >= 21: #aqui começa as condições
        maior+=1
    else:
        menor+=1
print('O número de pessoas que já atingiram a maioridade foram: {} e ainda iram atingir foram {}'.format(maior, menor))

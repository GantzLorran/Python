#Faça um programa que leia o peso de 5 pessoas. no final, mostre o maior e o menor peso lidos
maiorpeso = 0
menorpeso = 100
#lt = [] cria uma lista vazia
for c in range(1,3):
    peso = float(input('Digite o {}º peso:'.format(c)))
    #lt = peso 
    if peso > maiorpeso:
        maiorpeso = peso
    if peso < menorpeso:
        menorpeso = peso
print('O maior peso digitado foi {}kg'.format(maiorpeso))
print('O menor peso digitado foi {}kg'.format(menorpeso))
#Faça um programa que pergunte o salario
#de um funcionário e calcule o valor do seu aumento
sal = float(input('Digite seu salário! R$'))

if sal <= 1250:
    novo = sal + (sal*15/100)
    print('Seu salário agora é de {:.2f}'.format(novo))
else:
    novo = sal + (sal*10/100)
    print('Seu salário agora é de {:.2f}'.format(novo))

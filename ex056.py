#Desenvolva um programa que leia NOME, IDADE e SEXO de 4 pessoas. No final do programa
#.Mostre:
#A média de idade do grupo
#Qual é o nome do HOMEM MAIS VELHO
#Quantas mulheres têm menos de 20 anos
maisvelho = ''
nomemaisvleho = ''
qntmulheres = 0
qnthomens = 0
for count in range(1, 5):
    print('-------{}ª--------'.format(count))
    nome = str(input('Digite o {}º nome:'.format(count)))
    idade = int(input('Digite a {}ª idade:'.format(count)))
    sexo = str(input('Sexo (M/F)'.format(count)))
    media = idade+idade/4
    if count == 1 and sexo in 'Mm':
        maisvelho = idade
        nomemaisvleho = nome
    if sexo == 'M' and idade > qnthomens:
        qnthomens = idade
        nomemaisvleho = nome
    if sexo == 'F' and idade < 20:
        qntmulheres = qntmulheres +1
print('A idade média é {}'.format(media))
print('O homem mais velho se chama {} e ele tem {}'.format(nomemaisvleho, qnthomens))
print('O numero de mulheres com menos de 20 anos é de {}'.format(qntmulheres))

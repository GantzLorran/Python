'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada
, o programa deverá perguntar se o usuário quer continuar. No final mostre
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados
C) quantas mulheres tem menos de 20 anos usar max() min()'''
maior = homem = mulherMenor = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    while sexo not in 'FM':
        idade = int(input('Digite sua idade: '))
        sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
    pergunta = str(input('Quer continuar? S/N: ')).upper().strip()[0] #o zero indica que o cursor vai pegar só a primeira String
    if sexo == 'M':
        homem += 1
    if idade > 18:
        maior += 1
    elif sexo == 'F' and idade < 20:
        mulherMenor += 1
    if pergunta == 'N':
        break
print('AO TODO TEMOS!')
print(f'Total de homens cadastrados: {homem}')
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Total de mulheres com menos de 20 anos: {mulherMenor}')
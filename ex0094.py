'''Crie um programa que leia nome, sexo e idade de várias pessoas, guargando os dados de cada pessoa
em um dicionário
em uma lista no final, mostre:
A) quantas pessoas foram cadastradas.
B) a média de idade do grupo
C) uma lista com todas as mulheres
D) uma lista com as pessoas com idade acima da média'''
dados = dict()
mulheres = []
acimaMedia = []
glr = list()
p = 0
c = 0
media = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo: [M/F] ')).upper()
    dados['idade'] = int(input('Idade: '))
    p+=1
    media = dados['idade'] + dados['idade'] / len(dados)
    glr.append(dados.copy())
    pergunta = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if dados["sexo"] in 'Ff':
        mulheres.append(dados['nome'])#Mostra a lista só com as mulheres
    for c in dados:
        if dados['idade'] > media:
                acimaMedia.append(dados['nome'])
    if pergunta == 'N':
        break
print(f'No total temos {p} pessoas cadastradas!')
print(f'Á média de idade do grupo é {media:5.2f}')
print(f'As mulheres cadastradas foram {mulheres}')
print('-=-'*20)
print(f'Lista com pessoas com a idade maior do que a média {acimaMedia}')
for s in glr:
    if s["idade"] >= media:
        print('    ')
        for k, v in s.items():
            print(f'{k} = {v}; ', end='')





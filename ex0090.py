'''Faça um programa que leia nome e média de um aluno
guardando também a situação em um dicionário. No final
,mostre o conteúdo da estrutura na tela.'''

n = dict()
n['nome'] = str(input('Digite o nome: '))
n['media'] = float(input('Digite a média: '))

if n['media'] < 5:
    print(f'O aluno {n["nome"]} está reprovado com média {n["media"]}')
else:
    print(f'O aluno {n["nome"]} está aprovado com média {n["media"]}')
'''Crie um programa que leia nome, ano de nascimento
e carteira de trabalho e cadastre-os(com idade) em um
DICIONARIO se por acaso a CTPS for diferente de ZERO,
o dicionario receberá também o ano de contratação e o
salário. Calcule e acrescente, além da idade, com quantos
anos a pessoa vai se aposentar.'''
from datetime import datetime
cadastro = dict()
cadastro['nome'] = str(input('Digite seu nome: '))
cadastro['nasc'] = int(input('DIgite o ano nascimento: '))
cadastro['ctps'] = int(input('Digite o número da sua carteira de trabalho: (0 = Não tem) '))
if cadastro['ctps'] == 0:
    print(cadastro.items())
    print(f'O nome é {cadastro["nome"]}')
    print(f'Idade = {cadastro["nasc"]}')
    print(f'Carteira de trabalho = Não tem')
else:
    cadastro['cont'] = int(input('Digite o ano de contratação: '))
    cadastro['sal'] = float(input('Digite seu salário atual: '))
    print('RESULTADOS')
    print(cadastro)
    print(f'O nome tem o valor {cadastro["nome"]}')
    print(f'Idade tem o valor {cadastro["nasc"] - datetime.now().year}')
    print(f'A contratação foi no ano de {cadastro["cont"]}')
    print(f'O salário é de {cadastro["sal"]}')
    cadastro["aposentadoria"] = cadastro["nasc"] + ((cadastro["cont"] + 35) - datetime.now().year)
    print(f'A sua aposentadoria é dentro de {cadastro["aposentadoria"]}')


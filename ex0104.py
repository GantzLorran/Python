'''Crie um programa que tenha a função chamada leiaInt()
, que vai funcionar de forma semelhante a função input()
do Python, só que fazendo a validação para aceitar apenas
um valor numérico.

Ex:
n = leiaInt('Digite um n')'''
def leiaInt(n):
    n = str(input(n))
    while True:
        if not n.isnumeric():
            print(f'\033[31mERRO digite um número')
            break
        else:
            print(f'Você digitou o número {n}')
            return n
num = leiaInt('Digite um número: ')
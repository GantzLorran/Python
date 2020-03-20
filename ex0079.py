'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre
-os numa lista. Caso o número já exista lá dentro, ele não sera adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

n = []
pergunta = ''
while True:
    c = int(input('Digite um número: '))
    pergunta = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if c not in n:
        n.append(c)
        print(f'O valor {c} foi adicionado com sucesso!')
    else:
        print('Número ja encontrado na lista!')
    if pergunta == 'N':
        print('Terminado!')
        break
print(sorted(n))
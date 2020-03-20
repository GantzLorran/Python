'''Ultima aula de Pyhton '''
'''#cedulas = [10, 20, 50, 100]
n = s =0 # inicia uma variavel
while n != 999: # o numero da varial dentro do while nunca pode ser o mesmo numero que inica a variavel
    n = int(input('Digite um número:'))
    if n == 999:
        break# Comando break desconsidera o numero que esta no if
    s+= n
#s-=999# Ganbiarra
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}')#fstring é tipo um .format só que antes das aspas'''

nome = 'Lorran'
idade = 23
salário = 18700.00
print(f'O {nome} tem {idade} anos.')# python 3.6+
print('O {} tem {} anos.'.format(nome, idade))# python 3
print('O %s tem %d anos.' % (nome, idade))#moda antiga python 2

print(f'O {nome} tem {idade} anos e ganha R${salário:.2f}')
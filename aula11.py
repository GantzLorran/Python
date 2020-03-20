#Olá mundo com fundo lilás letra em negrito
print('\033[1;30;45mOlá mundo!\033[m')

#dando uma cor para cada caractere
a = 3
b = 5
print('Os valores são \033[31m{}\033[m e \033[34m{}\033[m'.format(a,b))
cores = {'limpa':'\033[m', 'azul':'\033[34m', 'amarelo': '\033[33m', 'pretoebranco':'\033[7;30m'}
nome = 'Lorran'
print('Olá! muito prazer em te conhecer,{}{}{}!' .format(cores['azul'], nome, cores['limpa']))


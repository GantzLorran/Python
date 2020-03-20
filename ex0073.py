'''Crie uma Tupla preenchida com os 20 primeiros colocados de tabela do Campeonato Brasileiro
de Futebol, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabéticas.
D) Em que posição na tabela está o time da posição Chapecoense.'''
a = b = c = []
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético',
         'Botafogo', 'Atlético-PR', 'Bahia', 'EC Vitória',
         'São Paulo', 'Fluminense', 'Sport-Recife',
          'Curitiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print(f'Times: {times}')

a = print(f'Os cinco primeiros colocados são: {times[0:5]}')

b = print(f'Os quatro últimos times colocados são: {times[-4:]}')

c = print('A ordem alfabética dos times é: ',sorted(times))

d = print(f'A Chapecoense está na posição {times.index("Chapecoense")+1}ª')

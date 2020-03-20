'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.
No final, mostre uma listagem de preços, organizando os dados de forma tabular.'''
produtos = ('Lápis', 0.50, 'Suco', 5.00, 'Playstation', 1500.00, 'TV-led', 1200.00, 'Xbox ONE', 1400.00, 'Forza Horizon 4', 200.00, 'The Last Of Us Part II', 250.00, 'Forza Horizon 3', 150.00)
print('====' * 10)
print('LOJAS RODRIGUES')
for c in range(0,( len(produtos)), 2):
    print(produtos[c],f'R$: {produtos[c+1]}')


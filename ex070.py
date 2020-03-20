'''Crie um programa que leia o nome e o preço de varios produtos. O programa deverá
perguntar se o uauário vai continuar. No final mostre:
A) qual é o total gasto na compra
B) Quantos produtos custam mais de R$ 1000
C) Qual é o nome do produto mais barato usar max() min()'''
s = c = tot = menor = maior = 0
pergunta = ''
while pergunta in 'Ss':
    c+=1
    p = str(input('Digite o nome do produto:'))
    n = float(input('Digite o preço do produto: R$'))
    tot+=n # faz o calculos dos preços enquanto a resposta for S
    pergunta = str(input('Deseja continuar [S/N]: ')).strip().upper()
    if n >= 1000:# Esse if faz uma verifica quais são os maiores preços
        maior += 1
    if c == 1 or n < menor:# Esse if verifica quais os menores preços
        menor += 1
        nome = p # A variavel nome vai pegar a pegar p
    if pergunta == 'Nn':
        break
print(f'O total da compra foi {tot}')
print(f'A quantidade de produtos que custam mais de R$1000 são {maior}')
print(f'O nome do produto com menor preço foi {nome}')
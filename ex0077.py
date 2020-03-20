'''Crie um programa que tenha uma TUPLA com várias palavras (NÂO USAR ACENTOS). Depois
disso você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavras = ('Lorran', 'Goku', 'Naruto', 'all Might', 'Luffy', 'Homem aranha', 'Homem de ferro',
            'Capitao america', 'Doutor estranho', 'Hulk')
for palavra in palavras:
    for vogais in palavra:
        if vogais.lower() in 'aeiou':
            print(f'{palavra.upper()} {vogais.lower()}')
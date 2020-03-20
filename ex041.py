#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
#e mostre sua categoria, de acordo com a idade:
#- até 9 anos: MIRIM
#- até 14 anos: infantil
#- até 19 anos: JUNIOR
#- até 20 anos: SENIOR
#- acima: MASTER
from datetime import date
idade = date.today().year
ano = int(input('Digite o ano em que você nasceu!!!'))
anos = idade - ano

if anos <= 9:
    print('Quem nasceu em {} tem {} anos e é um atleta MIRIM'.format(ano, anos))
elif anos <= 14:
    print('Quem nasceu em {} tem {} anos e é alteta INFANTIL'.format(ano, anos))
elif anos <= 19:
    print('Quem nasceu em {} tem {} anos e é atleta JÚNIOR'.format( ano, anos))
elif anos <= 25:
    print('Quem nasceu em {} tem {} anos e é atleta SÊNIOR'.format(ano, anos))
else:
    print('Quem nasceu em {} tem {} e é atleta MASTER'.format(ano, anos))
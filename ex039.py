#Faça um programa que leia o ano de um nascimento de um jovem e informe, de acordo com sua idade:
#- se ele ainda vai se alistar ao serviço militar
#- se é a hora de se alistar.
# se já passou do tempo de alistamento.
#O programa também deve mostrar o tempo que falta ou que passou do prazo
from datetime import date
nascimento = int(input('DIgite seu ano de nascimento!'))
ano = date.today().year
idade = ano - nascimento
if idade == 18:
    print('Você ja está com {} Você precisa se alistar \033[33mIMEDIATAMENTE'.format(idade))
elif idade < 18:
    sal = idade - 18
    print('Você ja está com {} ainda não está na hora de se alistar, faltam {} anos para você se alistar'.format(idade,sal))

elif idade > 18:
    sal = idade - 18
    print('Já passou do tempo de se alistar você está com {} você deveria ter se alistado há \033[31m{} anos'.format(idade,sal))

'''Faça um mini-sistema que utilize o interactive Help
do Python. O usuario vai digitar o comando e o manual
vai aparecer. Quando o usuario digitar a palavra FIM, o
programa se encerrará. OBS: use cores.'''
from time import sleep
c = [#tabela de cores
    '\033[m',
    '\033[0;30;41m',
    '\033[1;42m',
    '\033[1;43m',
    '\033[1;44m',
    '\033[1;45m',
    '\033[1;46m',
    '\033[1;47m',
    '\033[1;100m',
    '\033[1;101m',
    '\033[1;102m',
    '\033[1;103m',
    '\033[1;104m',
    '\033[1;105m',
    '\033[1;106m',
    '\033[1;107m'
]
def comando(com):#Pega o que foi digitado no while
    titulo(f'Acessando o manual do command \"{com}\"...', 4)
    sleep(0.5)
    print(c[6], end='')
    help(com)
    print(c[6], end='')
    sleep(0.4)
def titulo(msg, cor=0):
    tan = len(msg) + 4
    print(c[cor], end='')
    print('~' * tan)
    print(msg)
    print('~' * tan)
    print(c[0], end='')
#PROGRAMA PRINCIPAL
while True:
    titulo('PROMPT DE COMANDO DO PYTHON', 1)
    ajuda = str(input('Digite um comando que você queira ver: ')).strip()
    if ajuda.upper() == 'FIM':
        break
    else:
        comando(ajuda)
titulo('ATÉ LOGO...', 1)

from time import sleep

numero = ''
while numero == '':
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    escolha = int(input('''
    [1] somar
    [2] Multiplicar
    [3] dividir
    [4] Sair do programa'''))
    if escolha == 1:
        soma = n1 + n2
        print('O resultado da soma é {}'.format(soma))
    if escolha == 2:
        multiplicar = n1 * n2
        print('O resultado da multiplicação é {}'.format(multiplicar))
    if escolha == 3:
        dividir = n1/n2
        print('O resultado da divisão é {}'.format(dividir))
    if escolha == 4:
        print('Obrigado por usar o programa!')
        numero == ''
    sleep(2)
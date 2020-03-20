'''Crie uma programa que tenha uma função fatorial()
que receba dois parametros: o primeiro que indique o numero
a calcular e o outro chamado show, que será um valor lógico
(opcional)indicando se será mostrando ou não na tela o processo
de calculo do fatorial.'''
from math import factorial
def fatorial(num, show=False):
    """
    -> Informações do programa!
    :param num: pegar o número digitado
    :param show: (OPCIONAL) mostrar a fórmula da conta
    :return: retorna os resultados do fatorial ou da fórmula
    """
    c = num
    f = 1
    print('Calculando {}!'.format(c), end=' ')
    while c > 0:
        print('{}'.format(f), end=' ')
        print(' x ' if c > 1 else ' = ', end=' ')
        f *= c
        c -= 1
        print('{}'.format(f))
        for c in range(f, 0,-1):
            if show == True:
                print(f'{c} x ', end=' ')
                return f
            else:
                return num
#print(factorial(int(input('Digite um numero para o fatorial: '))))
fatorial(5, show=True)

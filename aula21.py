'''def contador(i, f, p):
    """ #docstring
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= i:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

help(contador)'''

'''#paramêtros opicionais exmeplo
def somar(a=0, b=0, c=0):
    """
    -> Fazer soma com paramêtros opicionais
    :param a: a vale o primeiro valor
    :param b: b vale o segundo valor
    :param c: c vale o terceiro valor
    """
    somar = a + b + c
    print(f'A soma valor {somar}')
somar(a = 4 , b = 2 , c = 4)'''

'''def teste():
    x = 8 # variável local
    print(f'Na função teste n vale {n}')
    print(f'Na função teste x vale {x}')

#programa principal
n = 2 # variável global
print(f'Na função teste n vale {n}')
print(f'Na função teste x vale {x}')'''

'''def somar(a=0,b=0,c=0):
    s = a + b + c
    return s
r1 = somar(3,2,5)
r2 = somar(2,2)
r3 = somar(6)

print(f'Os valores das somas são {r1} {r2} {r3}')'''

'''def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
        return f
n = int(input('Digite um número: '))
print(f'O factorial de {n} é igual a {fatorial(n)}')'''
print(input.__doc__)
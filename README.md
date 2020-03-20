# Python
Meus trabalhos em Python
def moeda(valor):
    """

    :param valor: Retorna um valor digitado pelo usuário
    :return:
    """
    return f'R$ {valor}'.replace('.', ',')
def aumentar(n):
    return moeda (n + (n * 10/100))
def diminuir(n):
    return moeda (n - (n * 13/100))
def dobrar(n):
    return moeda(n*2)
def metade(n):
    return moeda (n / 2)

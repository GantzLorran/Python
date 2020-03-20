''' Faça um programa que tenha uma função notas() que
pode receber varias notas de alunos e vai retornar um dicionario
com as seguintes informações:
Quantidade de notas
A maior nota
A menor nota
A média da turma
A situação (Opcional)
Adicione também as docstrings de função '''
from collections import OrderedDict
def notas(*resp, sit=False):
    """
    -> Função para analisar notas
    :param resp: um ou mais notas dos alunos
    :param sit: valor opicional
    :return:dicionário que retorna todos os valores
    """
    r = dict()
    r['total'] = len(resp)
    r['maior'] = max(resp)
    r['menor'] = min(resp)
    r['media'] = sum(resp)/len(resp)
    sit = bool
    if sit:
        if r['media'] < 7:
            print('\033[31mSITUAÇÃO RUIM...')
        elif r['media'] >= 7:
            print('\033[94mSITUAÇÃO ÓTIMA...')
        elif r['media'] >= 5 and r['media'] <= 6:
            print('\033[33mSITUAÇÃO RAZOÁVEL')
        if sit == False:
            del sit
    return r
    #calcula todas as notas cadastradas e gera uma média

#Programa Principal
n = notas(1.5, 2.0, 0.9, sit=False)
print(n)
help(notas)
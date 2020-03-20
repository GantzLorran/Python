'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista
composta. No final mostre um boletim contendo a média de cada um e permita que o usuario
possa mostrar as notas de cada aluno individualmente.'''
lista = list()
vlr = list()
c = 0
a = 0
while True:
    #Dados
    lista.append(str(input('Digite seu nome: ')))
    lista.append(float(input('Digite sua primeira nota: ')))
    lista.append(float(input('DIgite sua segunda nota: ')))
    m = lista[1] + lista[2] / 2
    vlr.append(lista[:])
    lista.clear()
    m = 2
    p = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if p == 'N':
        break
print(f'{"Nº":<4} {"NOME":<10} {"NOTA":<7}')
print('-----'*5)
for c in range(len(vlr)):#Esse for faz uma contagem correta bem alinhada de para baixo do primeiro ao ultimo
                         #Se caso eu esquecer do que eu to falando execute o programa e veja
    #print('Desse jeito que ficara a lista!!')
    print(f'{c:<4}',end='')
    print(f'{vlr[c][a]:<10}',end='')
    print(f'{vlr[c][m]:<7}')
#PARTE 2
while True:
    nt = int(input('Quais notas você deseja ver? digite 999 para parar o programa: '))
    if nt == 999:
        break
    if nt <= len(vlr) - 1:
        print(f'Notas de {vlr[nt][0]} são {vlr[nt][1]}')

#for i, a in enumerate(vlr): tbm posso fazer dessa maneria i pega o nome e a pega as notas

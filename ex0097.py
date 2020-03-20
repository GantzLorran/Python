'''Faça um programa que tenha uma função chamada escrava()
que receba um texto qualquer como parametro e mostre uma
mensagem com tamanho adaptável ex: escreva(Ola,Mundo!)
saída Olá, Mundo!'''

#len(txt)+4
def escreva(txt):
    print('~'*len(txt))
    print(txt)
    print('~'*len(txt))
txt = input('Digite uma frase: ')
escreva(txt)

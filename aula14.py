'''for c in range(1, 10):
    print(c)
    print('Fim')'''

'''c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')'''

'''n = 1
while n != 0: #flag(condição de parada)
    n = int(input('Digite um valor! '))
print('FIM')'''

#while not in 'MmFf':

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor'))
    r = str(input('Quer continuar: [S/N]')).upper()
print('Fim')'''

'''n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor'))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print('Você digitou {} numeros pares e {} números impares'.format(par, impar))'''
lista = []
while True:
    n = int(input('Digite o número (0 para encerrar): '))
    lista.append(n)
    if n == 0:
        break


print ('O maior número da lista é: ',max(lista))

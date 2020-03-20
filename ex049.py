#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolhe, só que
#agora utilizando um laço FOR.
n = int(input('Digite um numero! '))
for count in range(1, 11):
    print('{} x {} = {}'.format(n, count, n * count))


    #for c in range(0, 6):
    #print('Olá mundo!')
#print('FIM!')
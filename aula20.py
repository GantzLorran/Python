'''def título(txt):#Função com parâmetro
    print('-' * 30)
    print(txt)
    print('-' * 30)
#def lin():#Adiocina Linhas aonde eu quiser
#Programa Principal
título('Curso em Vídeo  ')
título('Python é muito BOOOOM!')
título('OIIII')'''

'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(s)#o que esta dentro do parenteses se chama parâmetro
    print(f'A soma vale A + B = {s}')
# Programa Principal
soma(a=4, b=5)
soma(7, 2)'''

'''def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')
    for valor in num:
        print(f'{valor}', end=' ')
    print('FIM!')
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
valores = [6, 8, 4, 1, 4, 5]
dobra(valores)
print(valores)

'''def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)'''


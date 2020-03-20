'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)#adiciona um numero
num.sort(reverse=True)
num.insert(2, 2)
num.pop()#eliminar valor dentro da lista
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')# faz uma contagem dos elementos que estão na lista'''

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei no final da lista.')

'''a = [2, 3, 4, 7]
b = a[:]
b[2] = 8# apartir do momento que eu igualo uma lista na outro o python faz uma ligação entre elas IMPORTANTE
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''


lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata fritas')  # Isso é uma Tupla
# Tuplas são imatáveis
# lanche[1] = 'Refrigerante'#essa forma é errada
# print(lanche[-2])
for comida in lanche:
    print(f'Eu vou comer {comida}')
    
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, c in enumerate(lanche):
   print(f'Eu vou comer {c}')
print('Comi pra carai!!!')

#print(sorted(lanche))#sorted colocar em ordem
#print(lanche)

#Essas tuplas irá juntar a e b quando somarmos a+b e transformar em uma linha só
'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
#count mostra quantos numeros tem na lista
print(c.index(8))#index mostra em qual posição o numero esta'''

pessoa = ('Lorran', 23, 'M', 67.56)
del(pessoa)
print(pessoa)
#TUPLAS AULA #16
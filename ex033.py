# Faça um pograma que leia tres numeros e mostre qual o maior e qual o menor

n1 = int(input('Digite um número!'))
n2 = int(input('Digite outro número!'))
n3 = int(input('Digite um último número!'))
# Verificando o menor núemro!
menor = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando o maior número!
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

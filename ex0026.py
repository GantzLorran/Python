#faça um programa que leia o nomede uma pessoa mostrando em
# seguida o primeiro e o ultimo nome separadamente

frase = str(input('Digite uma frase! ')).strip().upper()

print('A letra A aparece',frase.count('A'),'vezes na frase')#vai contar quantas letras A existem na frase
print('A letra A apareceu na posição {}'.format(frase.find('A')+1))# vai localizar o primeiro caractere da frase
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))#vai localizar um caractere da direita para esquerda
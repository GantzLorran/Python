frase = 'Curso em video python'

print(frase[::12])
print('Curso' in frase)
print(frase.count('C'),'A letra C aparece ' .format('C'),' vezes')
#print(frase.replace('python','Android'))

dividido = frase.split()
print(dividido[2][3])
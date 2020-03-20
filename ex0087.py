'''Aprimore o defasio 0086, mostrando no final:
A) A soma dos valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''
m = [[0,0,0], [0,0,0], [0,0,0]]
p = co = 0
for c in range(3):
    for i in range(3):
        m[c][i] = int(input(f'DIgie um valor para [{c},{i}]: '))
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[{m[c][i]}]', end='')
        print()
        if m[c][i] %2 == 0:
            p+=m[c][i]
        if c == 2:
            co+=m[i][2]
print(f'A soma dos valores pares digitados na coluna foi {p}')
print(f'A soma dos valores digitados na terceira coluna foi {co}')
print(f'O maior valor da 2ª linha foi {max(m[1])}')
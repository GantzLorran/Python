teste = list()
teste.append('Lorran')
teste.append(40)
print(teste)
#para isso não ficar igual bastar colocar [:] no galera.append
galera = list()
galera.append(teste[:])
print(galera)
teste[0] = 'Lorran Uchiha'
teste[1] = 22
galera.append(teste[:])
print(galera)

'''galera = [['João', 20], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[2][1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')'''

'''galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores de idade e {totmen} menores de idade!')'''
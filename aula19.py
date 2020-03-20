'''pessoas = {'nome': 'Lorran', 'sexo': 'M', 'idade': 22}
#pessoas['peso'] = '100.0' #Esse comando adiciona uma linha

for k, v in pessoas.items():
    print(f'{k} = {v}')'''

#print(pessoas.items())
#print(pessoas.values())
#print(pessoas.keys())
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

'''Brasil = []
estado1 = {'uf': 'Rio de janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
Brasil.append(estado1)
Brasil.append(estado2)
print(Brasil[0]['sigla'])'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Silga do Estado: '))
    brasil.append(estado.copy())#Jamais podemos fazer um fatiamento em um dicionario fatiamento se faz desse jeito
    # ---> [:]
for e in brasil:
    for k, v in e.keys():
        print(v, end=' ')
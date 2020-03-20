nome = str(input('Qual é o seu nome?'))
if nome =='Lorran':
    print('Que nome bonito!')
elif nome == 'Antonio' or nome == 'Goku' or nome == 'L':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Lorran Antonio Rodrigues':
    print('Belo nome Masculino!')
else:
    print('Bom dia Seu nome é normal!')
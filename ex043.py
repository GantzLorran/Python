#Desenvolva uma lógica que leia o peso e a altura de uma pessoa IMC e mostre seu status abaixo, de acordo
#- Abaixo de 18.5: abaixo do peso
#- Entre 18.5 e 25: peso ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#acima de 40: Obesidade mórbida
kg = float(input('Qual seu peso?'))
al = float(input('Qual sua altura?'))

imc = kg/(al**2)


if imc < 18.5:
    print('Seu IMC é igual a {:.1f} e você esta ABAIXO DO PESO!'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é igual a {:.1f} e você esta no peso NORMAL!'.format(imc))
elif imc >= 25 and imc <= 30:
    print('Seu IMC é igual a {:.1f} e você esta SOBREPESO!'.format(imc))
elif imc >= 30 and imc <= 40:
    print('Seu IMC é igual a {:.1f} e você esta com OBESIDADE!'.format(imc))
else:
    print('Seu IMC é igual a {:.1f} e você esta com OBESIDADE MÓRBIDA!'.format(imc))
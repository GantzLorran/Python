'''Crie um programa que leia vários números inteiros pelo telcado. O programa só vai
parar quando o usuario digitar o valor 999, que é a condição de parada. No final
,mostre foram digitados e qual foi a soma entre eles (desconsiderando o flag)'''

n = r = 0
num = -1 # Esse método desconsireda o ultimo número
while n != 999:
    num +=1#Esse método faz a contagem de números que o usúario irá fazer durante o processo while
    r+= n# faz a soma dos números
    n = int(input('Digite o número [999 para parar]'))
    if n == 999:
        break
print('A soma dos núemros que você digitou foram {}'.format(r))
print('E a quantidade de números que você digitou foram {}'.format(num))

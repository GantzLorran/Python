#Crie um programa que leia duas notas de um aluno calcule sua média, mostrando no final, de acordo
#com sua média atingida:
#- Média abaixo de 5.0 REPROVADO
#- Média entre 5.0 e 6.9 RECUPERAÇÃO
#- Média 7.0 ou superior APROVADO

n1 = float(input('Digite sua primeira nota!'))
n2 = float(input('Digite sua segunda nota!'))

media = (n1+n2)/2

if media <= 5:
    print('\033[31mVocê está REPROVADO com média {}!!!\033[31m'.format(media))
elif 7 > media >= 5:
    print('\033[33mVocê está em recuperação gafanhoto com média {:.1f}!!!\033[33m'.format(media))
elif media >= 7:
    print('\033[34mParabéns gafanhoto você esta aprovado com média {}!!!\033[34m'.format(media))

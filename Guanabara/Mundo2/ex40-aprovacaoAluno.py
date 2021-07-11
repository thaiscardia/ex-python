"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a média atingida:
- média abaixo de 5.0: reprovado
- média entre 5.0 e 6.9: recuperação
- média 7.0 ou superior: aprovado"""

nota1 = float(input("Insira primeira nota: "))
nota2 = float(input("Insira segunda nota: "))
media = (nota1 + nota2)/2

if media < 5.0 or media == 4.9:
    print("REPROVADO, média {}".format(media))
elif media == 5.0 or media <= 6.9:
    print("EM RECUPERAÇÃO, média {}".format(media))
else:
    print("APROVADO, média {}".format(media))
"""Faça um programa que leia o sexo de uma pessoa e só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto. 
"""

sex = str(input("Digite o sexo: \n[F] Feminino \n[M] Masculino \n")).strip().upper()[0]

while sex not in "MF":
    sex = str(input("Dados Inválidos. Digite o sexo: \n[F] Feminino \n[M] Masculino \n")).strip().upper()[0]
else:
    print('Sexo {} registrado com sucesso.'.format(sex))